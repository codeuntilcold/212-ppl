import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """class Example1 {
            int factorial(int n) {
                if n == 0 
                then return 1; 
                else return n * this.factorial(n - 1);
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Example1"), [
                MethodDecl(Instance(), Id("factorial"), 
                    [VarDecl(Id("n"), IntType())], IntType(),
                    Block([
                        If(BinaryOp('==', Id("n"), IntLiteral(0)), 
                            Return(IntLiteral(1)),
                            Return(BinaryOp('*', 
                                Id("n"), 
                                CallExpr(SelfLiteral(), Id("factorial"), 
                                    [BinaryOp('-', Id("n"), IntLiteral(1))])))
                        )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        input = """class Program {
            void main() {
                io.putInt(20);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"), [
            MethodDecl(Instance(), Id("main"), [], VoidType(), Block([
                CallStmt(Id("io"), Id("putInt"), [IntLiteral(20)])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_3(self):
        input = """class B {}"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,302))
   