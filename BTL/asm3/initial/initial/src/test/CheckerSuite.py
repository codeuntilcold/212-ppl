import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """Class Program {
            main() {
                io.foo();
            }
        }"""
        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        input = """Class Program {
            main() {
                io.putIntLn();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        input = """Class Program {
            main() {
                io.putIntLn(io.getInt(4));
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(getInt),[IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("foo"), [])
                ]))
            ])
        ])
        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_diff_numofparam_expr_use_ast(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("putIntLn"), [])
                ]))
            ])
        ])
        expect = "Type Mismatch In Statement: Call(Id(io),Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_diff_numofparam_stmt_use_ast(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallStmt(Id("io"), Id("putIntLn"), [
                        CallExpr(Id("io"), Id("getInt"), [IntLiteral(4)])
                    ])
                ]))
            ])
        ])
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(getInt),[IntLit(4)])"
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
        expect = "Redeclared Class: Program"
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
        input = """Class Program {
            main() {
                Var a: Int = io.nonexistent_attr.really;
            }
        }"""
        expect = "Undeclared Attribute: nonexistent_attr"
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
                Val a: Int;
                Val b: Int = 0;
                a = b;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        input = """Class Program {
            Val $constant: Int;

            main() {
                Program::$constant = 10;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(Program),Id($constant)),IntLit(10))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = """Class Program {
            main() {
                Val idx: Int;
                Foreach(idx In 1 .. 10) {
                    ## Do something ##
                }
            }
        }"""
        expect = ""
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
        Class B {}
        Class Program {
            main() {
                Val a: A = New A();
                Val b: A = New B();
                Val c: B = New B();
                Val d: B = New A();
            }
        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),ClassType(Id(B)),NewExpr(Id(A),[]))"
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
                Val k: Float;
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
                Var j: Array[Float, 3] = Array(0,1.1,1.2);

                Var b: Boolean = i == j;
                b = i;
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = """Class Program{
            main() {
                io.putIntLn(5);
                io.putFloatLn(5);
                io.putIntLn(5.3);
            }
        }"""
        expect = "Type Mismatch In Expression: FloatLit(5.3)"
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
        expect = "Redeclared Special Method: Constructor"
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
        expect = "Type Mismatch In Expression: FieldAccess(Id(a),Id($attri))"
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
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id($method),[])"
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
        expect = "Illegal Member Access: Access(Id(Rect),Id(ins))"
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
        expect = "Illegal Member Access: Access(Id(Rect),Id(ins))"
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
        expect = "Illegal Member Access: CallExpr(Id(x),Id($sta),[])"
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

    # def test_455(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,455))

    # def test_456(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,456))

    # def test_457(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,457))

    # def test_458(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,458))

    # def test_459(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,459))

    # def test_460(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,460))

    # def test_461(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,461))

    # def test_462(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,462))

    # def test_463(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,463))

    # def test_464(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,464))

    # def test_465(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,465))

    # def test_466(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,466))

    # def test_467(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,467))

    # def test_468(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,468))

    # def test_469(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,469))

    # def test_470(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,470))

    # def test_471(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,471))

    # def test_472(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,472))

    # def test_473(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,473))

    # def test_474(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,474))

    # def test_475(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,475))

    # def test_476(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,476))

    # def test_477(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,477))

    # def test_478(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,478))

    # def test_479(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,479))

    # def test_480(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,480))

    # def test_481(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,481))

    # def test_482(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,482))

    # def test_483(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,483))

    # def test_484(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,484))

    # def test_485(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,485))

    # def test_486(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,486))

    # def test_487(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,487))

    # def test_488(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,488))

    # def test_489(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,489))

    # def test_490(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,490))

    # def test_491(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,491))

    # def test_492(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,492))

    # def test_493(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,493))

    # def test_494(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,494))

    # def test_495(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,495))

    # def test_496(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,496))

    # def test_497(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,497))

    # def test_498(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,498))

    # def test_499(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,499))