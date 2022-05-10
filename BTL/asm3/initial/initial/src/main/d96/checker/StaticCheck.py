"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *

ENABLE_PRIVATE_ATTRIBUTE = False
ENABLE_ARRAYLIT_COERCE = False

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType(' + ', '.join([str(self.partype), str(self.rettype)]) + ')'

# Class Identifier == NameSpace (NS)
class NSType:
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "CName(" + self.cname + ")"

class Symbol:
    def __init__(self, name, mtype, is_const = False):
        self.name = name
        self.mtype = mtype
        self.is_const = is_const

    def __str__(self):
        return 'Symbol(' + ', '.join([str(self.name), str(self.mtype), str(self.is_const)]) + ')'


class StaticChecker(BaseVisitor):

    def __init__(self, ast):
        self.ast = ast
        self.curr_method_sym = None
        self.curr_class_name = None
        self.is_in_loop = False
        self.is_declaring_static = False
        self.has_explicit_constructor = False
        self.has_explicit_return = False

    def check(self):
        return self.visit(self.ast, None)


    """
            HELPERS
    """

    def log(self, msg):
        print('='*60)
        print(str(msg))
        print('='*60)

    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def lookup_attribute(self, attr_name, class_name, stack) -> (None or Symbol):
        classes = stack if isinstance(stack, dict) else stack[-1]
        if class_name in classes:
            syms = classes[class_name]
        else:
            raise Undeclared(Class(), class_name)
        for sym in syms:
            if sym.name == attr_name and not isinstance(sym.mtype, MType):
                return sym
        return None

    def lookup_method(self, method_name, class_name, stack) -> (None or Symbol):
        classes = stack if isinstance(stack, dict) else stack[-1]
        if class_name in classes:
            syms = classes[class_name]
        else:
            raise Undeclared(Class(), class_name)
        for sym in syms:
            if sym.name == method_name and isinstance(sym.mtype, MType):
                return sym
        return None

    def lookup_in_local_scopes(self, name, stack) -> (None or Symbol):
        # If not in local scope, return none
        if len(stack) == 1 or isinstance(stack, dict):
            return None
        for scope in stack[:-1]:
            sym = self.lookup(name, scope, lambda sym: sym.name)
            if sym: return sym
        return None

    def check_undeclared_class(self, classtype, stack):
        classes = stack[-1] if isinstance(stack, list) else stack
        if isinstance(classtype, ClassType):
            if not classtype.classname.name in classes:
                raise Undeclared(Class(), classtype.classname.name)
            else:
                return classtype
        else:
            # Parameter is not classtype, returning
            return classtype

    def check_args_match_params(self, ast, method_sym, stack):
        err = TypeMismatchInExpression if isinstance(ast, Expr) else TypeMismatchInStatement
        # Check param len
        if len(ast.param) != len(method_sym.mtype.partype):
            raise err(ast)
        # Check param type
        for (arg, partype) in list(zip(ast.param, method_sym.mtype.partype)):
            vartype = self.visit(arg, stack)
            if not self.can_coerce(partype, vartype):
                raise err(ast)

    def check_obj_and_mem_name(self, ast: (CallExpr or CallStmt or FieldAccess), stack) -> Symbol:
        mem_name = ast.fieldname.name if isinstance(ast, FieldAccess) else ast.method.name
        is_callee_static = '$' in mem_name
        err = TypeMismatchInExpression if isinstance(ast, Expr) else TypeMismatchInStatement

        # If calling static, immediately check if that class has been declared
        if is_callee_static:
            self.check_undeclared_class(ClassType(ast.obj), stack)
            class_name = ast.obj.name
        else:
            caller_type = self.visit(ast.obj, stack)
            # If caller is a class name, then must throw illegal member access
            if isinstance(caller_type, NSType):
                raise IllegalMemberAccess(ast)
            if not isinstance(caller_type, ClassType):
                raise err(ast)
            # If access an instance inside a static method
            if self.is_declaring_static:
                raise IllegalMemberAccess(ast)
            class_name = caller_type.classname.name
        
        if ENABLE_PRIVATE_ATTRIBUTE:
            if class_name != self.curr_class_name and isinstance(ast, FieldAccess):
                # Accessing public attribute
                if is_callee_static:
                    pass
                # Accessing private attribute
                else:
                    raise IllegalMemberAccess(ast)
        
        if isinstance(ast, FieldAccess):
            attr_sym = self.lookup_attribute(mem_name, class_name, stack)
            if attr_sym:
                return attr_sym
            else:
                raise Undeclared(Attribute(), mem_name)
        else:
            method_sym = self.lookup_method(mem_name, class_name, stack)
            if method_sym:
                return method_sym
            else:
                raise Undeclared(Method(), mem_name)
    
    def check_method_call(self, ast: (CallExpr or CallStmt), stack):
        method_sym = self.check_obj_and_mem_name(ast, stack)
        self.check_args_match_params(ast, method_sym, stack)

        if isinstance(ast, CallStmt) and not isinstance(method_sym.mtype.rettype, VoidType) or \
        isinstance(ast, CallExpr) and isinstance(method_sym.mtype.rettype, VoidType):
            raise TypeMismatchInStatement(ast) if isinstance(ast, CallStmt) else TypeMismatchInExpression(ast)

        return method_sym.mtype.rettype

    def can_coerce(self, tleft, tright):
        if type(tleft) == type(tright):
            if isinstance(tleft, ArrayType):
                return self.can_coerce(tleft.eleType, tright.eleType) and tleft.size == tright.size
            elif isinstance(tleft, ClassType):
                return tleft == tright
            return True
        elif type(tleft) == FloatType and type(tright) == IntType:
            return True
        elif type(tleft) == ClassType and type(tright) == VoidType:
            return True
        elif type(tleft) == VoidType and type(tright) == ClassType:
            return True
        return False

    def is_const(self, value, stack):
        if value is None:
            return False
        elif isinstance(value, Literal):
            return True
        elif isinstance(value, Id):
            var_sym = self.lookup_in_local_scopes(value.name, stack)
            if var_sym:
                return var_sym.is_const
            else:
                raise Undeclared(Identifier(), value.name)
        elif isinstance(value, FieldAccess):
            ctype = self.visit(value.obj, stack)
            if isinstance(ctype, ClassType):
                dot_sym = self.lookup_attribute(value.fieldname.name, ctype.classname.name, stack)
                if dot_sym:
                    return dot_sym.is_const
                else:
                    raise Undeclared(Attribute(), value.fieldname.name)
            elif isinstance(ctype, NSType):
                dot_sym = self.lookup_attribute(value.fieldname.name, ctype.cname, stack)
                if dot_sym:
                    return dot_sym.is_const
                else:
                    raise Undeclared(Attribute(), value.fieldname.name)
            else:
                raise TypeMismatchInExpression(value)
        elif isinstance(value, ArrayCell):
            return self.is_const(value.arr, stack)
        elif isinstance(value, NewExpr):
            return True
        elif isinstance(value, UnaryOp):
            return self.is_const(value.body, stack)
        elif isinstance(value, BinaryOp):
            return self.is_const(value.left, stack) and self.is_const(value.right, stack)
        return False

    def is_in_main(self):
        return self.curr_class_name == 'Program' and \
            self.curr_method_sym.name == 'main' and \
            len(self.curr_method_sym.mtype.partype) == 0 and \
            isinstance(self.curr_method_sym.mtype.rettype, VoidType)

    def enforce_access(self, value: Expr):
        if isinstance(value, Id):
            raise Undeclared(Identifier(), value.name)
        elif isinstance(value, ArrayCell):
            self.enforce_access(value.arr)
        elif isinstance(value, UnaryOp):
            self.enforce_access(value.body)
        elif isinstance(value, BinaryOp):
            self.enforce_access(value.left)
            self.enforce_access(value.right)

    """
            VISITORS
    """

    def visitProgram(self, ast: Program, c):
        # Check for Undeclared/Redeclared first
        env = {}
        ret = []
        for decl in ast.decl:
            ret.append(self.visit(decl, env))
            # Check for entry
            if decl.classname.name == "Program" and not any(
                isinstance(mem, MethodDecl)
                    and mem.name.name == "main"
                    and len(mem.param) == 0
                for mem in decl.memlist
            ):
                raise NoEntryPoint()
        if not any(decl.classname.name == "Program" for decl in ast.decl):
            raise NoEntryPoint()

        return ret


    def visitClassDecl(self, ast: ClassDecl, c):
        cname = ast.classname.name
        parent_cname = ast.parentname.name if ast.parentname else None

        if cname in c:
            raise Redeclared(Class(), cname)
        if parent_cname and not parent_cname in c:
            raise Undeclared(Class(), parent_cname)

        c[cname] = [
            # Default constructor
            Symbol("Constructor", MType([], VoidType()))
        ]
        self.curr_class_name = cname
        self.has_explicit_constructor = False
        for mem in ast.memlist:
            self.visit(mem, c)
            self.curr_method_sym = None
            self.is_declaring_static = False

    # TODO: Default destructor
    def visitMethodDecl(self, ast: MethodDecl, classes):
        cname = self.curr_class_name
        method_name = ast.name.name
        if self.lookup_method(method_name, cname, classes):
            if method_name == 'Constructor':
                if self.has_explicit_constructor:
                    raise Redeclared(Method(), method_name)
            elif method_name == 'Destructor':
                raise Redeclared(Method(), method_name)
            else:
                raise Redeclared(Method(), method_name)

        stack = [[Symbol(p.variable.name, p.varType) for p in ast.param]] + [classes]
        # Check for redeclared parameter
        parname = set()
        for par in stack[0]:
            self.check_undeclared_class(par.mtype, stack)
            if par.name in parname:
                raise Redeclared(Parameter(), par.name)
            parname.add(par.name)

        if method_name == 'Constructor':
            classes[cname] = list(filter(lambda sym: sym.name != method_name, classes[cname]))
            self.has_explicit_constructor = True

        classes[cname].append(
            Symbol(method_name, MType([p.varType for p in ast.param], VoidType()))
        )
        self.curr_method_sym = classes[cname][-1]
        self.is_declaring_static = '$' in method_name
        self.has_explicit_return = False
        self.visit(ast.body, stack)


    def visitAttributeDecl(self, ast: AttributeDecl, classes):
        cname = self.curr_class_name
        decl = ast.decl
        is_const = isinstance(decl, ConstDecl)
        attr_name = decl.constant.name if is_const else decl.variable.name
        typ = decl.constType if is_const else decl.varType
        self.is_declaring_static = '$' in attr_name

        if self.lookup_attribute(attr_name, cname, classes):
            raise Redeclared(Attribute(), attr_name)
        self.check_undeclared_class(typ, classes)

        if is_const:
            if not self.is_const(decl.value, classes):
                raise IllegalConstantExpression(decl.value)
            self.enforce_access(decl.value)
            if not self.can_coerce(decl.constType, self.visit(decl.value, classes)):
                raise TypeMismatchInConstant(ast)
        else:
            if decl.varInit and not self.can_coerce(decl.varType, self.visit(decl.varInit, classes)):
                raise TypeMismatchInStatement(ast)
            self.enforce_access(decl.varInit)

        classes[cname].append(Symbol(attr_name, typ, is_const))


    def visitVarDecl(self, ast: VarDecl, stack):
        varname = ast.variable.name
        if self.lookup(varname, stack[0], lambda sym: sym.name):
            raise Redeclared(Variable(), varname)
        self.check_undeclared_class(ast.varType, stack)
        if ast.varInit and not self.can_coerce(ast.varType, self.visit(ast.varInit, stack)):
            raise TypeMismatchInStatement(ast)
        stack[0].append(Symbol(varname, ast.varType))


    def visitConstDecl(self, ast: ConstDecl, stack):
        constname = ast.constant.name
        if self.lookup(constname, stack[0], lambda sym: sym.name):
            raise Redeclared(Constant(), constname)
        self.check_undeclared_class(ast.constType, stack)
        if not self.is_const(ast.value, stack):
            raise IllegalConstantExpression(ast.value)
        if not self.can_coerce(ast.constType, self.visit(ast.value, stack)):
            raise TypeMismatchInConstant(ast)
        stack[0].append(Symbol(constname, ast.constType, True))


    def visitAssign(self, ast: Assign, stack):
        tr = self.visit(ast.exp, stack)
        tl = self.visit(ast.lhs, stack)

        if self.is_const(ast.lhs, stack):
            raise CannotAssignToConstant(ast)

        if type(tl) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif not self.can_coerce(tl, tr):
            raise TypeMismatchInStatement(ast)


    def visitBlock(self, ast: Block, stack):
        for stmt in ast.inst:
            self.visit(stmt, stack)


    def visitIf(self, ast: If, c):
        typ = self.visit(ast.expr, c)
        if not isinstance(typ, BoolType):
            raise TypeMismatchInStatement(ast)
        env = [[]] + c
        self.visit(ast.thenStmt, env)
        if ast.elseStmt:
            self.visit(ast.elseStmt, env)


    def visitFor(self, ast: For, stack):
        t1 = self.visit(ast.expr1, stack)
        t2 = self.visit(ast.expr2, stack)
        t3 = self.visit(ast.expr3, stack)
        tid = self.visit(ast.id, stack)

        if any(map(lambda t: type(t) != IntType, [t1, t2, t3, tid])):
            raise TypeMismatchInStatement(ast)

        # Cannot assign to constant
        self.visit(Assign(ast.id, ast.expr1), stack)

        self.is_in_loop = True
        env = [[]] + stack
        self.visit(ast.loop, env)
        self.is_in_loop = False


    def visitBreak(self, ast: Break, stack):
        # somehow stack must know that there is a loop being called
        if not self.is_in_loop:
            raise MustInLoop(ast)


    def visitContinue(self, ast: Continue, stack):
        if not self.is_in_loop:
            raise MustInLoop(ast)

    
    def visitReturn(self, ast: Return, stack):
        explicit_ret_type = self.visit(ast.expr, stack) if ast.expr else VoidType()
        explicit_ret_is_const = self.is_const(ast.expr, stack)
        cur_ret_type = self.curr_method_sym.mtype.rettype
        cur_ret_is_const = self.curr_method_sym.is_const

        if self.has_explicit_return:
            if not self.can_coerce(cur_ret_type, explicit_ret_type) or \
            explicit_ret_is_const != cur_ret_is_const:
                raise TypeMismatchInStatement(ast)
        else:
            self.has_explicit_return = True

        if type(explicit_ret_type) != VoidType and \
        (self.is_in_main() or self.curr_method_sym.name in ['Constructor', 'Destructor']):
            raise TypeMismatchInStatement(ast)

        self.curr_method_sym.mtype.rettype = explicit_ret_type
        self.curr_method_sym.is_const = explicit_ret_is_const

        return explicit_ret_type


    def visitCallStmt(self, ast: CallStmt, stack):
        return self.check_method_call(ast, stack)


    def visitCallExpr(self, ast: CallExpr, stack):
        return self.check_method_call(ast, stack)


    def visitFieldAccess(self, ast: FieldAccess, stack):
        return self.check_obj_and_mem_name(ast, stack).mtype


    def visitId(self, ast: Id, stack):
        if isinstance(stack, list):
            # Currently in a scope / method
            res = self.lookup_in_local_scopes(ast.name, stack)
            if res:
                return res.mtype
            # Check if Id is a ClassName
            if ast.name in stack[-1]:
                return NSType(ast.name)
            raise Undeclared(Identifier(), ast.name)
        else:
            # Currently in class body
            if ast.name in stack:
                return NSType(ast.name)
            # This id is in the attribute decl
            attr_sym = self.lookup_attribute(ast.name, self.curr_class_name, stack)
            if attr_sym:
                return attr_sym.mtype
            else:
                raise Undeclared(Attribute(), ast.name)


    def visitBinaryOp(self, ast: BinaryOp, c):
        # typeleft, constleft
        tl = self.visit(ast.left, c)
        tr = self.visit(ast.right, c)
        if isinstance(tl, NSType): raise Undeclared(Identifier(), tl.cname)
        if isinstance(tr, NSType): raise Undeclared(Identifier(), tr.cname)

        op = ast.op
        if op in ["+", "-", "*", "/", ">", ">=", "<", "<="]:
            not_allowed = (BoolType, ArrayType, StringType, VoidType, ClassType)
            if isinstance(tl, not_allowed) or isinstance(tr, not_allowed):
                raise TypeMismatchInExpression(ast)
            if op in [">", ">=", "<", "<="]:
                return BoolType()
            if isinstance(tl, FloatType) or isinstance(tr, FloatType):
                return FloatType()
            else:
                return IntType()
        else:
            if op == "%":
                if type(tl) != IntType or type(tr) != IntType:
                    raise TypeMismatchInExpression(ast)
            elif op in ["&&", "||"]:
                if type(tl) != BoolType or type(tr) != BoolType:
                    raise TypeMismatchInExpression(ast)
            elif op in ["==."]:
                if type(tl) != StringType or type(tr) != StringType:
                    raise TypeMismatchInExpression(ast)
                return BoolType()
            elif op in ["+."]:
                if type(tl) != StringType or type(tr) != StringType:
                    raise TypeMismatchInExpression(ast)
            elif op in ["==", "!="]:
                if type(tl) != type(tr):
                    raise TypeMismatchInExpression(ast)
                if not isinstance(tl, (IntType, BoolType)):
                    raise TypeMismatchInExpression(ast)
                return BoolType()

            return tl


    def visitUnaryOp(self, ast: UnaryOp, c):
        te = self.visit(ast.body, c)
        if isinstance(te, NSType): raise Undeclared(Identifier(), te.cname)

        if ast.op == "-" and type(te) != IntType:
            raise TypeMismatchInExpression(ast)
        elif ast.op == "!" and type(te) != BoolType:
            raise TypeMismatchInExpression(ast)
        return te


    def visitNewExpr(self, ast: NewExpr, stack):
        class_name = ast.classname.name
        self.check_undeclared_class(ClassType(ast.classname), stack)
        constructor = self.lookup_method('Constructor', class_name, stack)
        self.check_args_match_params(ast, constructor, stack)
        return ClassType(ast.classname)

    # TODO: If cell is mutable then return mutable
    # TODO: Index must be literal/immutable
    def visitArrayCell(self, ast: ArrayCell, stack):
        # Get type of expr
        typ = self.visit(ast.arr, stack)
        if type(typ) != ArrayType:
            raise TypeMismatchInExpression(ast)
        if any(map(lambda idx: type(self.visit(idx, stack)) != IntType, ast.idx)):
            raise TypeMismatchInExpression(ast)
        for _ in ast.idx:
            if isinstance(typ, ArrayType):
                typ = typ.eleType
            else:
                raise TypeMismatchInExpression(ast)
        return typ


    def visitIntLiteral(self, ast: IntLiteral, c):
        return IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()


    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()


    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return BoolType()


    def visitArrayLiteral(self, ast: ArrayLiteral, stack):
        ele_type = self.visit(ast.value[0], stack) if len(ast.value) else VoidType()
        try:
            if ENABLE_ARRAYLIT_COERCE and \
            any(type(self.visit(ele, stack)) == FloatType for ele in ast.value) and \
            all(type(self.visit(ele, stack)) in (IntType, FloatType) for ele in ast.value):
                ele_type = FloatType()
            elif any(type(ele_type) != type(self.visit(ele, stack)) for ele in ast.value):
                raise IllegalArrayLiteral(ast)
        except:
            raise IllegalArrayLiteral(ast)

        size = len(ast.value)
        return ArrayType(size, ele_type)


    def visitNullLiteral(self, ast: NullLiteral, c):
        return VoidType()


    def visitSelfLiteral(self, ast: SelfLiteral, stack):
        classname = self.curr_class_name
        return ClassType(Id(classname))
