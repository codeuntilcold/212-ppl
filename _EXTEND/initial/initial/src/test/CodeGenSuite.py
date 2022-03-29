import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

    def test_ast(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],VoidType(),Block([
                    CallStmt(Id("io"), Id("putInt"),[
                        BinaryOp("+", 
                            IntLiteral(20),
                            IntLiteral(30)
                        )
                    ])
                ]))
            ])
        ])
        expect = "50"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_ast_add_int(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],VoidType(),Block([
                    CallStmt(Id("io"), Id("putInt"),[
                        BinaryOp("+", 
                            IntLiteral(20),
                            BinaryOp("+", 
                                IntLiteral(30),
                                IntLiteral(50)
                            )  
                        )
                    ])
                ]))
            ])
        ])
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_ast_add_float(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],VoidType(),Block([
                    CallStmt(Id("io"), Id("putFloat"),[
                        BinaryOp("+",
                            IntLiteral(10),    
                            BinaryOp("+", 
                                FloatLiteral(20.5),
                                FloatLiteral(29.5)
                            )
                        )
                    ])
                ]))
            ])
        ])
        expect = "60.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_code(self):
        input = """class Program {
            void main() {
                io.putInt(20);
            }
        }"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_code_add_int(self):
        input = """class Program {
            void main() {
                io.putInt(15 + 20);
            }
        }"""
        expect = "35"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_code_add_float(self):
        input = """class Program {
            void main() {
                io.putFloat(20.5 + 79.5);
            }
        }"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,504))
