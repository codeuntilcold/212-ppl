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
        expect = "Type Mismatch In Statement: CallStmt(Id(io),Id(putIntLn),List())"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        input = """Class Program {
            main() {
                io.putIntLn(io.getInt(4));
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(getInt),List(IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_undeclared_function_use_ast(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"), [], Block([
                    CallExpr(Id("io"), Id("foo"), [])
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
        expect = "Type Mismatch In Statement: CallStmt(Id(io),Id(putIntLn),List())"
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
        expect = "Type Mismatch In Expression: CallExpr(Id(io),Id(getInt),List(IntLiteral(4)))"
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

    # def test_420(self):
    #     input = """Class Test {
    #         Var $attri: Int;
    #     }
    #     Class Program() {
    #         main() {
    #             Var a: Int = Test::$attri.really;
    #         }
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,420))

    # def test_421(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,421))

    # def test_422(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,422))

    # def test_423(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,423))

    # def test_424(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,424))

    # def test_425(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,425))

    # def test_426(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,426))

    # def test_427(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,427))

    # def test_428(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,428))

    # def test_429(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,429))

    # def test_430(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,430))

    # def test_431(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,431))

    # def test_432(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,432))

    # def test_433(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,433))

    # def test_434(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,434))

    # def test_435(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,435))

    # def test_436(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,436))

    # def test_437(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,437))

    # def test_438(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,438))

    # def test_439(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,439))

    # def test_440(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,440))

    # def test_441(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,441))

    # def test_442(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,442))

    # def test_443(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,443))

    # def test_444(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,444))

    # def test_445(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,445))

    # def test_446(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,446))

    # def test_447(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,447))

    # def test_448(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,448))

    # def test_449(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,449))

    # def test_450(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,450))

    # def test_451(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,451))

    # def test_452(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,452))

    # def test_453(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,453))

    # def test_454(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input,expect,454))

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