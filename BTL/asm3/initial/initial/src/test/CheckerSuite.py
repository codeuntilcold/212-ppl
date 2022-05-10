import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program {
            main() {
                io::$foo();
            }
        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_401(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program {
            main() {
                io::$putIntLn();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id($putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_402(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program {
            main() {
                io::$putIntLn(io::$getInt(4));
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id($getInt),[IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_403(self):
        input = Program([
            ClassDecl(Id("io"), [
                MethodDecl(Static(), Id("$getInt"), [], Block([
                    Return(IntLiteral(1))
                ])),
                MethodDecl(Static(), Id("$putIntLn"), [VarDecl(Id("a"), IntType())], Block([
                ])),
                MethodDecl(Static(), Id("$putFloatLn"), [VarDecl(Id("a"), FloatType())], Block([
                ])),
            ]),
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("$foo"), [])
                ]))
            ])
        ])
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        input = Program([
            ClassDecl(Id("io"), [
                MethodDecl(Static(), Id("$getInt"), [], Block([
                    Return(IntLiteral(1))
                ])),
                MethodDecl(Static(), Id("$putIntLn"), [VarDecl(Id("a"), IntType())], Block([
                ])),
                MethodDecl(Static(), Id("$putFloatLn"), [VarDecl(Id("a"), FloatType())], Block([
                ])),
            ]),
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("$putIntLn"), [])
                ]))
            ])
        ])
        expect = "Type Mismatch In Statement: Call(Id(io),Id($putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        input = Program([
            ClassDecl(Id("io"), [
                MethodDecl(Static(), Id("$getInt"), [], Block([
                    Return(IntLiteral(1))
                ])),
                MethodDecl(Static(), Id("$putIntLn"), [VarDecl(Id("a"), IntType())], Block([
                ])),
                MethodDecl(Static(), Id("$putFloatLn"), [VarDecl(Id("a"), FloatType())], Block([
                ])),
            ]),
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("$putIntLn"), [
                        CallExpr(Id("io"), Id("$getInt"), [IntLiteral(4)])
                    ])
                ]))
            ])
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id($getInt),[IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        input = "Class NoProgram {}"
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        input = """Class Program {
            Var main: Int;
            no_main() {}
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        input = """
            Class NotProgram {
                main() {}
                not_main() {}
            }
            Class Program {
                not_main() {}
                no_main() {}
                main(but_has_param: Int) {}
            }        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_409(self):
        input = """Class Program: B {}"""
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        input = """Class Program {} Class Program {}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = """Class Program {
            Var attr1: Int;
            Val attr1: Float;
        }"""
        expect = "Redeclared Attribute: attr1"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        input = """Class Program {
            main() {}
            main() {}
        }"""
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = """Class Program {
            Var main: Int;
            main() {}
            main() {}
        }"""
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = """Class Program {
            main(a: Int) {
                Var a: Int;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        input = """Class Program {
            main(a: Int) {
                Val a: Int;
            }
        }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_416(self):
        input = """Class Program {
            main(a: Int; a: Float) {
                Var a: Int;
            }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        input = """Class Program {
            main() {
                a = 5;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        input = """Class Program {
            main() {
                Var a: Rectangle;
            }
        }"""
        expect = "Undeclared Class: Rectangle"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program {
            main() {
                Var a: Int = io.nonexistent_attr.really;
            }
        }"""
        expect = "Illegal Member Access: FieldAccess(Id(io),Id(nonexistent_attr))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
        input = """Class Test {
            Var $attri: Float;
        }
        Class Program {
            main() {
                Var a: Int = Test::$attri;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FieldAccess(Id(Test),Id($attri)))"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        input = """Class Program {
            main() {
                Val a: Int = 5;
                Val b: Int = 0;
                a = b;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        input = """Class Program {
            Val $constant: Int = 10;

            main() {
                Program::$constant = 10;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Program),Id($constant)),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = """Class Program {
            main() {
                Val idx: Int = 5;
                Foreach(idx In 1 .. 10) {
                    ## Do something ##
                }
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(idx),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        input = """Class Program {
            main() {
                Val idx: Int = 1.2;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(idx),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_425(self):
        input = """Class Program {
            main() {
                Val idx: Boolean = 1;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(idx),BoolType,IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_426(self):
        input = """Class A {}
        Class B: A {}
        Class Program {
            main() {
                Val a: A = New A();
                Val b: A = New B();
                Val c: B = New B();
                Val d: B = New A();
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(b),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_427(self):
        input = """Class Program {
            main() {
                Val idx: Int = True;
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(idx),IntType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_428(self):
        input = """Class Program {
            main() {
                Break;
                Foreach(idx In 1 .. 10) {
                    Continue;
                }
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_429(self):
        input = """Class Program {
            main() {
                Continue;
                Foreach(idx In 1 .. 10) {
                    Break;
                }
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_430(self):
        input = """Class Program {
            main() {
                Var idx: Int;
                Foreach(idx In 1 .. 10) {
                    Var aidx: Int;
                    Foreach(aidx In 1 .. 10) {
                        Continue;
                    }
                }
                Break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_431(self):
        input = """Class Program {
            main() {
                If (True) {
                    Break;
                }
                Var idx: Int;
                Foreach(idx In 1 .. 10) {
                    Continue;
                }
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        input = """Class Program{
            main() {
                Var i: Float;
                Foreach(i In 1 .. 10) {
                    ## Do nothing ##
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_433(self):
        input = """Class Program{
            main() {
                Var i: Int;
                Foreach(i In 1 .. 10.2) {
                    ## Do nothing ##
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),FloatLit(10.2),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_434(self):
        input = """Class Program{
            main() {
                Var i: Float;
                Foreach(i In 1 + 1 .. 10 + 0.5) {
                    ## Do nothing ##
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(Id(i),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(10),FloatLit(0.5)),IntLit(1),Block([])])"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        input = """Class Program{
            main() {
                Var i: Float;
                Var j: Int;
                i = j;
                j = i;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(j),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        input = """Class Program{
            main() {
                Var i: Boolean;
                Var j: Int;
                i = j == j;
                i = j;
                j = i;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(i),Id(j))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        input = """Class Program{
            main() {
                Var i: Boolean;
                Var j: Int;
                Val k: Float = 2.1;
                i = j == j;
                i = j >= k;
                i = (j <= k) && (j < k) || (j > k);
                j = i;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(j),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        input = """Class Program{
            main() {
                Var i: Array[Int, 3] = Array(0,1,2);
                Var j: Array[Float, 3] = Array(0.0,1.1,1.2);
                j = i;
                Var b: Boolean;
                b = i;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program{
            main() {
                io::$putIntLn(5);
                io::$putFloatLn(5);
                io::$putIntLn(5.3);
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id($putIntLn),[FloatLit(5.3)])"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
        input = """Class Program{
            main() {
                Val a: Int = 0;
                a.toString();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(a),Id(toString),[])"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
        input = """Class Program {
            main() {}
            Constructor() {}
            Constructor() {}
        }"""
        expect = "Redeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        input = """Class Rect {
            $method() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Rect::$method();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(Rect),Id($method),[])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        input = """Class Rect {
            $method() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var a: Boolean;
                Var b: Int;
                Var c: Float;

                b = Rect::$method();
                c = Rect::$method();
                a = Rect::$method();
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),CallExpr(Id(Rect),Id($method),[]))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        input = """Class Program {
            main() {
                Var arr: Array[Int, 5] = Array(0,1,2,2,3);
                Var idx: Int = 0;
                Var b: Boolean = True;
                arr[idx] = arr[idx + 1];
                idx = arr[b];
            }
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        input = """Class Program {
            main() {
                Var a: Int = 0;
                Var b: Boolean = True;
                Var c: Float = 0.5;

                c = c + a;
                c = c + c;
                b = b || b;
                c = b + a;
            }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_446(self):
        input = """Class Program {
            main() {
                Var a: Int = 5;
                a = -a;
                a = a + a;
                a = !a;
            }
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        input = """Class Rect {
            Var $attri: Float;
            $method() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var a: Int = Rect::$method();
                a = Rect::$attri;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FieldAccess(Id(Rect),Id($attri)))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_448(self):
        input = """Class Rect {
            Var $attri: Float;
            $method() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var a: Int = Rect::$method();
                a = a::$attri;
            }
        }"""
        expect = "Undeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
        input = """Class Rect {
            Var $attri: Float;
            $method() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var a: Int = Rect::$method();
                a = a::$method();
            }
        }"""
        expect = "Undeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        input = """Class Program {
            main() {
                Val arr: Array[Int, 5] = Array(0,1,2,2,3);
                Var idx: Int = 0;
                Var b: Boolean = True;
                arr[idx] = arr[idx + 1];
                idx = arr[b];
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(arr),[Id(idx)]),ArrayCell(Id(arr),[BinaryOp(+,Id(idx),IntLit(1))]))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_451(self):
        input = """Class Rect {
            Var ins: Int;
            Var $sta: Int;
        }
        Class Program {
            main() {
                Var a: Int = Rect.ins;
            }
        }"""
        expect = "Illegal Member Access: FieldAccess(Id(Rect),Id(ins))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_452(self):
        input = """Class Rect {
            Var ins: Int;
            Var $sta: Int;
        }
        Class Program {
            main() {
                Var x: Rect = New Rect();
                Var a: Int = x::$sta;
            }
        }"""
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_453(self):
        input = """Class Rect {
            ins() {}
            $sta() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var x: Rect = New Rect();
                Var a: Int = x::$sta();
            }
        }"""
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_454(self):
        input = """Class Rect {
            ins() {
                Return 3;
            }
            $sta() {
                Return 1;
            }
        }
        Class Program {
            main() {
                Var a: Int = Rect.ins();
            }
        }"""
        expect = "Illegal Member Access: CallExpr(Id(Rect),Id(ins),[])"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_455(self):
        input = """Class Rect {
            Val $arr: Array[Int, 1] = Array(1);
        }
        Class Program {
            main() {
                Rect::$arr = Array(2);
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Rect),Id($arr)),[IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        input = """Class Rect {
            Val $arr: Array[Int, 1] = Array(1);
        }
        Class Program {
            main() {
                Var a: Array[Int, 1] = Rect::$arr;
                Var b: Array[Int, 2] = Rect::$arr;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,IntType),FieldAccess(Id(Rect),Id($arr)))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_457(self):
        input = """Class Rect {
            Val $arr: Array[Int, 1] = Array(1);
        }
        Class Program {
            main() {
                Var Rect: Int = 5;
                Var a: Int = Rect::$arr;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FieldAccess(Id(Rect),Id($arr)))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_458(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Rect {
            area() { Return 1; }
        }
        Class Program {
            main() {
                Var rect: Rect = New Rect();
                io::$putIntLn(rect.area());
                io::$putIntLn(Rect.area());
            }
        }"""
        expect = "Illegal Member Access: CallExpr(Id(Rect),Id(area),[])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_459(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Rect {
            area() { Return 1; }
        }
        Class Program {
            main() {
                Var rect: Rect = New Rect();
                io::$putIntLn(rect.area());
                io::$putIntLn(Rect::$area());
            }
        }"""
        expect = "Undeclared Method: $area"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_460(self):
        input = """Class Rect {
            area() { 
                Return 1;
                If (True) {
                    Return True;
                }
            }
        }
        Class Program {
            main() {
                Var rect: Rect = New Rect();
                io::$putIntLn(rect.area());
                io::$putIntLn(Rect::$area());
            }
        }"""
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_461(self):
        input = """Class Rect {
            area() {}
            $totalArea() {
                Self.area();
            }
        }
        Class Program {
            main() {}
        }"""
        expect = "Illegal Member Access: Call(Self(),Id(area),[])"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_462(self):
        input = """Class A {
            Var x: Int = 10;
        }
        Class Program {
            main() {
                Val a: A = New A();
                a.x = 10;
                b = 5;
            }
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_463(self):
        input = """Class Program {
            main() {
                Var a: Float = True;
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_464(self):
        input = """Class Program {
            Var a: Float = True;
            main() {
            }
        }"""
        expect = "Type Mismatch In Statement: AttributeDecl(Instance,VarDecl(Id(a),FloatType,BooleanLit(True)))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_465(self):
        input = """Class Program{
            Val $someStatic: Int = 10;
            main() {
                Var Program: Float = 1.0;
                Var x: Int = Program::$someStatic;
                Program::$someStatic = Program;
            }
        }"""
        expect = "Type Mismatch In Expression: FieldAccess(Id(Program),Id($someStatic))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_466(self):
        input = """Class Car {}
        Class Program{
            Var a : Int;
            main(){
                Var x : Int = 1 + Car;
            }
        }"""
        expect = "Undeclared Identifier: Car"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_467(self):
        input = """Class Car {
            Var tire: Int;
            Var npp: Int = Self.tire * 12 + tire;
        }
        Class Program{
            Var a : Int;
            main(){
                Var y : Int = 1 + Self.a;
            }
        }"""
        expect = "Undeclared Identifier: tire"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_468(self):
        input = """Class Program {
            main() {
                Return Null;
                Return 1;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_469(self):
        input = """Class Program {
            $methodReturn1() {
                Return 1;
            }
            $methodReturnNull() {

            }
            main() {
                Program::$methodReturnNull();
                Program::$methodReturn1();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(Program),Id($methodReturn1),[])"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_470(self):
        input = """Class Program {
            main() {
                Var a: Array[Int, 1] = Array();
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(1,IntType),[])"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_471(self):
        input = """Class Program {
            main() {
                Var a: Array[Float, 2] = Array(1.0, 1.2);
                Var b: Array[Int, 2] = Array(1, True);
            }
        }"""
        expect = "Illegal Array Literal: [IntLit(1),BooleanLit(True)]"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_472(self):
        input = """Class Program {
            main() {
                Var a: Array[Boolean, 3] = Array(True, True, False);
                Var b: Array[Array[Int, 1], 2] = Array(
                    Array(1),
                    Array(2),
                    Array(3)
                );
                Var c: Array[Array[String, 2], 3] = Array(
                    Array("This", "is"),
                    Array("dim", "mismatch")
                );
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(2)],[IntLit(3)]])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_473(self):
        input = """Class Program {
            $static(a: Float) {}
            main() {
                Program::$static(5);
                Program::$static(True);
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(Program),Id($static),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_474(self):
        input = """Class Program {
            $doesReturn() {
                If (True) { Return 1; }
                Else {
                    Val imm: Int = 3;
                    Return imm;
                }
            }
            main() {
                Program::$doesReturn();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(Program),Id($doesReturn),[])"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_475(self):
        input = """Class Program {
            main() {
                If (True) {
                    If (False) {
                        Return 1;
                    }
                }
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_476(self):
        input = """Class Car {}
        Class Program {
            main() {
                Var a: Car = New Car();
                Var b: Car = New Car(1, 2);
            }
        }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(Car),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_477(self):
        input = """Class Car {
            Var tire: Int;
            getTire() {
                Return Self.tire;
            }
        }
        Class Program {
            main() {
                Var a: Car;
                Var b: Int = a.getTire();
                Var c: Int = a.tire;
                d = c;
            }
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_478(self):
        input = """Class Car {
            Var tire: Int;
        }
        Class Program {
            main() {
                Var a: Car = New Car(4);
                Var b: Int = a.tire;
                Var c: Car = New Car();
            }
        }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(Car),[IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_479(self):
        input = """Class A {
            a() {}
            Var a: Int;
            Var b: Int;
            $a() {}
            a() {}
        }"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_480(self):
        input = """Class Rect {
            Var tire: Int;
            tire() { Return Self.tire; }
            $totalTires() {
                If (True) {
                    If (False) {
                        Return Self.tire;
                    }
                }
            }
        }"""
        expect = "Illegal Member Access: FieldAccess(Self(),Id(tire))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_481(self):
        input = """Class Rect{}
        Class Program {
            main() {
                Var a: Program = New Pop();
            }
        }"""
        expect = "Undeclared Class: Pop"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_482(self):
        input = """Class Program {
            main() {
                Var a: Array[Array[Int, 3], 2] = Array(
                    Array(1, 2, 3),
                    Array(1, 2, 3)
                );
                Var b: Array[Int, 3] = a[0];
                Var c: Array[Int, 2] = a[0];
            }
        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(c),ArrayType(2,IntType),ArrayCell(Id(a),[IntLit(0)]))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_483(self):
        input = """Class Program {
            main() {
                Var a: Array[Array[Array[String, 1], 1], 1] = Array(
                    Array(
                        Array("This is so weird")
                    )
                );
                Var b: Array[String, 1] = a[0][0];
                Var c: String = a[0][0][0];
                d.e = 10;
            }
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_484(self):
        input = """Class Program {
            main() {
                Var a: Array[Float, 2] = Array(5, 7);
                a = Array("Doctor", "Strange");
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(Doctor),StringLit(Strange)])"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_485(self):
        input = """Class Rect {
            area() {
                Return Null;
                If (True) {
                    If (False) {
                        Return Null;
                    }
                    Else {
                        Return 1;
                    }
                }
            }
        }"""
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_486(self):
        input = """Class Rect {
            Constructor() {
                Return False;
                Return Null;
            }
        }"""
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_487(self):
        input = """Class Program {
            Var a: Int;
            Var b: Int = 1 + Self.a;
            Var c: Int = 1 + a;
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_488(self):
        input = """Class Program {
            main() {
                If (True) {

                } Elseif (True) {

                } Elseif (True) {
                    Var b: Int;
                    If (b) {
                        Return True;
                    }
                } Else {

                }
            }
        }"""
        expect = "Type Mismatch In Statement: If(Id(b),Block([Return(BooleanLit(True))]))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_489(self):
        input = """
        Class Program {
            main() {
                Var myArray: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(5,6,7,8)
                    ),
                    Array(
                        Array(-1,-2,-3,-4),
                        Array(-5,-6,-7,False)
                    )
                );
            }
        }"""
        expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_490(self):
        input = """
        Class Rect {
            Var $totalRect: Int = 0;
            Var $totalArea: Float = 0;

            Var width, length: Float;

            area() {
                Return Self.width * Self.heig;
            }

            Constructor(w, l: Float) {
                Self.width = w;
                Self.length = l;
                Rect::$totalRect = Rect::$totalRect + 1;
                Rect::$totalArea = Rect::$totalArea + Self.area();
            }
        }
        Class Program {
            main() {

            }
        }"""
        expect = "Undeclared Attribute: heig"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_491(self):
        input = """
        Class IO {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Rect {
            Var $totalRect: Int = 0;
            Var $totalArea: Float = 0;

            Var width, length: Float;

            area() {
                Return Self.width * Self.length;
            }

            Constructor(w, l: Float) {
                Self.width = w;
                Self.length = l;
                Rect::$totalRect = Rect::$totalRect + 1;
                Rect::$totalArea = Rect::$totalArea + Self.area();
            }

            draw(x, y: Float) {}
        }
        Class Program {
            main() {
                Var shape: Rect = New Rect(3, 4);
                IO::$putFloatLn(shape.area());
                shape.length = shape.length / 3;
                IO::$putFloatLn(shape.area());
                IO::$putFloatLn(Rect::$totalArea);

                Val area: Float = shape.area();
            }
        }
        """
        expect = "Illegal Constant Expression: CallExpr(Id(shape),Id(area),[])"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_492(self):
        input = """Class Program {
            main() {
                Var a: Array[Float, 2] = Array(0, 1.1);
            }
        }"""
        expect = "Illegal Array Literal: [IntLit(0),FloatLit(1.1)]"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_493(self):
        input = """
        Class A {
            Var a: Int;  ## instance attribute of class A ##
        }
        Class Program {
            main(){
                Var obj: A = New A();  ## object of class A ##
                Var b: Int = obj.a;        ## access instance attribute of class A ##
                a = 5;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_494(self):
        input = """
        Class A {
            Var a: Int;  ## instance attribute of class A ##
        }
        Class B: A {
            foo(){
                Var x: Int = Self.a;   ## member of class A ##
            }
        }"""
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        input = """
        Class Program{
            foo(){
                Val x: Int = 1;
                Return x;
            }
            foo2(){
                Var x: Int = 1;
                Return x;
            }
            main(){
                Val y1: Int = Self.foo() + 1; ## OK since Self.foo() return Constant ##
                Val y2: Int = Self.foo2() + 1; ## Raise error because Self.foo2() return Variable ##
            }
        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,CallExpr(Self(),Id(foo),[]),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_496(self):
        input = """
        Class A {
            $foo(){}
        }
        Class Program {
            main(){
                Var y : A = New A();
                Var z : Int = 10;
                y::$foo(); ## 1 ##
                z::$foo(); ## 2 ##
            }
        }"""
        expect = "Undeclared Class: y"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_497(self):
        input = """Class A{
            Val y:Int=10;
        }
        Class B{
            Var x:A;
            func (){
                Val z:Int=Self.x.y;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_498(self):
        input = """Class Program {}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_499(self):
        input = """Class Program {}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,499))
