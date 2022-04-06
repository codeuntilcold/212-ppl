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
    