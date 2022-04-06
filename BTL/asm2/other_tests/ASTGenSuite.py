import unittest
from TestUtils import TestAST
from AST import *
#from main.d96.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test_01(self):
        """test class"""
        input = """Class Program {}"""
        expect = str(Program([ClassDecl(Id("Program"),[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_02(self):
        """test class"""
        input = """Class Program: test {}"""
        expect = str(Program([ClassDecl(Id("Program"),[],Id("test"))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_03(self):
        """test class"""
        input = """Class Program {}
        Class Test: Program {}
        """
        expect = str(Program([ClassDecl(Id("Program"),[]),
        ClassDecl(Id("Test"),[],Id("Program"))]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_04(self):
        """test class"""
        input = """Class Program {}
        Class Some: Program {}
        Class A {}
        """
        expect = str(Program([ClassDecl(Id("Program"),[]),
        ClassDecl(Id("Some"),[],Id("Program")),ClassDecl(Id("A"),[])]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_05(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var length: Int;
            Val num: Float;
        }"""
        expect = str(Program([ClassDecl(Id('Rectangle'),[AttributeDecl(Instance(),VarDecl(Id('length'),IntType())),
        AttributeDecl(Instance(),ConstDecl(Id("num"),FloatType()))])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_06(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Val a, $b: Float = 1.E2, 0.001e12;
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(1.E2))),
        AttributeDecl(Static(),ConstDecl(Id("$b"),FloatType(),FloatLiteral(0.001e12)))])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_07(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var a: String = "Something @@";
            Var $b: Int = 01234; 
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("Something @@"))),
        AttributeDecl(Static(),VarDecl(Id("$b"),IntType(),IntLiteral(668)))])]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_08(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var a, b, c: Boolean;
            Val d, e: Int = 0x123, 0XAF; 
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),BoolType())),
        AttributeDecl(Instance(),VarDecl(Id("b"),BoolType())),
        AttributeDecl(Instance(),VarDecl(Id("c"),BoolType())),
        AttributeDecl(Instance(),ConstDecl(Id("d"),IntType(), IntLiteral(291))),
        AttributeDecl(Instance(),ConstDecl(Id("e"),IntType(), IntLiteral(175)))])]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_09(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var a: Boolean;
            Var $b: Int = 0b11;
            Val c, $d: String = "abc \\t", "123";
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),BoolType())),
        AttributeDecl(Static(),VarDecl(Id("$b"),IntType(),IntLiteral(3))),
        AttributeDecl(Instance(),ConstDecl(Id("c"),StringType(),StringLiteral("abc \\t"))),
        AttributeDecl(Static(),ConstDecl(Id("$d"),StringType(),StringLiteral("123")))])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var a: Array[Int, 2];
            Var $b: Shape = New Shape();
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,IntType()))),
        AttributeDecl(Static(),VarDecl(Id("$b"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[])))])]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_11(self):
        """test attribute declare"""
        input = """Class Rectangle {
            Var a: Array[Array[Int, 3], 2] = Array(Array(1,2,3),Array(4,5,6));
            Var $b: Shape = Null;
            Val c: Int = a[0][1];
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,ArrayType(3,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])]))),
        AttributeDecl(Static(),VarDecl(Id("$b"),ClassType(Id("Shape")),NullLiteral())),
        AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),ArrayCell(Id("a"),[IntLiteral(0),IntLiteral(1)])))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12(self):
        """test attribute declare"""
        input = """Class Shape {
            Var a: Array[Boolean, 2] = Array(True, False);
            Var $b: String = "OK";
        }
        Class Rectangle: Shape {
            Val c: Shape = New Shape(a);
            Val $d: Float;
        }
        """
        expect = str(Program([ClassDecl(Id("Shape"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,BoolType()),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)]))),
        AttributeDecl(Static(),VarDecl(Id("$b"),StringType(),StringLiteral("OK")))]),
        ClassDecl(Id("Rectangle"),
        [AttributeDecl(Instance(),ConstDecl(Id("c"),ClassType(Id("Shape")),NewExpr(Id("Shape"),[Id("a")]))),
        AttributeDecl(Static(),ConstDecl(Id("$d"),FloatType()))],Id("Shape"))]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self):
        """test method declare"""
        input = """Class Student {
            getName(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("getName"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self):
        """test method declare"""
        input = """Class Student {
            Constructor(a: Int){}
            Destructor(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("a"),IntType())],Block([])),
        MethodDecl(Instance(),Id("Destructor"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15(self):
        """test method declare"""
        input = """Class Student {
            getName(){}
            setName(a,b: String){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("getName"),[],Block([])),
        MethodDecl(Instance(),Id("setName"),[VarDecl(Id("a"),StringType()),VarDecl(Id("b"),StringType())],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16(self):
        """test method declare"""
        input = """Class Program {
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Static(),Id("main"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_17(self):
        """test method declare"""
        input = """Class Student {
            main(){}
        }
        Class Program {
            main(a: Int){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("main"),[],Block([]))]),
        ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("main"),[VarDecl(Id("a"),IntType())],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_18(self):
        """test method declare"""
        input = """Class Student {
            getName(a: Array[Int, 10]; b: A){}
        }
        Class Program: Student {
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("getName"),[VarDecl(Id("a"),ArrayType(10,IntType())),VarDecl(Id("b"),ClassType(Id("A")))],Block([]))]),
        ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([]))],Id("Student"))]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_19(self):
        """test method declare"""
        input = """Class Student {
            $getName(a: Float){}
            A() {}
            method() {
                Var a: Int;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Static(),Id("$getName"),[VarDecl(Id("a"),FloatType())],Block([])),
        MethodDecl(Instance(),Id("A"),[],Block([])),
        MethodDecl(Instance(),Id("method"),[],Block([VarDecl(Id("a"),IntType())]))])]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20(self):
        """test method declare"""
        input = """Class Student: Person {
            get(a: Array[Boolean, 10]; b,c: A){}
        }
        Class Program {
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("get"),[VarDecl(Id("a"),ArrayType(10,BoolType())),VarDecl(Id("b"),ClassType(Id("A"))),VarDecl(Id("c"),ClassType(Id("A")))],Block([]))],Id("Person")),
        ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_21(self):
        """test mixed declare"""
        input = """Class Student {
            Var a: Int;
            getName(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
        MethodDecl(Instance(),Id("getName"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_22(self):
        """test mixed declare"""
        input = """Class Student {
            Val a: Float = 0.0e12;
            $get(){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [AttributeDecl(Instance(),ConstDecl(Id("a"),FloatType(),FloatLiteral(0.0e12))),
        MethodDecl(Static(),Id("$get"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23(self):
        """test mixed declare"""
        input = """Class Student {
            Var $a, b: Array[String, 2] = Array("BK", "HCM"), Array("abc", "cdf");
            Constructor(name: String){}
            Val c: Int = 0B101;
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [AttributeDecl(Static(),VarDecl(Id("$a"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral("BK"),StringLiteral("HCM")]))),
        AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(2,StringType()),ArrayLiteral([StringLiteral("abc"),StringLiteral("cdf")]))),
        MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("name"),StringType())],Block([])),
        AttributeDecl(Instance(),ConstDecl(Id("c"),IntType(),IntLiteral(5)))])]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_24(self):
        """test mixed declare"""
        input = """Class Student: Person {
            Var a: Array[Boolean, 2] = Array(False, False);
            Val $b: Boolean = a[1];
            Val name: A = Null;
            getName(c: A){}
            $method(test, test1: Int){}
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,BoolType()),ArrayLiteral([BooleanLiteral(False),BooleanLiteral(False)]))),
        AttributeDecl(Static(),ConstDecl(Id("$b"),BoolType(),ArrayCell(Id("a"),[IntLiteral(1)]))),
        AttributeDecl(Instance(),ConstDecl(Id("name"),ClassType(Id("A")),NullLiteral())),
        MethodDecl(Instance(),Id("getName"),[VarDecl(Id("c"),ClassType(Id("A")))],Block([])),
        MethodDecl(Static(),Id("$method"),[VarDecl(Id("test"),IntType()),VarDecl(Id("test1"),IntType())],Block([]))],Id("Person"))]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_25(self):
        """test mixed declare"""
        input = """Class Program {
            Var a: Float = 1.0001;
            Destructor(){}
            main(){}
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),FloatType(),FloatLiteral(1.0001))),
        MethodDecl(Instance(),Id("Destructor"),[],Block([])),
        MethodDecl(Static(),Id("main"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_26(self):
        """test mixed declare"""
        input = """Class A {
            Var a: Array[Float, 2] = Array(1.01, 2.E10);
            method(){}
        }
        Class B: A {
            Val $b: A;
            Constructor(){}
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(1.01),FloatLiteral(2.E10)]))),
        MethodDecl(Instance(),Id("method"),[],Block([]))]),
        ClassDecl(Id("B"),[AttributeDecl(Static(),ConstDecl(Id("$b"),ClassType(Id("A")),NullLiteral())),
        MethodDecl(Instance(),Id("Constructor"),[],Block([]))],Id("A"))]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_27(self):
        """test mixed declare"""
        input = """Class Program: test {
            Var a: Int = x[1];
            main(a: Int){
                Val b: Boolean = False;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),ArrayCell(Id("x"),[IntLiteral(1)]))),
        MethodDecl(Instance(),Id("main"),[VarDecl(Id("a"),IntType())],Block([ConstDecl(Id("b"),BoolType(),BooleanLiteral(False))]))],Id("test"))]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_28(self):
        """test mixed declare"""
        input = """Class A {
            Var $a: Array[Float, 2];
            method(x: Float){
                x = 1.1;
            }
        }
        Class B: A {
            Val $b: A;
            $func(){}
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Static(),VarDecl(Id("$a"),ArrayType(2,FloatType()))),
        MethodDecl(Instance(),Id("method"),[VarDecl(Id("x"),FloatType())],Block([Assign(Id("x"),FloatLiteral(1.1))]))]),
        ClassDecl(Id("B"),[AttributeDecl(Static(),ConstDecl(Id("$b"),ClassType(Id("A")),NullLiteral())),
        MethodDecl(Static(),Id("$func"),[],Block([]))],Id("A"))]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_29(self):
        """test mixed declare"""
        input = """Class A {
            Var a: String;
            methodA(){}
        }
        Class B: A {
            Val b: A = Null;
            main(){}
        }
        Class C {
            Var c, $d: Int = 1, 2;
            $methodC(){}
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),StringType())),
        MethodDecl(Instance(),Id("methodA"),[],Block([]))]),
        ClassDecl(Id("B"),[AttributeDecl(Instance(),ConstDecl(Id("b"),ClassType(Id("A")),NullLiteral())),
        MethodDecl(Instance(),Id("main"),[],Block([]))],Id("A")),
        ClassDecl(Id("C"),[AttributeDecl(Instance(),VarDecl(Id("c"),IntType(),IntLiteral(1))),
        AttributeDecl(Static(),VarDecl(Id("$d"),IntType(),IntLiteral(2))),
        MethodDecl(Static(),Id("$methodC"),[],Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_30(self):
        """test mixed declare"""
        input = """Class A {
            Var a: Array[Float, 2];
            method(){}
        }
        Class B: A {
            Val $b: A;
            Constructor(){}
            Destructor(){}
            $getB(){}
            $set(c: A){}
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,FloatType()))),
        MethodDecl(Instance(),Id("method"),[],Block([]))]),
        ClassDecl(Id("B"),[AttributeDecl(Static(),ConstDecl(Id("$b"),ClassType(Id("A")),NullLiteral())),
        MethodDecl(Instance(),Id("Constructor"),[],Block([])),
        MethodDecl(Instance(),Id("Destructor"),[],Block([])),
        MethodDecl(Static(),Id("$getB"),[],Block([])),
        MethodDecl(Static(),Id("$set"),[VarDecl(Id("c"),ClassType(Id("A")))],Block([]))],Id("A"))]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_31(self):
        """test expr, expr1"""
        input = """Class Program {
            Var a: String = "BK" +. "HCM";
            Val b: Boolean = a ==. "BKHCM";
            Var c, d, e: Boolean = 1 == 2, 1 != 2, 9 > 10;
            Val f, g, h: Boolean = 9 < 10, 9 >= 10, 9 <= 10;
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),BinaryOp("+.",StringLiteral("BK"),StringLiteral("HCM")))),
        AttributeDecl(Instance(),ConstDecl(Id("b"),BoolType(),BinaryOp("==.",Id("a"),StringLiteral("BKHCM")))),
        AttributeDecl(Instance(),VarDecl(Id("c"),BoolType(),BinaryOp("==",IntLiteral(1),IntLiteral(2)))),
        AttributeDecl(Instance(),VarDecl(Id("d"),BoolType(),BinaryOp("!=",IntLiteral(1),IntLiteral(2)))),
        AttributeDecl(Instance(),VarDecl(Id("e"),BoolType(),BinaryOp(">",IntLiteral(9),IntLiteral(10)))),
        AttributeDecl(Instance(),ConstDecl(Id("f"),BoolType(),BinaryOp("<",IntLiteral(9),IntLiteral(10)))),
        AttributeDecl(Instance(),ConstDecl(Id("g"),BoolType(),BinaryOp(">=",IntLiteral(9),IntLiteral(10)))),
        AttributeDecl(Instance(),ConstDecl(Id("h"),BoolType(),BinaryOp("<=",IntLiteral(9),IntLiteral(10))))])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_32(self):
        """test expr2, expr3"""
        input = """Class Program {
            method(){
                Var a, b: Boolean = True && False, True || False;
                Val c, d: Int = 9 + 10, 9 - 10;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),BoolType(),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False))),
            VarDecl(Id("b"),BoolType(),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False))),
            ConstDecl(Id("c"),IntType(),BinaryOp("+",IntLiteral(9),IntLiteral(10))),
            ConstDecl(Id("d"),IntType(),BinaryOp("-",IntLiteral(9),IntLiteral(10)))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_33(self):
        """test expr4, expr5"""
        input = """Class Program {
            method(){
                Var a, b: Int = 9 * 10, 10 % 1;
                Var c: Float = 100 / 9;
                Var d: Boolean = !True;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),IntType(),BinaryOp("*",IntLiteral(9),IntLiteral(10))),
            VarDecl(Id("b"),IntType(),BinaryOp("%",IntLiteral(10),IntLiteral(1))),
            VarDecl(Id("c"),FloatType(),BinaryOp("/",IntLiteral(100),IntLiteral(9))),
            VarDecl(Id("d"),BoolType(),UnaryOp("!",BooleanLiteral(True)))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_34(self):
        """test expr6, expr7"""
        input = """Class Program {
            method(){
                Var a, b: Int = -10, x[1+2*3];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),IntType(),UnaryOp("-",IntLiteral(10))),
            VarDecl(Id("b"),IntType(),ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3)))]))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_35(self):
        """test expr10, expr7 more"""
        input = """Class Program {
            method(){
                Var a, b: Test = New Test(), New Test(a, 1);
                Var c: Float = !(1 + 2)[a && (b % 10)];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),ClassType(Id("Test")),NewExpr(Id("Test"),[])),
            VarDecl(Id("b"),ClassType(Id("Test")),NewExpr(Id("Test"),[Id("a"),IntLiteral(1)])),
            VarDecl(Id("c"),FloatType(),UnaryOp("!",ArrayCell(BinaryOp("+",IntLiteral(1),IntLiteral(2)),[BinaryOp("&&",Id("a"),BinaryOp("%",Id("b"),IntLiteral(10)))])))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_36(self):
        """test expr8"""
        input = """Class Program {
            method(){
                Var a, b: Int = x.attr, x.func();
                Var c: Float = x.foo(a,b);
                Var d: String = x.y.z;
                Var e: Int = x.y.get();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),IntType(),FieldAccess(Id("x"),Id("attr"))),
            VarDecl(Id("b"),IntType(),CallExpr(Id("x"),Id("func"),[])),
            VarDecl(Id("c"),FloatType(),CallExpr(Id("x"),Id("foo"),[Id("a"),Id("b")])),
            VarDecl(Id("d"),StringType(),FieldAccess(FieldAccess(Id("x"),Id("y")),Id("z"))),
            VarDecl(Id("e"),IntType(),CallExpr(FieldAccess(Id("x"),Id("y")),Id("get"),[]))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_37(self):
        """test expr9"""
        input = """Class Program {
            method(){
                Var a, b: Int = x::$attr, x::$func();
                Var c: Float = x::$foo(a,b);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("method"),[],Block([
            VarDecl(Id("a"),IntType(),FieldAccess(Id("x"),Id("$attr"))),
            VarDecl(Id("b"),IntType(),CallExpr(Id("x"),Id("$func"),[])),
            VarDecl(Id("c"),FloatType(),CallExpr(Id("x"),Id("$foo"),[Id("a"),Id("b")]))
        ]))])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_38(self):
        """test mixed expr"""
        input = """Class Program {
            Var a: Int = -(1 + x[2 || (3 / y[1][2*3])]);
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),
            UnaryOp("-",BinaryOp("+",IntLiteral(1),ArrayCell(Id("x"),[BinaryOp("||",IntLiteral(2),BinaryOp("/",IntLiteral(3),ArrayCell(Id("y"),[IntLiteral(1),BinaryOp("*",IntLiteral(2),IntLiteral(3))])))])))))
        ])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_39(self):
        """test mixed expr"""
        input = """Class Program {
            Constructor(a: Int; b: A; c: String) {
                Self.a = a;
                Self.b = Null;
                x = (c +. "BK").st;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("Constructor"),[
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),ClassType(Id("A"))),
            VarDecl(Id("c"),StringType())
        ],Block([
            Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
            Assign(FieldAccess(SelfLiteral(),Id("b")),NullLiteral()),
            Assign(Id("x"),FieldAccess(BinaryOp("+.",Id("c"),StringLiteral("BK")),Id("st")))
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_40(self):
        """test mixed expr"""
        input = """Class Program {
            Val a: Int = x.y(a0, a1)[z.attr - z] + !(b * 2 - 1).get(x[y.z.set(t - 1)]);
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),ConstDecl(Id("a"),IntType(),
        BinaryOp("+",ArrayCell(CallExpr(Id("x"),Id("y"),[Id("a0"),Id("a1")]),[BinaryOp("-",FieldAccess(Id("z"),Id("attr")),Id("z"))]),
        UnaryOp("!",CallExpr(BinaryOp("-",BinaryOp("*",Id("b"),IntLiteral(2)),IntLiteral(1)),Id("get"),[ArrayCell(Id("x"),[CallExpr(FieldAccess(Id("y"),Id("z")),Id("set"),[BinaryOp("-",Id("t"),IntLiteral(1))])])])))))
        ])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_41(self):
        """test mixed expr"""
        input = """Class Program {
            Val a: Boolean = -(b % c) && ((c * d.get()) || (!(x != y.z)));
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),ConstDecl(Id("a"),BoolType(),
        BinaryOp("&&",UnaryOp("-",BinaryOp("%",Id("b"),Id("c"))),BinaryOp("||",
        BinaryOp("*",Id("c"),CallExpr(Id("d"),Id("get"),[])),UnaryOp("!",BinaryOp("!=",Id("x"),FieldAccess(Id("y"),Id("z"))))))))
        ])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_42(self):
        """test mixed expr"""
        input = """Class Program {
            Val a: A = New A((Self.arr)[1/a.name[sth[A.attr] * !2]]).get();
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [AttributeDecl(Instance(),ConstDecl(Id("a"),ClassType(Id("A")),
        CallExpr(NewExpr(Id("A"),[ArrayCell(FieldAccess(SelfLiteral(),Id("arr")),[BinaryOp("/",IntLiteral(1),ArrayCell(FieldAccess(Id("a"),Id("name")),
        [BinaryOp("*",ArrayCell(Id("sth"),[FieldAccess(Id("A"),Id("attr"))]),UnaryOp("!",IntLiteral(2)))]))])]),Id("get"),[])))
        ])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_43(self):
        """test mixed expr"""
        input = """Class Program {
            foo(a: Int) {
                Var attr: Float = Shape.getY().attr;
                Var a: Int = Shape::$getX();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],Block([VarDecl(Id("attr"),FloatType(),FieldAccess(CallExpr(Id("Shape"),Id("getY"),[]),Id("attr"))),VarDecl(Id("a"),IntType(),CallExpr(Id("Shape"),Id("$getX"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_44(self):
        """test mixed expr"""
        input = """Class Program {
            foo(a: Int) {
                Var a: Float = A[c::$getA(a) == b[1][c::$name]];
                Var b: Test = Null && Self;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],
        Block([VarDecl(Id("a"),FloatType(),ArrayCell(Id("A"),[BinaryOp("==",CallExpr(Id("c"),Id("$getA"),[Id("a")]),ArrayCell(Id("b"),[IntLiteral(1),FieldAccess(Id("c"),Id("$name"))]))])),
        VarDecl(Id("b"),ClassType(Id("Test")),BinaryOp("&&",NullLiteral(),SelfLiteral()))]))])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_45(self):
        """test mixed expr"""
        input = """Class Program {
            foo(a: Int) {
                Var a: A = New A(Null).get.method(a::$set())[1 + 2] * (True && False) / 1 <= 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("a"),IntType())],
        Block([VarDecl(Id("a"),ClassType(Id("A")),BinaryOp("<=",BinaryOp("/",BinaryOp("*",ArrayCell(CallExpr(FieldAccess(NewExpr(Id("A"),[NullLiteral()]),Id("get")),Id("method"),
        [CallExpr(Id("a"),Id("$set"),[])]),[BinaryOp("+",IntLiteral(1),IntLiteral(2))]),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False))),IntLiteral(1)),IntLiteral(2)))]))])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_46(self):
        """test block declare statement"""
        input = """Class Student {
            foo() {
                Var a, b: Int = 1, 2;
                Val c: Float;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            VarDecl(Id("a"),IntType(),IntLiteral(1)),
            VarDecl(Id("b"),IntType(),IntLiteral(2)),
            ConstDecl(Id("c"),FloatType())]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_47(self):
        """test assign statement"""
        input = """Class Student {
            foo() {
                Var a, b: Int;
                a = 1;
                b = 2;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            Assign(Id("a"),IntLiteral(1)),
            Assign(Id("b"),IntLiteral(2))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_48(self):
        """test assign statement"""
        input = """Class Student {
            foo() {
                Point::$a = 1 + 2 * !A.getX(x, y);
                arr[2][3] = New P(x).Y();
                Self.a = 10;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            Assign(FieldAccess(Id("Point"),Id("$a")),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),UnaryOp("!",CallExpr(Id("A"),Id("getX"),[Id("x"),Id("y")]))))),
            Assign(ArrayCell(Id("arr"),[IntLiteral(2),IntLiteral(3)]),CallExpr(NewExpr(Id("P"),[Id("x")]),Id("Y"),[])),
            Assign(FieldAccess(SelfLiteral(),Id("a")),IntLiteral(10))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_49(self):
        """test assign statement"""
        input = """Class Student {
            foo() {
                arr[1] = 1;
                Self.a.b.c = 10;
                x::$name = 9;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            Assign(ArrayCell(Id("arr"),[IntLiteral(1)]),IntLiteral(1)),
            Assign(FieldAccess(FieldAccess(FieldAccess(SelfLiteral(),Id("a")),Id("b")),Id("c")),IntLiteral(10)),
            Assign(FieldAccess(Id("x"),Id("$name")),IntLiteral(9))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_50(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a == b){
                    x = 1;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("==",Id("a"),Id("b")),Block([Assign(Id("x"),IntLiteral(1))]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_51(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a != b){
                    x = 1;
                } Elseif(a == b){
                    x = 2;
                } Else {
                    x = 3;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("!=",Id("a"),Id("b")),Block([Assign(Id("x"),IntLiteral(1))]),If(BinaryOp("==",Id("a"),Id("b")),Block([Assign(Id("x"),IntLiteral(2))]),Block([Assign(Id("x"),IntLiteral(3))])))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_52(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a + b.get()[1]){}
                Elseif(!True){}
                Elseif(a && (1 * 2)){}
                Else{}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("+",Id("a"),ArrayCell(CallExpr(Id("b"),Id("get"),[]),[IntLiteral(1)])),Block([]),
            If(UnaryOp("!",BooleanLiteral(True)),Block([]),If(BinaryOp("&&",Id("a"),BinaryOp("*",IntLiteral(1),IntLiteral(2))),Block([]),Block([]))))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_53(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a == b){
                    If(c == d){
                        a = 1;
                        b = Array(1,2,3);
                    }
                } Else{
                    If(1 == 2){}
                    Elseif(2 == 1){}
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("c"),Id("d")),Block([Assign(Id("a"),IntLiteral(1)),Assign(Id("b"),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))]))]),
            Block([If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([]),If(BinaryOp("==",IntLiteral(2),IntLiteral(1)),Block([])))]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_54(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a == b){
                    If(c == d){
                        If(1 == 2){
                            Return;
                        }
                    } Elseif(True){
                        Return a;
                    }
                } Else{
                    If(1 == 2){}
                    Else{}
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("c"),Id("d")),Block([If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([Return()]))]),If(BooleanLiteral(True),Block([Return(Id("a"))])))]),
            Block([If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([]),Block([]))]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_55(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a == b){
                    If(c == d){
                        If(1 == 2){}
                        Else{}
                    }
                    Else{
                        If(True){}
                        Elseif(False){}
                    }
                }
                Else{
                    Return Self.a[1] + Null - A::$get();
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("c"),Id("d")),Block([If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([]),Block([]))]),
            Block([If(BooleanLiteral(True),Block([]),If(BooleanLiteral(False),Block([])))]))]),Block([
                Return(BinaryOp("-",BinaryOp("+",ArrayCell(FieldAccess(SelfLiteral(),Id("a")),[IntLiteral(1)]),NullLiteral()),CallExpr(Id("A"),Id("$get"),[])))
            ]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_56(self):
        """test if statement"""
        input = """Class Student {
            foo() {
                If(a == b){
                    If(c == d){
                        If(1 == 2){}
                        Else{}
                    }
                    Elseif(False){
                        If(True){}
                        Elseif(False){}
                        Elseif(-1){}
                        Else{}
                    }
                }
                Else{}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("==",Id("c"),Id("d")),Block([If(BinaryOp("==",IntLiteral(1),IntLiteral(2)),Block([]),Block([]))]),
            If(BooleanLiteral(False),Block([If(BooleanLiteral(True),Block([]),If(BooleanLiteral(False),Block([]),If(UnaryOp("-",IntLiteral(1)),Block([]),Block([]))))])))]),Block([]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_57(self):
        """test method invoke statement"""
        input = """Class Student {
            foo() {
                a.get();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            CallStmt(Id("a"),Id("get"),[])]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_58(self):
        """test method invoke statement"""
        input = """Class Student {
            foo() {
                a.get(1, x+y);
                b::$func();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            CallStmt(Id("a"),Id("get"),[IntLiteral(1),BinaryOp("+",Id("x"),Id("y"))]),
            CallStmt(Id("b"),Id("$func"),[])]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_59(self):
        """test method invoke statement"""
        input = """Class Student {
            foo() {
                (a * Null.x[2 || True]).get("BK" ==. "bk");
                b::$func(Self);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            CallStmt(BinaryOp("*",Id("a"),ArrayCell(FieldAccess(NullLiteral(),Id("x")),[BinaryOp("||",IntLiteral(2),BooleanLiteral(True))])),Id("get"),[BinaryOp("==.",StringLiteral("BK"),StringLiteral("bk"))]),
            CallStmt(Id("b"),Id("$func"),[SelfLiteral()])]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_60(self):
        """test method invoke statement"""
        input = """Class Student {
            foo() {
                Self.get(Array(1.3,1.e2) + Array(3.0,0.1e2));
                b::$func(Self.x + A::$x, New T());
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            CallStmt(SelfLiteral(),Id("get"),[BinaryOp("+",ArrayLiteral([FloatLiteral(1.3),FloatLiteral(1.e2)]),ArrayLiteral([FloatLiteral(3.0),FloatLiteral(0.1e2)]))]),
            CallStmt(Id("b"),Id("$func"),[BinaryOp("+",FieldAccess(SelfLiteral(),Id("x")),FieldAccess(Id("A"),Id("$x"))),NewExpr(Id("T"),[])])]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_61(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    a = a + i;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([Assign(Id("a"),BinaryOp("+",Id("a"),Id("i")))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_62(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10 By 2){
                    a = a + i;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([Assign(Id("a"),BinaryOp("+",Id("a"),Id("i")))]),IntLiteral(2))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_63(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In a + 1 .. arr[1][2 || Self.a] By c.get()){
                    a = a + i;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),BinaryOp("+",Id("a"),IntLiteral(1)),ArrayCell(Id("arr"),[IntLiteral(1),BinaryOp("||",IntLiteral(2),FieldAccess(SelfLiteral(),Id("a")))]),Block([Assign(Id("a"),BinaryOp("+",Id("a"),Id("i")))]),CallExpr(Id("c"),Id("get"),[]))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_64(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 1){
                        Return Self;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(1)),Block([Return(SelfLiteral())]))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_65(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    Foreach(j In 012 .. 01){}
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([For(Id("j"),IntLiteral(10),IntLiteral(1),Block([]),IntLiteral(1))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_66(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 1_00_0 By 10){
                    Foreach(j In 100 .. 1 By -1){
                        If(j != i) {
                            j = i;
                        }
                    }
                    If(i == x.get()){
                        Return;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(1000),Block([
                For(Id("j"),IntLiteral(100),IntLiteral(1),Block([If(BinaryOp("!=",Id("j"),Id("i")),Block([Assign(Id("j"),Id("i"))]))]),UnaryOp("-",IntLiteral(1))),
                If(BinaryOp("==",Id("i"),CallExpr(Id("x"),Id("get"),[])),Block([Return()]))]),IntLiteral(10))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_67(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    x = a[i];
                }
                Foreach(i In 10 .. 1 By 2){
                    a[i] = x;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([Assign(Id("x"),ArrayCell(Id("a"),[Id("i")]))]),IntLiteral(1)),
            For(Id("i"),IntLiteral(10),IntLiteral(1),Block([Assign(ArrayCell(Id("a"),[Id("i")]),Id("x"))]),IntLiteral(2))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_68(self):
        """test for statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(Self.x + i == 1){
                        Foreach(j In a[i][2] .. x::$attr){
                            Self.call();
                        }
                    } Else {
                        Return Null;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                If(BinaryOp("==",BinaryOp("+",FieldAccess(SelfLiteral(),Id("x")),Id("i")),IntLiteral(1)),Block([For(Id("j"),ArrayCell(Id("a"),[Id("i"),IntLiteral(2)]),FieldAccess(Id("x"),Id("$attr")),Block([
                    CallStmt(SelfLiteral(),Id("call"),[])
                ]),IntLiteral(1))]),Block([Return(NullLiteral())]))
            ]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_69(self):
        """test break statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 0){
                        Break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([Break()]))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_70(self):
        """test break statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 0){
                        Break;
                    } Elseif(i / 3 != 0){
                        If(arr[i/3]){
                            Break;
                        } Else{
                            Return;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([Break()]),
            If(BinaryOp("!=",BinaryOp("/",Id("i"),IntLiteral(3)),IntLiteral(0)),Block([If(ArrayCell(Id("arr"),[BinaryOp("/",Id("i"),IntLiteral(3))]),Block([Break()]),Block([Return()]))])))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71(self):
        """test continue statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 0){
                        Continue;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([Continue()]))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_72(self):
        """test Continue statement"""
        input = """Class Student {
            foo() {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 0){
                        Continue;
                    } Elseif(i / 3 != 0){
                        If(arr[i/3]){
                            Continue;
                        } Else{
                            Return;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([Continue()]),
            If(BinaryOp("!=",BinaryOp("/",Id("i"),IntLiteral(3)),IntLiteral(0)),Block([If(ArrayCell(Id("arr"),[BinaryOp("/",Id("i"),IntLiteral(3))]),Block([Continue()]),Block([Return()]))])))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73(self):
        """test mixed break, continue statement"""
        input = """Class Program {
            foo(arg: Int) {
                Foreach(i In 1 .. 10){
                    If(i % 2 == 0){
                        Break;
                    } Elseif(i / 3 != 0){
                        If(arr[i/3]){
                            Continue;
                        } Else{
                            Break;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("arg"),IntType())],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([Break()]),
            If(BinaryOp("!=",BinaryOp("/",Id("i"),IntLiteral(3)),IntLiteral(0)),Block([If(ArrayCell(Id("arr"),[BinaryOp("/",Id("i"),IntLiteral(3))]),Block([Continue()]),Block([Break()]))])))]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_74(self):
        """test mixed break, continue statement"""
        input = """Class Program {
            foo(arg: Int) {
                Foreach(i In 1 .. 10){
                    Var a: Boolean = True;
                    Foreach(j In i + 1 .. arg.length()){
                        arr[i][j] = arg[j];
                        If(a == True){
                            Continue;
                        } Else {
                            Break;
                        }
                    }
                    If(x){
                        Break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("arg"),IntType())],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                VarDecl(Id("a"),BoolType(),BooleanLiteral(True)),
                For(Id("j"),BinaryOp("+",Id("i"),IntLiteral(1)),CallExpr(Id("arg"),Id("length"),[]),Block([
                    Assign(ArrayCell(Id("arr"),[Id("i"),Id("j")]),ArrayCell(Id("arg"),[Id("j")])),
                    If(BinaryOp("==",Id("a"),BooleanLiteral(True)),Block([Continue()]),Block([Break()]))
                ]),IntLiteral(1)),
                If(Id("x"),Block([Break()]))
            ]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_75(self):
        """test mixed break, continue statement"""
        input = """Class Program {
            foo(arg: Int) {
                Foreach(i In 1 .. 10){
                    Var a: Boolean = True;
                    If(arg[0] == 1){
                        Continue;
                    }
                    Foreach(j In i + 1 .. arg.length()){
                        arr[i][j] = arg[j];
                        If(a == True){
                            Continue;
                        }
                        If(a.get - b.get() != 0){
                            Break;
                        }
                    }
                    If(x){
                        Break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Program"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("arg"),IntType())],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                VarDecl(Id("a"),BoolType(),BooleanLiteral(True)),
                If(BinaryOp("==",ArrayCell(Id("arg"),[IntLiteral(0)]),IntLiteral(1)),Block([Continue()])),
                For(Id("j"),BinaryOp("+",Id("i"),IntLiteral(1)),CallExpr(Id("arg"),Id("length"),[]),Block([
                    Assign(ArrayCell(Id("arr"),[Id("i"),Id("j")]),ArrayCell(Id("arg"),[Id("j")])),
                    If(BinaryOp("==",Id("a"),BooleanLiteral(True)),Block([Continue()])),
                    If(BinaryOp("!=",BinaryOp("-",FieldAccess(Id("a"),Id("get")),CallExpr(Id("b"),Id("get"),[])),IntLiteral(0)),Block([Break()]))
                ]),IntLiteral(1)),
                If(Id("x"),Block([Break()]))
            ]),IntLiteral(1))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_76(self):
        """test mixed"""
        input = """Class Student {
            Var a, b: Int = 1 + 2, 10;
            main(input: Int) {
                Val temp: Boolean;
                Foreach(i In 1 .. 10 By 2){
                    input[i] = i;
                }
                If(b >= 1){
                    Student.main(a);
                } Elseif(b <= 10){
                    temp = (True && i[2][3 * 2]) || x.get(c != Null);
                } Else {
                    Break;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Student"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),
        AttributeDecl(Instance(),VarDecl(Id("b"),IntType(),IntLiteral(10))),
        MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),IntType())],Block([
            ConstDecl(Id("temp"),BoolType()),
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([Assign(ArrayCell(Id("input"),[Id("i")]),Id("i"))]),IntLiteral(2)),
            If(BinaryOp(">=",Id("b"),IntLiteral(1)),Block([CallStmt(Id("Student"),Id("main"),[Id("a")])]),If(BinaryOp("<=",Id("b"),IntLiteral(10)),Block([
                Assign(Id("temp"),BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),ArrayCell(Id("i"),[IntLiteral(2),BinaryOp("*",IntLiteral(3),IntLiteral(2))])),CallExpr(Id("x"),Id("get"),[BinaryOp("!=",Id("c"),NullLiteral())])))
            ]),Block([Break()])))
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_77(self):
        """test mixed"""
        input = """Class Shape {
                Val $numOfShape: Int = 0;
                Val immutableAttribute: Int = 0;
                Var length, width: Int;
                $getNumOfShape(){
                    Return Shape::$numOfShape;
                }
            }
            Class Rectangle: Shape {
                getArea(){
                    Return Self.length * Self.width;
                }
            }
            Class Program {
                main(){
                    Out.printInt(Shape::$numOfShape);
                }
            }"""
        expect = str(Program([ClassDecl(Id("Shape"),
        [AttributeDecl(Static(),ConstDecl(Id("$numOfShape"),IntType(),IntLiteral(0))),
        AttributeDecl(Instance(),ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),
        AttributeDecl(Instance(),VarDecl(Id("length"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("width"),IntType())),
        MethodDecl(Static(),Id("$getNumOfShape"),[],Block([
            Return(FieldAccess(Id("Shape"),Id("$numOfShape")))
        ]))]),
        ClassDecl(Id("Rectangle"),[
            MethodDecl(Instance(),Id("getArea"),[],Block([
                Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))
            ]))
        ],Id("Shape")),
        ClassDecl(Id("Program"),[
            MethodDecl(Static(),Id("main"),[],Block([CallStmt(Id("Out"),Id("printInt"),[FieldAccess(Id("Shape"),Id("$numOfShape"))])]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_78(self):
        """test mixed"""
        input = """Class Point {
            Foo(a, b: Int) {
                Return a + b;
            }
            Foo1(a,b:Float) {
                Return a + b --a - c % 2 / 1 * a;
            }
            Foo2(a,b:Boolean) {
                Return a || !b && !!!!(c == f);
            }
            Add(a, abcd: String) {
                Return a ==. (b ==. (c ==. (d ==. ("abc" ==. ffff))));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Point"),
        [MethodDecl(Instance(),Id("Foo"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],Block([
            Return(BinaryOp("+",Id("a"),Id("b")))
        ])),
        MethodDecl(Instance(),Id("Foo1"),[VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],Block([
            Return(BinaryOp("-",BinaryOp("-",BinaryOp("+",Id("a"),Id("b")),UnaryOp("-",Id("a"))),BinaryOp("*",BinaryOp("/",BinaryOp("%",Id("c"),IntLiteral(2)),IntLiteral(1)),Id("a"))))
        ])),
        MethodDecl(Instance(),Id("Foo2"),[VarDecl(Id("a"),BoolType()),VarDecl(Id("b"),BoolType())],Block([
            Return(BinaryOp("&&",BinaryOp("||",Id("a"),UnaryOp("!",Id("b"))),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",BinaryOp("==",Id("c"),Id("f"))))))))
        ])),
        MethodDecl(Instance(),Id("Add"),[VarDecl(Id("a"),StringType()),VarDecl(Id("abcd"),StringType())],Block([
            Return(BinaryOp("==.",Id("a"),BinaryOp("==.",Id("b"),BinaryOp("==.",Id("c"),BinaryOp("==.",Id("d"),BinaryOp("==.",StringLiteral("abc"),Id("ffff")))))))
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_79(self):
        """test mixed"""
        input = """Class Point {
            Var a, b: Int;
            Val $c: Boolean = True;
            Constructor(a, b: Int) {
                Self.a = a;
                Self.b = b;
            }
            Destructor() {}
            function(c: Boolean) {
                If(c == Point::$c) {
                    Return a + b;
                }
                Point.function(Point::$c);
            }
        }"""
        expect = str(Program([ClassDecl(Id("Point"),
        [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
        AttributeDecl(Instance(),VarDecl(Id("b"),IntType())),
        AttributeDecl(Static(),ConstDecl(Id("$c"),BoolType(),BooleanLiteral(True))),
        MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],Block([
            Assign(FieldAccess(SelfLiteral(),Id("a")),Id("a")),
            Assign(FieldAccess(SelfLiteral(),Id("b")),Id("b"))
        ])),
        MethodDecl(Instance(),Id("Destructor"),[],Block([])),
        MethodDecl(Instance(),Id("function"),[VarDecl(Id("c"),BoolType())],Block([
            If(BinaryOp("==",Id("c"),FieldAccess(Id("Point"),Id("$c"))),Block([Return(BinaryOp("+",Id("a"),Id("b")))])),
            CallStmt(Id("Point"),Id("function"),[FieldAccess(Id("Point"),Id("$c"))])
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80(self):
        """test mixed"""
        input = """Class Point {
            Var $a, $b: Int = 1+2/arr[1], New X().attr;
            $Function(a: Int; b: Array[Int, 2]) {
                b[1] = Point::$a;
                Foreach(i In 1 .. 10){
                    If(Point::$b == i || !b[1]){
                        Continue;
                    }
                    Point.Function(Point::$a, Point::$b);
                }
                Return Self;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Point"),
        [AttributeDecl(Static(),VarDecl(Id("$a"),IntType(),BinaryOp("+",IntLiteral(1),BinaryOp("/",IntLiteral(2),ArrayCell(Id("arr"),[IntLiteral(1)]))))),
        AttributeDecl(Static(),VarDecl(Id("$b"),IntType(),FieldAccess(NewExpr(Id("X"),[]),Id("attr")))),
        MethodDecl(Static(),Id("$Function"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayType(2,IntType()))],Block([
            Assign(ArrayCell(Id("b"),[IntLiteral(1)]),FieldAccess(Id("Point"),Id("$a"))),
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                If(BinaryOp("==",FieldAccess(Id("Point"),Id("$b")),BinaryOp("||",Id("i"),UnaryOp("!",ArrayCell(Id("b"),[IntLiteral(1)])))),Block([Continue()])),
                CallStmt(Id("Point"),Id("Function"),[FieldAccess(Id("Point"),Id("$a")),FieldAccess(Id("Point"),Id("$b"))])
            ]),IntLiteral(1)),
            Return(SelfLiteral())
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_81(self):
        """test mixed"""
        input = """Class Shape: Point {
            Var x, $y: Int = 1, 2;
            func(x,y,z: Int){
                Self.x = x;
                If(x == y || !z[2]){
                    Point.doSomething();
                } Elseif(123 ==. 234){
                    If(Array(1,2) + stu[1+Self.z]){}
                    Else{}
                    Foreach(i In 1 .. 100){
                        If(i && ("BK" +. "HCM")){
                            Break;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),
        [AttributeDecl(Instance(),VarDecl(Id("x"),IntType(),IntLiteral(1))),
        AttributeDecl(Static(),VarDecl(Id("$y"),IntType(),IntLiteral(2))),
        MethodDecl(Instance(),Id("func"),[VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType()),VarDecl(Id("z"),IntType())],Block([
            Assign(FieldAccess(SelfLiteral(),Id("x")),Id("x")),
            If(BinaryOp("==",Id("x"),BinaryOp("||",Id("y"),UnaryOp("!",ArrayCell(Id("z"),[IntLiteral(2)])))),Block([CallStmt(Id("Point"),Id("doSomething"),[])]),
            If(BinaryOp("==.",IntLiteral(123),IntLiteral(234)),Block([
                If(BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayCell(Id("stu"),[BinaryOp("+",IntLiteral(1),FieldAccess(SelfLiteral(),Id("z")))])),Block([]),Block([])),
                For(Id("i"),IntLiteral(1),IntLiteral(100),Block([
                    If(BinaryOp("&&",Id("i"),BinaryOp("+.",StringLiteral("BK"),StringLiteral("HCM"))),Block([Break()]))
                ]),IntLiteral(1))
            ])))
        ]))
        ],Id("Point"))]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_82(self):
        """test mixed"""
        input = """Class Shape {
            func(_: Int; __: Float){
                Val x: Int = 1_23_456;
                Var y: Float = 1_23.1;
                Var z: Boolean = !-True;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),
        [MethodDecl(Instance(),Id("func"),[VarDecl(Id("_"),IntType()),VarDecl(Id("__"),FloatType())],Block([
            ConstDecl(Id("x"),IntType(),IntLiteral(1_23_456)),
            VarDecl(Id("y"),FloatType(),FloatLiteral(1_23.1)),
            VarDecl(Id("z"),BoolType(),UnaryOp("!",UnaryOp("-",BooleanLiteral(True))))
        ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_83(self):
        """test mixed"""
        input = """Class Rectangle: Shape{
            Constructor(){
                Self.a = a.b.c + a.b.c() * a.b().c / a.b().c();
                Self.b = ((-(1 && 2) + 3 - 4) * 3 - 6/7 + 8%9);
            }

            foo(input: Shape){
                attr = ((((input + a <= b + c) < d) == e) != f) >= 4/3 + 2;
            }
        }
        Class Shape {
            main(){
                a = (!-(New Shape(New Point()))).x;
                b = (1 + 2 * 3/4)[c >= d + e * f];
                c = (3 - Self.a)[-1 + x.a(1 + 2,New a(1, 2))];
                d = (((a.b(1,2))[x.b[2]])[x.y()[3]])[x.y().z[2 + 3]];
            }
        }"""
        expect = str(Program([ClassDecl(Id("Rectangle"),
        [MethodDecl(Instance(),Id("Constructor"),[],Block([
            Assign(FieldAccess(SelfLiteral(),Id("a")),BinaryOp("+",FieldAccess(FieldAccess(Id("a"),Id("b")),Id("c")),BinaryOp("/",BinaryOp("*",CallExpr(FieldAccess(Id("a"),Id("b")),Id("c"),[]),FieldAccess(CallExpr(Id("a"),Id("b"),[]),Id("c"))),CallExpr(CallExpr(Id("a"),Id("b"),[]),Id("c"),[])))),
            Assign(FieldAccess(SelfLiteral(),Id("b")),BinaryOp("+",BinaryOp("-",BinaryOp("*",BinaryOp("-",BinaryOp("+",UnaryOp("-",BinaryOp("&&",IntLiteral(1),IntLiteral(2))),IntLiteral(3)),IntLiteral(4)),IntLiteral(3)),BinaryOp("/",IntLiteral(6),IntLiteral(7))),BinaryOp("%",IntLiteral(8),IntLiteral(9))))])),
        MethodDecl(Instance(),Id("foo"),[VarDecl(Id("input"),ClassType(Id("Shape")))],Block([
            Assign(Id("attr"),BinaryOp(">=",BinaryOp("!=",BinaryOp("==",BinaryOp("<",BinaryOp("<=",BinaryOp("+",Id("input"),Id("a")),BinaryOp("+",Id("b"),Id("c"))),Id("d")),Id("e")),Id("f")),BinaryOp("+",BinaryOp("/",IntLiteral(4),IntLiteral(3)),IntLiteral(2))))]))],Id("Shape")),
        ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("main"),[],Block([
                Assign(Id("a"),FieldAccess(UnaryOp("!",UnaryOp("-",NewExpr(Id("Shape"),[NewExpr(Id("Point"),[])]))),Id("x"))),
                Assign(Id("b"),ArrayCell(BinaryOp("+",IntLiteral(1),BinaryOp("/",BinaryOp("*",IntLiteral(2),IntLiteral(3)),IntLiteral(4))),[BinaryOp(">=",Id("c"),BinaryOp("+",Id("d"),BinaryOp("*",Id("e"),Id("f"))))])),
                Assign(Id("c"),ArrayCell(BinaryOp("-",IntLiteral(3),FieldAccess(SelfLiteral(),Id("a"))),[BinaryOp("+",UnaryOp("-",IntLiteral(1)),CallExpr(Id("x"),Id("a"),[BinaryOp("+",IntLiteral(1),IntLiteral(2)),NewExpr(Id("a"),[IntLiteral(1),IntLiteral(2)])]))])),
                Assign(Id("d"),ArrayCell(ArrayCell(ArrayCell(CallExpr(Id("a"),Id("b"),[IntLiteral(1),IntLiteral(2)]),[ArrayCell(FieldAccess(Id("x"),Id("b")),[IntLiteral(2)])]),[ArrayCell(CallExpr(Id("x"),Id("y"),[]),[IntLiteral(3)])]),[ArrayCell(FieldAccess(CallExpr(Id("x"),Id("y"),[]),Id("z")),[BinaryOp("+",IntLiteral(2),IntLiteral(3))])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_84(self):
        """test mixed"""
        input = """Class Point {
            Var $a, $b: Int = 1+2/arr[1], New X().attr;
            $Function(a: Int; b: Array[Int, 2]) {
                b[1] = Point::$a;
                Foreach(i In 1 .. 10){
                    If(Point::$b == i || !b[1]){
                        Continue;
                    }
                    Point.Function(Point::$a, Point::$b);
                }
                Return Self;
            }
            foo(){
                Foreach(i In 1 .. 10 By 2){
                    If(i == a){
                        Continue;
                    } Else {
                        Break;
                    }
                    Foreach(j In i .. i*3+b[New X()[1]]){
                        Return Shape::$foo();
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Point"),
        [AttributeDecl(Static(),VarDecl(Id("$a"),IntType(),BinaryOp("+",IntLiteral(1),BinaryOp("/",IntLiteral(2),ArrayCell(Id("arr"),[IntLiteral(1)]))))),
        AttributeDecl(Static(),VarDecl(Id("$b"),IntType(),FieldAccess(NewExpr(Id("X"),[]),Id("attr")))),
        MethodDecl(Static(),Id("$Function"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),ArrayType(2,IntType()))],Block([
            Assign(ArrayCell(Id("b"),[IntLiteral(1)]),FieldAccess(Id("Point"),Id("$a"))),
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                If(BinaryOp("==",FieldAccess(Id("Point"),Id("$b")),BinaryOp("||",Id("i"),UnaryOp("!",ArrayCell(Id("b"),[IntLiteral(1)])))),Block([Continue()])),
                CallStmt(Id("Point"),Id("Function"),[FieldAccess(Id("Point"),Id("$a")),FieldAccess(Id("Point"),Id("$b"))])]),IntLiteral(1)),
            Return(SelfLiteral())])),
        MethodDecl(Instance(),Id("foo"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                If(BinaryOp("==",Id("i"),Id("a")),Block([Continue()]),Block([Break()])),
                For(Id("j"),Id("i"),BinaryOp("+",BinaryOp("*",Id("i"),IntLiteral(3)),ArrayCell(Id("b"),[ArrayCell(NewExpr(Id("X"),[]),[IntLiteral(1)])])),Block([Return(CallExpr(Id("Shape"),Id("$foo"),[]))]),IntLiteral(1))]),IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_85(self):
        """test mixed"""
        input = """Class Grade {
            foo(name: String){
                Var x, y: Boolean = True, False;
                If((name +. "HCM") ==. "BK HCM"){
                    Grade::$y = Student.show(name, Self.x);
                    Return a[1] + x[1]*y[x[1] + A.get(a[1])];
                }
                Foreach(i In 1 .. 10 By (School::$getX()).attr[1] + 1){
                    A.foo(name);
                    Self.foo(name);
                }
                Return x + Grade::$y == True;
            }
            Get(e: Grade){
                If (x + y * 3 - 0){
                    Return;
                } 
                Elseif(a == b) {
                    If (1 + 2){
                        a = A[c::$getA(a) == b[1][c::$name]];
                    }
                } Elseif(Point::$a[123][234]){}
                Else{}
            }
        }"""
        expect = str(Program([ClassDecl(Id("Grade"),
        [MethodDecl(Instance(),Id("foo"),[VarDecl(Id("name"),StringType())],Block([
            VarDecl(Id("x"),BoolType(),BooleanLiteral(True)),
            VarDecl(Id("y"),BoolType(),BooleanLiteral(False)),
            If(BinaryOp("==.",BinaryOp("+.",Id("name"),StringLiteral("HCM")),StringLiteral("BK HCM")),Block([
                Assign(FieldAccess(Id("Grade"),Id("$y")),CallExpr(Id("Student"),Id("show"),[Id("name"),FieldAccess(SelfLiteral(),Id("x"))])),
                Return(BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(1)]),BinaryOp("*",ArrayCell(Id("x"),[IntLiteral(1)]),ArrayCell(Id("y"),[BinaryOp("+",ArrayCell(Id("x"),[IntLiteral(1)]),CallExpr(Id("A"),Id("get"),[ArrayCell(Id("a"),[IntLiteral(1)])]))]))))])),
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                CallStmt(Id("A"),Id("foo"),[Id("name")]),
                CallStmt(SelfLiteral(),Id("foo"),[Id("name")])]),BinaryOp("+",ArrayCell(FieldAccess(CallExpr(Id("School"),Id("$getX"),[]),Id("attr")),[IntLiteral(1)]),IntLiteral(1))),
            Return(BinaryOp("==",BinaryOp("+",Id("x"),FieldAccess(Id("Grade"),Id("$y"))),BooleanLiteral(True)))])),
        MethodDecl(Instance(),Id("Get"),[VarDecl(Id("e"),ClassType(Id("Grade")))],Block([
            If(BinaryOp("-",BinaryOp("+",Id("x"),BinaryOp("*",Id("y"),IntLiteral(3))),IntLiteral(0)),Block([Return()]),If(BinaryOp("==",Id("a"),Id("b")),Block([
                If(BinaryOp("+",IntLiteral(1),IntLiteral(2)),Block([Assign(Id("a"),ArrayCell(Id("A"),[BinaryOp("==",CallExpr(Id("c"),Id("$getA"),[Id("a")]),ArrayCell(Id("b"),[IntLiteral(1),FieldAccess(Id("c"),Id("$name"))]))]))]))]),If(ArrayCell(FieldAccess(Id("Point"),Id("$a")),[IntLiteral(123),IntLiteral(234)]),Block([]),Block([]))))]))])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_86(self):
        """test mixed"""
        input = """Class A {
            $rand() {
                Return x::$rand() * x::$rand() / x.a;
            }
            foo() {
                Return Self.foo();
            }
        }
        Class B: A {
            foo() {
                Return A::$rand() * A.sys(Self);
            }
        }
        Class Main {
            $main() {
                Var a: Array[Array[String, 2], 5];
                Foreach (i In 0 .. 10){
                    Var b: B;
                    b = B.foo();
                    If (b == System.isinstance(B)) {
                        a[i][0] = New A();
                    }
                    Else {
                        a[i][0] = New B();
                    }
                    If(a[0] != B.A.foo()) {
                        Break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),
        [MethodDecl(Static(),Id("$rand"),[],Block([
            Return(BinaryOp("/",BinaryOp("*",CallExpr(Id("x"),Id("$rand"),[]),CallExpr(Id("x"),Id("$rand"),[])),FieldAccess(Id("x"),Id("a"))))])),
        MethodDecl(Instance(),Id("foo"),[],Block([
            Return(CallExpr(SelfLiteral(),Id("foo"),[]))]))]),
        ClassDecl(Id("B"),[
            MethodDecl(Instance(),Id("foo"),[],Block([
                Return(BinaryOp("*",CallExpr(Id("A"),Id("$rand"),[]),CallExpr(Id("A"),Id("sys"),[SelfLiteral()])))]))],Id("A")),
        ClassDecl(Id("Main"),[
            MethodDecl(Static(),Id("$main"),[],Block([
                VarDecl(Id("a"),ArrayType(5,ArrayType(2,StringType()))),
                For(Id("i"),IntLiteral(0),IntLiteral(10),Block([
                    VarDecl(Id("b"),ClassType(Id("B")),NullLiteral()),
                    Assign(Id("b"),CallExpr(Id("B"),Id("foo"),[])),
                    If(BinaryOp("==",Id("b"),CallExpr(Id("System"),Id("isinstance"),[Id("B")])),Block([Assign(ArrayCell(Id("a"),[Id("i"),IntLiteral(0)]),NewExpr(Id("A"),[]))]),Block([Assign(ArrayCell(Id("a"),[Id("i"),IntLiteral(0)]),NewExpr(Id("B"),[]))])),
                    If(BinaryOp("!=",ArrayCell(Id("a"),[IntLiteral(0)]),CallExpr(FieldAccess(Id("B"),Id("A")),Id("foo"),[])),Block([Break()]))]),IntLiteral(1))]))])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_87(self):
        """test mixed"""
        input = """Class A {
            Var x, y: Int;
            Var $static: B = New B();
            Constructor(x, y: Int){
                Self.x = x;
                Self.y = y;
            }
            foo() {
                Var a: A = New A(1 + 2, sys.arr[1]);
                Val count: Float = 10_000.123;
                System.out.println("Hello");
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            AttributeDecl(Instance(),VarDecl(Id("x"),IntType())),
            AttributeDecl(Instance(),VarDecl(Id("y"),IntType())),
            AttributeDecl(Static(),VarDecl(Id("$static"),ClassType(Id("B")),NewExpr(Id("B"),[]))),
            MethodDecl(Instance(),Id("Constructor"),[VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())],Block([
                Assign(FieldAccess(SelfLiteral(),Id("x")),Id("x")),
                Assign(FieldAccess(SelfLiteral(),Id("y")),Id("y"))
            ])),
            MethodDecl(Instance(),Id("foo"),[],Block([
                VarDecl(Id("a"),ClassType(Id("A")),NewExpr(Id("A"),[BinaryOp("+",IntLiteral(1),IntLiteral(2)),ArrayCell(FieldAccess(Id("sys"),Id("arr")),[IntLiteral(1)])])),
                ConstDecl(Id("count"),FloatType(),FloatLiteral(10_000.123)),
                CallStmt(FieldAccess(Id("System"),Id("out")),Id("println"),[StringLiteral("Hello")])
            ]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_88(self):
        """test mixed"""
        input = """Class A {
            foo() {
                Var x, y: Int = -111, 0x1AF;
                Foreach(i In 0 .. arr.length() By 10 / 1){
                    If(arr.get(arr[i]) == Null) {
                        Continue;
                    }
                    Foreach(j In 0 .. Self.length(arr.get(i))){
                        If(arr.get(i)[j] == 0){
                            Continue;
                        }
                        If(arr.get(i)[j] && !arr[i][j]){
                            x = i;
                            y = j;
                            Break;
                        }
                    }
                    If(x == Self.x){
                        Break;
                    } Elseif(x == 1) {
                        Return Null;
                    }
                }
                Return arr.get(arr[x])[y];
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            MethodDecl(Instance(),Id("foo"),[],Block([
                VarDecl(Id("x"),IntType(),UnaryOp("-",IntLiteral(111))),
                VarDecl(Id("y"),IntType(),IntLiteral(431)),
                For(Id("i"),IntLiteral(0),CallExpr(Id("arr"),Id("length"),[]),Block([
                    If(BinaryOp("==",CallExpr(Id("arr"),Id("get"),[ArrayCell(Id("arr"),[Id("i")])]),NullLiteral()),Block([Continue()])),
                    For(Id("j"),IntLiteral(0),CallExpr(SelfLiteral(),Id("length"),[CallExpr(Id("arr"),Id("get"),[Id("i")])]),Block([
                        If(BinaryOp("==",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),[Id("j")]),IntLiteral(0)),Block([Continue()])),
                        If(BinaryOp("&&",ArrayCell(CallExpr(Id("arr"),Id("get"),[Id("i")]),[Id("j")]),UnaryOp("!",ArrayCell(Id("arr"),[Id("i"),Id("j")]))),Block([Assign(Id("x"),Id("i")),Assign(Id("y"),Id("j")),Break()]))]),IntLiteral(1)),
                    If(BinaryOp("==",Id("x"),FieldAccess(SelfLiteral(),Id("x"))),Block([Break()]),If(BinaryOp("==",Id("x"),IntLiteral(1)),Block([Return(NullLiteral())])))]),BinaryOp("/",IntLiteral(10),IntLiteral(1))),
                Return(ArrayCell(CallExpr(Id("arr"),Id("get"),[ArrayCell(Id("arr"),[Id("x")])]),[Id("y")]))]))])]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_89(self):
        """test mixed"""
        input = """Class A {
            Var a: Int = 1 + 2;
            foo(x, y: Float){
                x = y + 11.e00;
                If(a == x){
                    Return Grade.foo(1.2, .1e1);
                }
                Return Self.a;
            }
        }"""
        expect = str(Program([ClassDecl(Id("A"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),
            MethodDecl(Instance(),Id("foo"),[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],Block([
                Assign(Id("x"),BinaryOp("+",Id("y"),FloatLiteral(11.e00))),
                If(BinaryOp("==",Id("a"),Id("x")),Block([Return(CallExpr(Id("Grade"),Id("foo"),[FloatLiteral(1.2),FloatLiteral(.1e1)]))])),Return(FieldAccess(SelfLiteral(),Id("a")))]))])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_90(self):
        """test mixed"""
        input = """Class Grade {
            getScore() {
                Point::$a.X = 1 + 2 * !A.getX(x, y);
                Foreach(i In 1 .. 50) {
                    Foreach(j In i + 1 .. New X().attr){}
                    Var a: String = "BK";
                    Self.a = "HCM";
                }
                Foreach(j In 1 .. 50 + 1 - a[1 + A.foo(a,b)] By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Grade"),[
            MethodDecl(Instance(),Id("getScore"),[],Block([
                Assign(FieldAccess(FieldAccess(Id("Point"),Id("$a")),Id("X")),BinaryOp("+",IntLiteral(1),BinaryOp("*",IntLiteral(2),UnaryOp("!",CallExpr(Id("A"),Id("getX"),[Id("x"),Id("y")]))))),
                For(Id("i"),IntLiteral(1),IntLiteral(50),Block([
                    For(Id("j"),BinaryOp("+",Id("i"),IntLiteral(1)),FieldAccess(NewExpr(Id("X"),[]),Id("attr")),Block([]),IntLiteral(1)),
                    VarDecl(Id("a"),StringType(),StringLiteral("BK")),
                    Assign(FieldAccess(SelfLiteral(),Id("a")),StringLiteral("HCM"))]),IntLiteral(1)),
                For(Id("j"),IntLiteral(1),BinaryOp("-",BinaryOp("+",IntLiteral(50),IntLiteral(1)),ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(1),CallExpr(Id("A"),Id("foo"),[Id("a"),Id("b")]))])),Block([CallStmt(Id("Out"),Id("printInt"),[Id("i")])]),IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_91(self):
        """test mixed"""
        input = """Class Shape {
            func(x, y, z: Int){
                Val x, y: Int = 111 + Array(1, 2) / New x(), 1;
                x = y == z + 1;
                Return;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("func"),[VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType()),VarDecl(Id("z"),IntType())],Block([
                ConstDecl(Id("x"),IntType(),BinaryOp("+",IntLiteral(111),BinaryOp("/",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),NewExpr(Id("x"),[])))),
                ConstDecl(Id("y"),IntType(),IntLiteral(1)),Assign(Id("x"),BinaryOp("==",Id("y"),BinaryOp("+",Id("z"),IntLiteral(1)))),
                Return()]))])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_92(self):
        """test mixed"""
        input = """Class Shape {
            Var a: String = "Hello, '" John ";
            Var b: Array[Array[Int, 2], 1] = Array(Array(1), Array(1,2));
            method(){
                Var c: A;
                If(a ==. (c + New A(x).get(y))){
                    Foreach(i In 1 .. 10){
                        If(c == 1){
                            Continue;
                        } Else {
                            Break;
                        }
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),StringType(),StringLiteral("Hello, '\" John "))),
            AttributeDecl(Instance(),VarDecl(Id("b"),ArrayType(1,ArrayType(2,IntType())),ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(1),IntLiteral(2)])]))),
            MethodDecl(Instance(),Id("method"),[],Block([
                VarDecl(Id("c"),ClassType(Id("A")),NullLiteral()),
                If(BinaryOp("==.",Id("a"),BinaryOp("+",Id("c"),CallExpr(NewExpr(Id("A"),[Id("x")]),Id("get"),[Id("y")]))),Block([
                    For(Id("i"),IntLiteral(1),IntLiteral(10),Block([If(BinaryOp("==",Id("c"),IntLiteral(1)),Block([Continue()]),Block([Break()]))]),IntLiteral(1))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_93(self):
        """test mixed"""
        input = """Class Shape {
            method(){
                Val a: A;
                arr[1] = Array(1,2) + Array(2,4);
                x.a.b.c.d.e.f();
                Return Self + New B();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("method"),[],Block([
                ConstDecl(Id("a"),ClassType(Id("A")),NullLiteral()),
                Assign(ArrayCell(Id("arr"),[IntLiteral(1)]),BinaryOp("+",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(2),IntLiteral(4)]))),CallStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id("x"),Id("a")),Id("b")),Id("c")),Id("d")),Id("e")),Id("f"),[]),
                Return(BinaryOp("+",SelfLiteral(),NewExpr(Id("B"),[])))]))])]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_94(self):
        """test mixed"""
        input = """Class Shape {
            method(){
                Foreach(i In True .. z - 1){
                    Var a: String;
                    io.push(stdin);
                    std::$getline(a);
                    If(a != "-1"){
                        Shape.draw(a);
                    } Else {
                        Break;
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("method"),[],Block([
                For(Id("i"),BooleanLiteral(True),BinaryOp("-",Id("z"),IntLiteral(1)),Block([
                    VarDecl(Id("a"),StringType()),CallStmt(Id("io"),Id("push"),[Id("stdin")]),CallStmt(Id("std"),Id("$getline"),[Id("a")]),
                    If(BinaryOp("!=",Id("a"),StringLiteral("-1")),Block([CallStmt(Id("Shape"),Id("draw"),[Id("a")])]),Block([Break()]))]),IntLiteral(1))]))])]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95(self):
        """test mixed"""
        input = """Class Shape {
            Val $a: A;
            method(){
                If(Shape::$a == Null){
                    Shape::$a = Self;
                }
            }
            Var text: String;
            $display(str: String){
                text = str;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            AttributeDecl(Static(),ConstDecl(Id("$a"),ClassType(Id("A")),NullLiteral())),
            MethodDecl(Instance(),Id("method"),[],Block([
                If(BinaryOp("==",FieldAccess(Id("Shape"),Id("$a")),NullLiteral()),Block([Assign(FieldAccess(Id("Shape"),Id("$a")),SelfLiteral())]))])),
            AttributeDecl(Instance(),VarDecl(Id("text"),StringType())),
            MethodDecl(Static(),Id("$display"),[VarDecl(Id("str"),StringType())],Block([Assign(Id("text"),Id("str"))]))])]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_96(self):
        """test mixed"""
        input = """Class Shape {
            foo(arr: Array[Int, 3]){
                Var s: Int = 0;
                Foreach(i In 0 .. 10){
                    s = s + arr[i];
                }
                Return s;
            }
            main(){
                Var arr: Array[Int, 3];
                Foreach(i In 0 .. 3){
                    Var temp: Int;
                    temp = System.call("Int num");
                    If(temp > 0){
                        Continue;
                    } Else {
                        Console.log("Error");
                    }
                }
                std.cout(Self.sum(arr));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("foo"),[VarDecl(Id("arr"),ArrayType(3,IntType()))],Block([
                VarDecl(Id("s"),IntType(),IntLiteral(0)),
                For(Id("i"),IntLiteral(0),IntLiteral(10),Block([Assign(Id("s"),BinaryOp("+",Id("s"),ArrayCell(Id("arr"),[Id("i")])))]),IntLiteral(1)),
                Return(Id("s"))])),
            MethodDecl(Instance(),Id("main"),[],Block([
                VarDecl(Id("arr"),ArrayType(3,IntType())),
                For(Id("i"),IntLiteral(0),IntLiteral(3),Block([
                    VarDecl(Id("temp"),IntType()),Assign(Id("temp"),CallExpr(Id("System"),Id("call"),[StringLiteral("Int num")])),
                    If(BinaryOp(">",Id("temp"),IntLiteral(0)),Block([Continue()]),Block([CallStmt(Id("Console"),Id("log"),[StringLiteral("Error")])]))]),IntLiteral(1)),
                CallStmt(Id("std"),Id("cout"),[CallExpr(SelfLiteral(),Id("sum"),[Id("arr")])])]))])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_97(self):
        """test mixed"""
        input = """Class Shape {
            foo(){
                If(a == b){
                    If(c != d){
                        If(e > f){
                            Return True == False;
                        }
                        Else{
                            Return 1;
                        }
                    } Elseif(c == d){
                        Return Null;
                    }
                } Else {
                    Return window.getChildCount();
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            MethodDecl(Instance(),Id("foo"),[],Block([
                If(BinaryOp("==",Id("a"),Id("b")),Block([If(BinaryOp("!=",Id("c"),Id("d")),Block([If(BinaryOp(">",Id("e"),Id("f")),Block([Return(BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False)))]),Block([Return(IntLiteral(1))]))]),If(BinaryOp("==",Id("c"),Id("d")),Block([Return(NullLiteral())])))]),Block([Return(CallExpr(Id("window"),Id("getChildCount"),[]))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_98(self):
        """test mixed"""
        input = """Class Shape: Point {
            ## This is comment
            Hello my fen ##
            Var a: Int = 1;
            Foo(){}
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),IntLiteral(1))),
            MethodDecl(Instance(),Id("Foo"),[],Block([]))],Id("Point"))]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_99(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Array[Int, 1_00_00];
            foo(){
                a[b[1] * b[2]] = Self.x;
                x.a.foo().get().x = a >= b;
            }
        }
        Class B: Shape {
            main(input: Float){
                Console.log(input);
            }
        }
        Class Program {
            main(){
                array.map(os.arrowFunc(Console.log(a)));
            }
        }"""
        expect = str(Program([ClassDecl(Id("Shape"),[
            AttributeDecl(Instance(),ConstDecl(Id("a"),ArrayType(10000,IntType()))),
            MethodDecl(Instance(),Id("foo"),[],Block([
                Assign(ArrayCell(Id("a"),[BinaryOp("*",ArrayCell(Id("b"),[IntLiteral(1)]),ArrayCell(Id("b"),[IntLiteral(2)]))]),FieldAccess(SelfLiteral(),Id("x"))),
                Assign(FieldAccess(CallExpr(CallExpr(FieldAccess(Id("x"),Id("a")),Id("foo"),[]),Id("get"),[]),Id("x")),BinaryOp(">=",Id("a"),Id("b")))]))]),
            ClassDecl(Id("B"),[MethodDecl(Instance(),Id("main"),[VarDecl(Id("input"),FloatType())],Block([CallStmt(Id("Console"),Id("log"),[Id("input")])]))],Id("Shape")),
            ClassDecl(Id("Program"),[MethodDecl(Static(),Id("main"),[],Block([CallStmt(Id("array"),Id("map"),[CallExpr(Id("os"),Id("arrowFunc"),[CallExpr(Id("Console"),Id("log"),[Id("a")])])])]))])]))
        self.assertTrue(TestAST.test(input,expect,399))

    def test_100(self):
        """test mixed"""
        input = """Class Tree {
            insertNode(idx: Int; root: Node; value: Int){
                If(idx == 0 && (root == Null)){
                    root = New Node(root, value);
                } Else {
                    Tree.insertNode(idx - 1, root.getNext(), value);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Tree"),[
            MethodDecl(Instance(),Id("insertNode"),[VarDecl(Id("idx"),IntType()),VarDecl(Id("root"),ClassType(Id("Node"))),VarDecl(Id("value"),IntType())],Block([
                If(BinaryOp("==",Id("idx"),BinaryOp("&&",IntLiteral(0),BinaryOp("==",Id("root"),NullLiteral()))),Block([Assign(Id("root"),NewExpr(Id("Node"),[Id("root"),Id("value")]))]),Block([CallStmt(Id("Tree"),Id("insertNode"),[BinaryOp("-",Id("idx"),IntLiteral(1)),CallExpr(Id("root"),Id("getNext"),[]),Id("value")])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,400))