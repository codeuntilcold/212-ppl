"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, is_const = False):
        self.name = name
        self.mtype = mtype
        self.is_const = is_const


class StaticChecker(BaseVisitor,Utils):

    libname = "io"
    global_envi = [
        Symbol("$getInt", MType([], IntType())),
        Symbol("$putIntLn", MType([IntType()], VoidType())),
        Symbol("$putFloatLn", MType([FloatType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast
 
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)


    """
            HELPERS
    """
    def check_undeclared_class(self, classtype, stack):
        if isinstance(classtype, ClassType) and not classtype.classname.name in stack[-1]:
            raise Undeclared(Class(), classtype.classname.name)
        return classtype

    def log(self, msg):
        print('='*60)
        print(str(msg))
        print('='*60)

    def lookup_in_local_scopes(self, name, stack) -> (None or Symbol):
        for scope in stack[:-1]:
            sym = self.lookup(name, scope, lambda sym: sym.name)
            if sym: return sym
        return None

    def lookup_in_class_scope(self, name, classname, stack) -> (None or Symbol):
        if classname in stack[-1]:
            sym = self.lookup(name, stack[-1][classname], lambda sym: sym.name)
            if sym: return sym
        else:
            raise Undeclared(Class(), classname)
        return None

    def check_args_match_params(self, ast, method_sym, stack, err):
        # Check param len
        if len(ast.param) != len(method_sym.mtype.partype):
            raise err(ast)
        # Check param type
        partype = [type(par) for par in method_sym.mtype.partype]
        for (arg, ptype) in list(zip(ast.param, partype)):
            vartype = type(self.visit(arg, stack))
            if ptype == FloatType:
                if vartype == IntType:
                    # TODO: type coersion
                    pass
            elif vartype != ptype:
                raise TypeMismatchInExpression(arg)
    
    def check_illegal_mem_access(self, expr: (FieldAccess or CallExpr), stack):
        if type(expr) == FieldAccess:
            mem_name = expr.fieldname.name
            is_static = "$" in mem_name
            accessor = self.visit(expr.obj, stack)
            # If accessor is Class and accessing an instance attribute, then throw
            if type(expr.obj) == Id and type(accessor) == ClassType and not is_static:
                raise IllegalMemberAccess(expr)
            # if accessor is a class instance and accessing a static attribute, then throw
            if type(expr.obj) == FieldAccess and type(accessor) == ClassType and is_static:
                raise IllegalMemberAccess(expr)
        else:
            mem_name = expr.method
            is_static = "$" in mem_name
            accessor = self.visit(expr.obj, stack)
            # If accessor is Class and accessing an instance attribute, then throw
            if type(expr.obj) == Id and type(accessor) == ClassType and not is_static:
                raise IllegalMemberAccess(expr)
            # if accessor is a class instance and accessing a static attribute, then throw
            if type(expr.obj) == CallExpr and type(accessor) == ClassType and is_static:
                raise IllegalMemberAccess(expr)

    """
            VISITORS
    """
    def visitProgram(self, ast: Program, c):
        # Check for Undeclared/Redeclared first
        env = { StaticChecker.libname: StaticChecker.global_envi }
        ret = [self.visit(decl, env) for decl in ast.decl]

        # Check for entry
        program_class = self.lookup("Program", ast.decl, lambda decl: decl.classname.name)
        if program_class is None or not any(
            isinstance(mem, MethodDecl) 
                and mem.name.name == "main" 
                and len(mem.param) == 0
            for mem in program_class.memlist
        ):
            raise NoEntryPoint()
        
        return ret 


    def visitClassDecl(self, ast: ClassDecl, c):
        cname = ast.classname.name
        parent_cname = ast.parentname.name if ast.parentname else None

        if cname in c:
            raise Redeclared(Class(), cname)
        c[cname] = []
        
        if parent_cname:
            if not parent_cname in c:
                raise Undeclared(Class(), parent_cname)
            else:
                # TODO: Support polymorphism
                pass

        # Holds an array of Symbols
        # Pass the global class env and also name of current class for members
        [self.visit(mem, (c, cname)) for mem in ast.memlist]


    def visitAttributeDecl(self, ast: AttributeDecl, classes):
        cname = classes[1]
        decl = ast.decl
        is_const = isinstance(decl, ConstDecl)
        attr_name = decl.constant.name if is_const else decl.variable.name
        if self.lookup(attr_name, classes[0][cname], lambda sym: sym.name):
            raise Redeclared(Attribute(), attr_name)

        typ = decl.constType if is_const else decl.varType
        self.check_undeclared_class(typ, classes[0])

        if is_const:
            if decl.value is None:
                raise IllegalConstantExpression(None)
            if type(decl.constType) != type(self.visit(decl.value, classes[0])):
                raise TypeMismatchInConstant(ast)
                # raise TypeMismatchInStatement(ast)
        else:
            if decl.varInit and type(decl.varType) != type(self.visit(decl.varInit, classes[0])):
                raise TypeMismatchInStatement(ast)

        classes[0][cname].append(Symbol(attr_name, typ, is_const))
    

    def visitMethodDecl(self, ast: MethodDecl, classes):
        cname = classes[1]
        method_name = ast.name.name
        if self.lookup(method_name, classes[0][cname], lambda sym: sym.name):
            raise Redeclared(SpecialMethod(), method_name) if method_name in ['Constructor', 'Destructor'] else \
                Redeclared(Method(), method_name)
        
        stack = [[Symbol(p.variable.name, p.varType) for p in ast.param]] + [classes[0]]
        for i in range(len(stack[0]) - 1):
            cur = stack[0][i]
            rest = stack[0][i+1:]
            self.check_undeclared_class(cur.mtype, stack) 
            if self.lookup(cur.name, rest, lambda sym: sym.name):
                raise Redeclared(Parameter(), cur.name)
            
        partype = [p.varType for p in ast.param]
        retlist = list(filter(lambda inst: isinstance(inst, Return), ast.body.inst))
        rettype = VoidType() if len(retlist) == 0 else self.visit(retlist[0], stack)
        for retstmt in retlist:
            if type(self.visit(retstmt, stack)) != type(rettype):
                raise TypeMismatchInStatement(retstmt)

        self.visit(ast.body, stack)

        classes[0][cname].append(Symbol(method_name, MType(partype, rettype)))


    def visitBlock(self, ast: Block, stack):
        for stmt in ast.inst:    
            self.visit(stmt, stack)


    def visitVarDecl(self, ast: VarDecl, stack):
        varname = ast.variable.name
        if self.lookup(varname, stack[0], lambda sym: sym.name):
            raise Redeclared(Variable(), varname)
        self.check_undeclared_class(ast.varType, stack)

        if ast.varInit and type(ast.varType) != type(self.visit(ast.varInit, stack)):
            raise TypeMismatchInStatement(ast)

        stack[0].append(Symbol(varname, ast.varType))


    def visitConstDecl(self, ast: ConstDecl, stack):
        constname = ast.constant.name
        if self.lookup(constname, stack[0], lambda sym: sym.name):
            raise Redeclared(Constant(), constname)
        self.check_undeclared_class(ast.constType, stack)

        if ast.value:
            if type(ast.constType) != type(self.visit(ast.value, stack)):
                raise TypeMismatchInConstant(ast)
            
            # TODO: Check static evaluation
            def cannot_be_evaluated_statically(expr):
                if isinstance(expr, Literal):
                    return False
                else:
                    return False
            
            if cannot_be_evaluated_statically(ast.value):
                raise IllegalConstantExpression(ast.value)
        else:
            raise IllegalConstantExpression(ast.value)

        stack[0].append(Symbol(constname, ast.constType, True))


    def visitAssign(self, ast: Assign, stack):
        tr = self.visit(ast.exp, stack)
        tl = self.visit(ast.lhs, stack)
        
        is_const = False
        if isinstance(ast.lhs, Id):
            var_sym = self.lookup_in_local_scopes(ast.lhs.name, stack)
            if var_sym:
                is_const = var_sym.is_const
            else:
                Undeclared(Identifier(), ast.lhs.name)
        elif isinstance(ast.lhs, FieldAccess):
            ctype = self.visit(ast.lhs.obj, stack)
            dot_sym = self.lookup_in_class_scope(ast.lhs.fieldname.name, ctype.classname.name, stack)
            if dot_sym:
                is_const = dot_sym.is_const
            else:
                raise Undeclared(Attribute(), ast.lhs.fieldname.name)
        elif isinstance(ast.lhs, ArrayCell):
            arr = ast.lhs.arr
            if isinstance(arr, Id):
                var_sym = self.lookup_in_local_scopes(arr.name, stack)
                if var_sym:
                    is_const = var_sym.is_const
                else:
                    raise Undeclared(Identifier(), arr.name)
            elif isinstance(arr, FieldAccess):
                caller_type = self.visit(arr.obj, stack)
                if isinstance(caller_type, ClassType):
                    class_name = caller_type.classname.name
                    arrsym = self.lookup_in_class_scope(arr.fieldname, class_name, stack)
                    if arrsym:
                        is_const = arrsym.is_const
                    else:
                        raise Undeclared(Attribute(), arr.fieldname)
                else:
                    raise TypeMismatchInExpression(ast.lhs)
        if is_const:
            raise CannotAssignToConstant(ast)
        if type(tl) == VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(tl) == FloatType:
            if not isinstance(tr, (IntType, FloatType)):
                raise TypeMismatchInStatement(ast)
        elif type(tl) != type(tr):
            raise TypeMismatchInStatement(ast)


    def visitCallStmt(self, ast: CallStmt, stack):
        method_name = ast.method.name
        if isinstance(ast.obj, Id):
            class_name = ast.obj.name
            # If classname is shadowed by localvar
            sym = self.lookup_in_local_scopes(class_name, stack)
            if sym and type(sym.mtype) != ClassType:
                raise TypeMismatchInStatement(ast)
            
            method_sym = self.lookup_in_class_scope(method_name, ast.obj.name, stack)
            if not method_sym:
                raise Undeclared(Method(), method_name)
            self.check_args_match_params(ast, method_sym, stack, TypeMismatchInStatement)
            
            # Return
            if not isinstance(method_sym.mtype.rettype, VoidType):
                raise TypeMismatchInStatement(ast)
            return method_sym.mtype.rettype
        elif isinstance(ast.obj, SelfLiteral):
            # TODO
            pass 
        else:
            self.visit(ast.obj, stack)



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

        stack[0].append(Symbol("<For>", VoidType()))
        env = [[]] + stack
        self.visit(ast.loop, env)
        stack[0] = list(filter(lambda sym: sym.name != "<For>", stack[0]))


    def visitBreak(self, ast: Break, stack):
        # somehow stack must know that there is a loop being called
        for scope in stack[:-1]:
            if self.lookup("<For>", scope, lambda sym: sym.name):
                return
        raise MustInLoop(ast)


    def visitContinue(self, ast: Continue, stack):
        for scope in stack[:-1]:
            if self.lookup("<For>", scope, lambda sym: sym.name):
                return
        raise MustInLoop(ast)


    def visitReturn(self, ast: Return, c):
        return self.visit(ast.expr, c) if ast.expr else VoidType()

    
    def visitCallExpr(self, ast: CallExpr, stack): 
        method_name = ast.method.name
        is_static = '$' in method_name
        if isinstance(ast.obj, Id):
            class_name = ast.obj.name
            # If classname is shadowed by localvar
            sym = self.lookup_in_local_scopes(class_name, stack)
            if sym:
                if isinstance(sym.mtype, ClassType):
                    class_name = sym.mtype.classname.name
                else:
                    raise TypeMismatchInExpression(ast)

            method_sym = self.lookup_in_class_scope(method_name, class_name, stack)
            if not method_sym:
                raise Undeclared(Method(), method_name)
            
            if sym:
                if is_static:
                    raise IllegalMemberAccess(ast)
            else:
                if not is_static:
                    raise IllegalMemberAccess(ast)


            self.check_args_match_params(ast, method_sym, stack, TypeMismatchInExpression)              
            # Return
            if isinstance(method_sym.mtype.rettype, VoidType):
                raise TypeMismatchInExpression(ast)
            return method_sym.mtype.rettype
        elif isinstance(ast.obj, SelfLiteral):
            # TODO
            pass
        else:
            ret = self.visit(ast.obj, stack)
            if not isinstance(ret, ClassType):
                raise TypeMismatchInExpression(ast)
            
            classname = ret.classname.name
            method_sym = self.lookup_in_class_scope(method_name, classname, stack)
            if not method_sym:
                raise Undeclared(Method(), method_name)
            self.check_args_match_params(ast, method_sym, stack, TypeMismatchInExpression)
            # Return
            if isinstance(method_sym.mtype.rettype, VoidType):
                raise TypeMismatchInExpression(ast)
            return method_sym.mtype.rettype


    def visitId(self, ast: Id, stack):
        res = self.lookup_in_local_scopes(ast.name, stack)
        if res: 
            return res.mtype
        else:
            # Check if Id is a ClassName
            if ast.name in stack[-1]:
                return ClassType(Id(ast.name))
            raise Undeclared(Identifier(), ast.name)


    def visitBinaryOp(self, ast: BinaryOp, c):
        # typeleft, constleft
        tl = self.visit(ast.left, c)
        tr = self.visit(ast.right, c)
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
                if type(tl) == ArrayType:
                    if tl.size != tr.size:
                        raise TypeMismatchInExpression(ast)
                    if isinstance(tl.eleType, (IntType, FloatType)) and isinstance(tr.eleType, (IntType, FloatType)):
                        # This pass allows type coersion
                        pass
                    elif type(tl) != type(tr):
                        raise TypeMismatchInExpression(ast)
                if not isinstance(tl, (IntType, BoolType)):
                    raise TypeMismatchInExpression(ast)
                return BoolType()

            return tl


    def visitUnaryOp(self, ast: UnaryOp, c):
        te = self.visit(ast.body, c)
        if ast.op == "-" and type(te) != IntType:
            raise TypeMismatchInExpression(ast)
        elif ast.op == "!" and type(te) != BoolType:
            raise TypeMismatchInExpression(ast)
        return te
            

    def visitNewExpr(self, ast: NewExpr, c):
        class_name = ast.classname.name
        # TODO: Check param with constructor
        ast.param
        return ClassType(Id(class_name))


    def visitArrayCell(self, ast: ArrayCell, stack):
        # Get type of expr
        typ = self.visit(ast.arr, stack)
        if type(typ) != ArrayType:
            raise TypeMismatchInExpression(ast)
        if any(map(lambda idx: type(self.visit(idx, stack)) != IntType, ast.idx)):
            raise TypeMismatchInExpression(ast)
        return typ


    def visitFieldAccess(self, ast: FieldAccess, stack):
        rettype = VoidType()
        field = ast.fieldname.name
        is_static = '$' in field
        if isinstance(ast.obj, Id):
            class_name = ast.obj.name
            # If class_name is shadowed by a variable name
            sym = self.lookup_in_local_scopes(class_name, stack)
            if sym: 
                if not isinstance(sym.mtype, ClassType):
                    raise TypeMismatchInExpression(ast)
                else:
                    # This id has the same name as the class name
                    # and is an instance of a class
                    class_name = sym.mtype.classname.name

            attr_name = self.lookup_in_class_scope(field, class_name, stack)
            if not attr_name:
                raise Undeclared(Attribute(), field)
            else:
                rettype = attr_name.mtype
            # Instance cannot access Static and vice-versa
            if sym:
                if is_static:
                    raise IllegalMemberAccess(ast)
            else:
                if not is_static:
                    raise IllegalMemberAccess(ast)

        elif isinstance(ast.obj, SelfLiteral):
            pass 
        elif isinstance(ast.obj, FieldAccess):
            typ = self.visit(ast.obj, stack)
            class_name = ast.obj.fieldname
            attr_name = self.lookup_in_class_scope(field, class_name, stack)
            if not attr_name:
                raise Undeclared(Attribute(), field)
            else:
                rettype = attr_name.mtype
        
        return rettype


    def visitIntLiteral(self, ast: IntLiteral, c): 
        return IntType()


    def visitFloatLiteral(self, ast: FloatLiteral, c):
        return FloatType()


    def visitStringLiteral(self, ast: StringLiteral, c):
        return StringType()


    def visitBooleanLiteral(self, ast: BooleanLiteral, c):
        return BoolType()


    def visitArrayLiteral(self, ast: ArrayLiteral, stack):
        ele_type = self.visit(ast.value[0], stack)
        if any(ele_type != self.visit(ele, stack) for ele in ast.value):
            raise IllegalArrayLiteral(ast)

        array_dim = len(ast.value) * ele_type.size if isinstance(ele_type, ArrayType) else len(ast.value)
        while isinstance(ele_type, ArrayType):
            ele_type = ele_type.eleType

        return ArrayType(array_dim, ele_type)


    def visitNullLiteral(self, ast: NullLiteral, c):
        return VoidType()
