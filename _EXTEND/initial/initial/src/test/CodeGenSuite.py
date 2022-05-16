import unittest
# from TestUtils import TestCodeGen
from TestUtils import TestMIPSCodeGen as TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

    def test_500(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],Block([
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

    def test_501(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],Block([
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

    def test_502(self):
        input = Program([
            ClassDecl(Id("Program"), [
                MethodDecl(Static(), Id("main"),[],Block([
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

    def test_503(self):
        input = """Class Program {
            main() {
                io.putInt(20);
            }
        }"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_504(self):
        input = """Class Program {
            main() {
                io.putInt(15 + 20);
            }
        }"""
        expect = "35"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_505(self):
        input = """Class Program {
            main() {
                io.putFloat(20.5 + 79.5);
            }
        }"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_506(self):
        input = """Class Program {
            main() {
                io.putIntLn(50 - 35 - 5);
            }
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_507(self):
        input = """Class Program {
            main() {
                Var a: Int = 507;
                Var b: Int = 508;
                a = b;

                io.putInt(a);
            }
        }"""
        expect = "508"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_508(self):
        input = """Class Program {
            main() {
                Var x: Int;
                Var y: Int;
                x = 10;
                y = 2;
                io.putInt(x - (2 + y));
            }
        }"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_509(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    # def test_510(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,510))

    # def test_511(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,511))

    # def test_512(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,512))

    # def test_513(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,513))

    # def test_514(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,514))

    # def test_515(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,515))

    # def test_516(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,516))

    # def test_517(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,517))

    # def test_518(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,518))

    # def test_519(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,519))

    # def test_520(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,520))

    # def test_521(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,521))

    # def test_522(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,522))

    # def test_523(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,523))

    # def test_524(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,524))

    # def test_525(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,525))

    # def test_526(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,526))

    # def test_527(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,527))

    # def test_528(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,528))

    # def test_529(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,529))

    # def test_530(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,530))

    # def test_531(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,531))

    # def test_532(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,532))

    # def test_533(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,533))

    # def test_534(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,534))

    # def test_535(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,535))

    # def test_536(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,536))

    # def test_537(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,537))

    # def test_538(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,538))

    # def test_539(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,539))

    # def test_540(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,540))

    # def test_541(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,541))

    # def test_542(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,542))

    # def test_543(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,543))

    # def test_544(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,544))

    # def test_545(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,545))

    # def test_546(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,546))

    # def test_547(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,547))

    # def test_548(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,548))

    # def test_549(self):
    #     input =
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,549))