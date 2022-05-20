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
                io.putFloat(1.5 + 3.5);
            }
        }"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_506(self):
        input = """Class Program {
            main() {
                io.putIntLn(50 - 35 - 5);
            }
        }
        """
        expect = "10\n"
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
                io.putInt(x + x - y + x);
            }
        }"""
        expect = "628"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_509(self):
        input = """Class Program {
            main() {
                Var a: Float = 10.0;
                io.putFloat(50 - a - 10);
            }
        }
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_510(self):
        input = """Class Program {
            main() {
                Var a: Int = 7;
                Var b: Float = 5.0;

                io.putIntLn(-5 * 7);
                io.putFloatLn(a * b);
                ip.putFloat(a / b);
            }
        }"""
        expect = "-35\n35.0\n1.4"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_511(self):
        input = """Class Program {
            no_param_four() { 
                io.putIntLn(26);
                Return 4; 
            }
            main() {
                Var x: Int = 10;
                io.putIntLn(x);
                x = Self.no_param_four();
                io.putInt(x);
            }
        }"""
        expect = "10\n26\n4"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_512(self):
        input = """Class Program {
            f(i: Int) {
                Var j: Int = 12;
                Return i + 4;
            }
            main() {
                Var x, y: Int = 10, 2;
                x = Self.f(x + y);
                io.putInt(x);
            }
        }
        """
        expect = "16"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_513(self):
        input = """
        Class Program {
            sumWithBias(a, b, c: Int) {
                Var bias: Int = -10;
                io.putIntLn(a);
                io.putIntLn(b);
                io.putIntLn(c);
                Return a + b + c + bias;
            }
            main() {
                Var x: Int = Self.sumWithBias(20, 30, 40) + 10;
                io.putInt(x);
            }
        }"""
        expect = "20\n30\n40\n90"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_514(self):
        input = """
        Class Program {
            times_f(a, b, c: Float) {
                io.putFloatLn(a);
                io.putFloatLn(b);
                io.putFloatLn(c);
                Return a * b * c;
            }
            main() {
                Var x, y: Float = 10.0, 2.0;
                x = Self.times_f(x, y, 1.0);
                io.putFloat(x);
            }
        }"""
        expect = "10.0\n2.0\n1.0\n20.0"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_515(self):
        input = """
        Class Program {
            main() {
                io.putIntLn(True);
                io.putIntLn(5 == 3);
                io.putInt(5 != 3);
            }
        }
        """
        expect = "1\n0\n1"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_516(self):
        input = """Class Program {
            returnWhat() {
                If (False) {
                    Return 3;
                }
                Elseif (4 != 4) {
                    Return 4;
                }
                Elseif (5 == 5) {
                    Return 5;
                }
                Else {
                    Return 6;
                }
            }
            main() {
                io.putInt(Self.returnWhat());
            }
        }"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_517(self):
        input = """Class Program {
            returnWhat() {
                Var default: Int = 127;
                If (False) {
                    Return 3;
                }
                Elseif (4 > 5) {
                    Return 4;
                }
                Elseif (5.0 < 4.9) {
                    Return 5;
                }
                Else {
                    Return default;
                }
                Return 6;
            }
            main() {
                io.putInt(Self.returnWhat());
            }
        }"""
        expect = "127"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_518(self):
        input = """
        Class Program {
            sumTo(i: Int) {
                If (i == 0) {
                    Return 0;
                }
                Else {
                    Return i + Self.sumTo(i - 1);
                }
            }
            main() {
                Var x: Int = Self.sumTo(10);
                io.putInt(x);
            }
        }"""
        expect = "55"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_519(self):
        input = """Class Program {
            main() {
                Var item: Int;
                Foreach(item In 0 .. 10 By 2) {
                    io.putInt(item);
                }
            }
        }"""
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_520(self):
        input = """
        Class Program {
            main() {
                Var item: Int;
                Foreach(item In 0 .. 10 By 2) {
                    Var next: Int = item + 1;
                    io.putInt(item);
                    io.putInt(next);
                }
            }
        }
        """
        expect = "01234567891011"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_521(self):
        input = """
        Class Program {
            main() {
                Var item: Int;
                Foreach(item In 10 .. 0 By 2) {
                    io.putInt(item);
                }
            }
        }"""
        expect = "1086420"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_522(self):
        input = """
        Class Program {
            print() {
                Var start, end: Int = 10, 15;
                Var item: Int;
                Foreach(item In start .. end) {
                    io.putInt(item);
                }
            }
            main() {
                Self.print();
            }
        }
        """
        expect = "101112131415"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_523(self):
        input = """
        Class Program {
            main() {
                Var x: Float = 5 * 3 + 7 * 1.5;
                io.putFloat(x);
            }
        }
        """
        expect = "25.5"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_524(self):
        input = """Class Program {
            main() {
                Var x: Boolean = 2 + 3 > 5;
                If (x) {
                    Var y: Int = 5 + 2;
                    io.putInt(y);
                }
                Else {
                    Var z: Int = 7 + 5;
                    io.putInt(z);
                }
            }
        }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_525(self):
        input = """Class Program {
            main() {
                Var a, b, c, d, e: Int = -3, -4, 2, 15, 7;
                Var max: Int = a;
                If (max < b) { max = b; }
                If (max < c) { max = c; }
                If (max < d) { max = d; }
                If (max < e) { max = e; }
                io.putInt(max);
            }
        }"""
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_526(self):
        input = """Class Program {
            main() {
                Var a, b, c, d, e: Int = -3, -4, 2, 15, 7;
                Var max: Int = a;
                If (max < b) { Var max: Int = b; }
                If (max < c) { Var max: Int = c; }
                If (max < d) { Var max: Int = d; }
                If (max < e) { Var max: Int = e; }
                io.putInt(max);
            }
        }"""
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_527(self):
        input = """Class Program {
            greater(a, b: Int) {
                If (a > b) { Return True; }
                Else { Return False; }
            }
            main() {
                Var a, b, c, d, e: Int = -3, -4, 2, 15, 7;
                Var max: Int = a;
                If (Self.greater(b, max)) { max = b; }
                If (Self.greater(c, max)) { max = c; }
                If (Self.greater(d, max)) { max = d; }
                If (Self.greater(e, max)) { max = e; }
                io.putInt(max);
            }
        }"""
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_528(self):
        input = """Class Program {
            main() {
                Var a: String = "You are amazing";
                io.putString(a);
            }
        }"""
        expect = "You are amazing"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_529(self):
        input = """Class Program {
            main() {
                Var a: String = "You are amazing";
                a = a +. ", put up the work!";
                io.putString(a);
            }
        }"""
        expect = "You are amazing, put up the work!"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_530(self):
        input = """Class Program {
            main() {
                Var x: Boolean = "You" ==. "You";
                If (x) {
                    Var y: Int = 5 + 2;
                    io.putInt(y);
                }
                Else {
                    Var z: Int = 7 + 5;
                    io.putInt(z);
                }
            }
        }"""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    # def test_531(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,531))

    # def test_532(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,532))

    # def test_533(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,533))

    # def test_534(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,534))

    # def test_535(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,535))

    # def test_536(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,536))

    # def test_537(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,537))

    # def test_538(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,538))

    # def test_539(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,539))

    # def test_540(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,540))

    # def test_541(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,541))

    # def test_542(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,542))

    # def test_543(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,543))

    # def test_544(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,544))

    # def test_545(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,545))

    # def test_546(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,546))

    # def test_547(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,547))

    # def test_548(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,548))

    # def test_549(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,549))