from ast import BinOp
from msilib.schema import Class
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        """Simple program: int main() {} """
        input = """Class A {}"""
        expect = str(Program([
            ClassDecl(Id("A"), [])
        ]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        """More complex program"""
        input = """Class A: B {}"""
        expect = str(Program([
            ClassDecl(Id("A"),[],Id("B"))
        ]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_302(self):
        """More complex program"""
        input = """Class A {
            Var a: Int;
        }"""
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(Instance(), VarDecl(Id("a"),IntType()))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_303(self):
        input = """Class A {
            Var a, $b: Int;
        }"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            Id("a"),
                            IntType()
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        VarDecl(
                            Id("$b"),
                            IntType()
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304(self):
        input = """Class A {
            Var a, $b: Int = 0, 1;
        }"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            Id("a"),
                            IntType(),
                            IntLiteral(0)
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        VarDecl(
                            Id("$b"),
                            IntType(),
                            IntLiteral(1)
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_305(self):
        input = """Class A {}
        Class B: A {}
        Class C: B {}"""
        expect = str(Program([
            ClassDecl(Id("A"),[],),
            ClassDecl(Id("B"),[],Id("A")),
            ClassDecl(Id("C"),[],Id("B"))
        ]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_306(self):
        input = """Class Decls {
            Var a: Int;
            Val $b: Boolean = True;
        }"""
        expect = str(Program([
            ClassDecl(Id("Decls"),[
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType())),
                AttributeDecl(Static(),ConstDecl(Id("$b"), BoolType(), BooleanLiteral(True)))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_307(self):
        input = """Class Decls {
            func(a, b: Int; c: Boolean) {}
        }"""
        expect = str(Program([
            ClassDecl(Id("Decls"), [
                MethodDecl(Instance(), Id("func"),
                    [
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType()),
                        VarDecl(Id("c"), BoolType())
                    ],
                    Block([])
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_308(self):
        input = """Class Decls {
            Constructor(a, b: Int) {}
            Destructor() {}
        }"""
        expect = str(Program([
            ClassDecl(Id("Decls"), [
                MethodDecl(Instance(), Id("Constructor"), [
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), IntType())
                    ],
                    Block([])
                ),
                MethodDecl(Instance(), Id("Destructor"), [],
                    Block([])
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_309(self):
        input = """Class Decls {
            $func(a:Int; b:Float) {}
        }"""
        expect = str(Program([
            ClassDecl(Id("Decls"), [
                MethodDecl(Static(), Id("$func"), [
                        VarDecl(Id("a"), IntType()),
                        VarDecl(Id("b"), FloatType())
                    ],
                    Block([])
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_310(self):
        input = """
        Class A {
            main() {}
        }
        Class Program {
            main(a: Int) {}

            main() {}
        }"""
        expect = str(Program([
            ClassDecl(Id("A"), [
                MethodDecl(Instance(), Id("main"), [], Block([]))
            ]),
            ClassDecl(Id("Program"), [
                MethodDecl(Instance(), Id("main"), [
                    VarDecl(Id("a"), IntType())
                ], Block([])),
                MethodDecl(Static(), Id("main"), [], Block([]))
            ])
        ]))

        self.assertTrue(TestAST.test(input,expect,310))

    def test_311(self):
        input = """Class Type {
            Var a: Boolean;
            Var b: Boolean = True || !a;
        }"""
        expect = str(Program([
            ClassDecl(Id("Type"), [
                AttributeDecl(Instance(),
                    VarDecl(Id("a"), BoolType())
                ),
                AttributeDecl(Instance(),
                    VarDecl(Id("b"), BoolType(), BinaryOp(
                        "||",
                        BooleanLiteral(True),
                        UnaryOp("!", Id("a"))))
                )
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_312(self):
        input = """Class Type {
            check() {
                a = (c == b) && (b != False);
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Type"), [
                MethodDecl(Instance(), Id("check"), [], Block([
                    Assign(
                        Id("a"),
                        BinaryOp("&&",
                            BinaryOp("==", Id("c"), Id("b")),
                            BinaryOp("!=", Id("b"), BooleanLiteral(False))
                        )
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_313(self):
        input = """Class Lit {
            check() {
                Val i1: Int = 0b11 + 0X16A7;
                Val i2: Int = 0123 % 12_345;
                Val i3: Int = 00 + 0;
                Val i4: Int = 0x0 >= 0B0;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                MethodDecl(Instance(), Id("check"), [], 
                Block([
                    ConstDecl(Id("i1"), IntType(), BinaryOp("+", IntLiteral(0b11), IntLiteral(0X16A7))),
                    ConstDecl(Id("i2"), IntType(), BinaryOp("%", IntLiteral(0o123), IntLiteral(12345))),
                    ConstDecl(Id("i3"), IntType(), BinaryOp("+", IntLiteral(0o0), IntLiteral(0))),
                    ConstDecl(Id("i4"), IntType(), BinaryOp(">=", IntLiteral(0x0), IntLiteral(0b0)))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_314(self):
        input = """Class Lit {
            check() {
                Val i1: Float = 0.7e-3;
                Val i2: Float = 1_2.7E-3;
                Val i3: Float = 0.7;
                Val i4: Float = 0.;
                Val i5: Float = 1e-3;
                Val i6: Float = .7e-3;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                MethodDecl(Instance(), Id("check"), [], 
                Block([
                    ConstDecl(Id("i1"), FloatType(), FloatLiteral(0.7e-3)),
                    ConstDecl(Id("i2"), FloatType(), FloatLiteral(12.7e-3)),
                    ConstDecl(Id("i3"), FloatType(), FloatLiteral(0.7)),
                    ConstDecl(Id("i4"), FloatType(), FloatLiteral(0.)),
                    ConstDecl(Id("i5"), FloatType(), FloatLiteral(1e-3)),
                    ConstDecl(Id("i6"), FloatType(), FloatLiteral(.7e-3))
                ]))
            ])
        ]))
        # print("314---", expect)
        self.assertTrue(TestAST.test(input,expect,314))

    def test_315(self):
        input = """Class Lit {
            check() {
                Var s1: String;
                Var s2, s3: String = "", "Medium";
                Var s4: String = "This is a long string";
                Var s5: String = "This is a \\t tabbed string";
                Var s6: String = "This is a '"quoted'" string";
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"),[
                MethodDecl(Instance(),Id("check"),[],
                    Block([
                        VarDecl(Id("s1"),StringType()),
                        VarDecl(Id("s2"),StringType(),StringLiteral("")),
                        VarDecl(Id("s3"),StringType(),StringLiteral("Medium")),
                        VarDecl(Id("s4"),StringType(),StringLiteral("This is a long string")),
                        VarDecl(Id("s5"),StringType(),StringLiteral("This is a \\t tabbed string")),
                        VarDecl(Id("s6"),StringType(),StringLiteral("This is a '\"quoted'\" string"))
                    ])
                )
            ])
        ]))
        # print("315--", expect)
        self.assertTrue(TestAST.test(input,expect,315))

    def test_316(self):
        input = """Class Lit {
            Var a: Array[Int, 5];
            Var a: Array[Int, 012];
            Var $a: Array[String, 1];
            check() {
                Var a: Array[Float, 0B11101];
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                AttributeDecl(Instance(), VarDecl(Id("a"), ArrayType(5, IntType()))),
                AttributeDecl(Instance(), VarDecl(Id("a"), ArrayType(0o12, IntType()))),
                AttributeDecl(Static(), VarDecl(Id("$a"), ArrayType(1, StringType()))),
                MethodDecl(Instance(), Id("check"), [], Block([
                    VarDecl(Id("a"), ArrayType(0b11101, FloatType()))
                ]))
            ])
        ]))
        # print("316--", expect)
        self.assertTrue(TestAST.test(input,expect,316))

    def test_317(self):
        input = """Class Lit {
            Var a: Array[ Array[Int, 5], 10 ];
            Var a: Array[ Array[ Array[Boolean, 3], 5], 10 ];
            check() {
                Var a: Array[ Array[Float, 2], 5 ];
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                AttributeDecl(Instance(), VarDecl(Id("a"), 
                    ArrayType(10, ArrayType(5, IntType()))    
                )),
                AttributeDecl(Instance(), VarDecl(Id("a"), 
                    ArrayType(10, ArrayType(5, ArrayType(3, BoolType())))    
                )),
                MethodDecl(Instance(), Id("check"), [], Block([
                    VarDecl(Id("a"), ArrayType(5, ArrayType(2, FloatType())))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_318(self):
        input = """Class Lit {
            Var a: Rectangle;
            Var a: Rectangle = New Rectangle();
            Var a: Rectangle = New Rectangle(1, 2);
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                AttributeDecl(Instance(), VarDecl(Id("a"), 
                    ClassType(Id("Rectangle")), 
                    NullLiteral() 
                )),
                AttributeDecl(Instance(), VarDecl(Id("a"), 
                    ClassType(Id("Rectangle")), 
                    NewExpr(Id("Rectangle"), [])
                )),
                AttributeDecl(Instance(), VarDecl(Id("a"), 
                    ClassType(Id("Rectangle")), 
                    NewExpr(Id("Rectangle"), [
                        IntLiteral(1), 
                        IntLiteral(2)
                    ])
                )),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_319(self):
        input = """Class Lit {
            check(a, b: Array[Int, 5]; c: Array[Array[Int, 7], 9]) {
                Var a: Array[ Array[Float, 2], 5 ];
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                MethodDecl(Instance(), Id("check"), [
                    VarDecl(Id("a"), ArrayType(5, IntType())),
                    VarDecl(Id("b"), ArrayType(5, IntType())),
                    VarDecl(Id("c"), ArrayType(9, ArrayType(7, IntType()))),
                ], Block([
                    VarDecl(Id("a"), ArrayType(5, ArrayType(2, FloatType())))
                ]))
            ])
        ]))
        # print(expect)
        self.assertTrue(TestAST.test(input,expect,319))

    def test_320(self):
        input = """Class Lit {
            check(a, b: Rectangle; c: Circle) {
                a.draw(b.__edge__);
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Lit"), [
                MethodDecl(Instance(), Id("check"), [
                    VarDecl(Id("a"), ClassType(Id("Rectangle"))),
                    VarDecl(Id("b"), ClassType(Id("Rectangle"))),
                    VarDecl(Id("c"), ClassType(Id("Circle"))),
                ], Block([
                    CallStmt(Id("a"), Id("draw"), [
                        FieldAccess(Id("b"), Id("__edge__"))
                    ])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_321(self):
        input = """Class Expr {
            Var a: Int = -1 + 1 - 1 * 1 / 1 % 1;
        }"""
        expect = str(Program([ClassDecl(Id("Expr"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),IntType(),
                BinaryOp("-",
                    BinaryOp("+",
                        UnaryOp("-",IntLiteral(1)),
                        IntLiteral(1)
                    ),
                    BinaryOp("%",
                        BinaryOp("/",
                            BinaryOp("*",IntLiteral(1),IntLiteral(1)),
                            IntLiteral(1)
                        ),
                        IntLiteral(1)
                    )
                )))])]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_322(self):
        input = """Class Expr {
            Var a: Boolean = !a || a && a;
            Var a: Boolean = string ==. string;
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(), VarDecl(Id("a"), BoolType(), 
                    BinaryOp("&&",
                        BinaryOp("||",
                            UnaryOp("!",Id("a")),
                            Id("a")
                        ),
                        Id("a")
                    )
                )),
                AttributeDecl(Instance(), VarDecl(Id("a"), BoolType(), 
                    BinaryOp("==.", Id("string"), Id("string"))
                ))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_323(self):
        input = """Class Expr {
            Var a: Boolean = (1 == 1) != 1;
            Var a: Boolean = (1 > 1) < 1;
            Var a: Boolean = 1 >= (1 <= 1);
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"),BoolType(),
                    BinaryOp("!=",
                        BinaryOp("==",IntLiteral(1),IntLiteral(1)),
                        IntLiteral(1)))),
                AttributeDecl(Instance(),VarDecl(Id("a"),BoolType(),
                    BinaryOp("<",
                        BinaryOp(">",IntLiteral(1),IntLiteral(1)),
                        IntLiteral(1)))),
                AttributeDecl(Instance(),VarDecl(Id("a"),BoolType(),
                    BinaryOp(">=",
                        IntLiteral(1),
                        BinaryOp("<=",IntLiteral(1),IntLiteral(1)))))
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_324(self):
        input = """Class Expr {
            Var a: Int = a[1];
            Var a: Int = a[1][1 + 2];
            Var a: Int = a[1][sub.size];
            Var a: Int = a[varname];
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(Id("a"), [IntLiteral(1)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(Id("a"), [IntLiteral(1), BinaryOp("+", IntLiteral(1), IntLiteral(2))]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(Id("a"), [IntLiteral(1), FieldAccess(Id("sub"), Id("size"))]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(Id("a"), [Id("varname")]))),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_325(self):
        input = """Class Expr {
            Var a: Int = a.a;
            Var a: Int = a.a[1];
            Var a: Int = a.a[1][2];
            Var a: Int = Shape::$num;
            Var a: Int = Shape::$num[1];
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), FieldAccess(Id("a"), Id("a")))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(FieldAccess(Id("a"), Id("a")), [IntLiteral(1)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(FieldAccess(Id("a"), Id("a")), [IntLiteral(1), IntLiteral(2)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), FieldAccess(Id("Shape"), Id("$num")))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(FieldAccess(Id("Shape"), Id("$num")), [IntLiteral(1)]))),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_326(self):
        input = """Class Expr {
            Var a: Int = (1 + 2).a;
            Var a: Int = "String".length;
            Var a: Int = Shape::$num.value;
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), FieldAccess(BinaryOp("+", IntLiteral(1), IntLiteral(2)), Id("a")))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), FieldAccess(StringLiteral("String"), Id("length")))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), FieldAccess(FieldAccess(Id("Shape"), Id("$num")), Id("value")))),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_327(self):
        input = """Class Expr {
            Var a: Int = a.a();
            Var a: Int = a.a()[1];
            Var a: Int = a.a()[1][2];
            Var a: Int = Shape::$num();
            Var a: Int = Shape::$num()[1];
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("a"), Id("a"), []))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(CallExpr(Id("a"), Id("a"), []), [IntLiteral(1)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(CallExpr(Id("a"), Id("a"), []), [IntLiteral(1), IntLiteral(2)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("Shape"), Id("$num"), []))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), ArrayCell(CallExpr(Id("Shape"), Id("$num"), []), [IntLiteral(1)]))),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_328(self):
        input = """Class Expr {
            Var a: Int = a.a(1, 2, 3);
            Var a: Int = a.a(a.length, a::$size);
            Var a: Int = a.a(a[1], a[2]);
            Var a: Int = Shape::$num(1, 2, 3);
            Var a: Int = Shape::$num(a[1]);
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("a"), Id("a"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("a"), Id("a"), [FieldAccess(Id("a"), Id("length")), FieldAccess(Id("a"), Id("$size"))]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("a"), Id("a"), [ArrayCell(Id("a"), [IntLiteral(1)]), ArrayCell(Id("a"), [IntLiteral(2)])]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("Shape"), Id("$num"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), CallExpr(Id("Shape"), Id("$num"), [ArrayCell(Id("a"), [IntLiteral(1)])]))),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_329(self):
        input = """Class Expr {
            Var a: Int = New Ele();
            Var a: Int = New Ele(1, 2);
            check() {
                Var a: Int = New Ele();
                Var a: Int = New Ele(1, 2);
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), NewExpr(Id("Ele"), []))),
                AttributeDecl(Instance(),VarDecl(Id("a"), IntType(), NewExpr(Id("Ele"), [IntLiteral(1), IntLiteral(2)]))),
                MethodDecl(Instance(), Id("check"), [], Block([
                    VarDecl(Id("a"), IntType(), NewExpr(Id("Ele"), [])),
                    VarDecl(Id("a"), IntType(), NewExpr(Id("Ele"), [IntLiteral(1), IntLiteral(2)])),
                ])),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_330(self):
        input = """Class Expr {
            check() {
                Return Self;
                Return Self.hate;
                Return Self + Self;
                Return Self[hatred];
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"), [
                MethodDecl(Instance(), Id("check"), [], Block([
                    Return(SelfLiteral()),
                    Return(FieldAccess(SelfLiteral(), Id("hate"))),
                    Return(BinaryOp("+", SelfLiteral(), SelfLiteral())),
                    Return(ArrayCell(SelfLiteral(), [Id("hatred")])),
                ])),
            ])
        ]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_331(self):
        input = """Class Expr {
            Var a: Array[Int, 3] = (a + a) * a::$a; 
            Var $a: String = - a - a % a.a;
            check() {
                Var a: Array[Int, 3] = (a == a) * a::$a; 
                Var a: String = - a - a % a[a];
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("Expr"),[
                AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(3,IntType()),
                    BinaryOp("*",
                        BinaryOp("+",Id("a"),Id("a")),
                        FieldAccess(Id("a"),Id("$a"))
                ))),
                AttributeDecl(Static(),VarDecl(Id("$a"),StringType(),
                    BinaryOp("-",
                        UnaryOp("-",Id("a")),
                        BinaryOp("%",Id("a"),FieldAccess(Id("a"),Id("a")))
                ))),
                MethodDecl(Instance(),Id("check"),[],Block([
                    VarDecl(Id("a"),ArrayType(3,IntType()),
                        BinaryOp("*",
                            BinaryOp("==",Id("a"),Id("a")),
                            FieldAccess(Id("a"),Id("$a")))),
                    VarDecl(Id("a"),StringType(),
                        BinaryOp("-",
                            UnaryOp("-",Id("a")),
                            BinaryOp("%",Id("a"),ArrayCell(Id("a"),[Id("a")]))))]))
        ])]))
        self.assertTrue(TestAST.test(input,expect,331))

    def test_332(self):
        input = """Class Expr {
            Var a: Rect = New Rect() + New PrevRect();
            Var a: Rect = (a >= b) || !(a < b);
            check() {
                {
                    Var a: Rect = New Rect() + New PrevRect();
                    Var a: Rect = (a >= b) || !(a < b);
                }
            }
            
        }"""
        expect = str(Program([ClassDecl(Id("Expr"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("Rect")),
                BinaryOp("+",
                    NewExpr(Id("Rect"),[]),
                    NewExpr(Id("PrevRect"),[])))),
            AttributeDecl(Instance(),VarDecl(Id("a"),ClassType(Id("Rect")),
                BinaryOp("||",
                    BinaryOp(">=",Id("a"),Id("b")),
                    UnaryOp("!",BinaryOp("<",Id("a"),Id("b")))))),
            MethodDecl(Instance(),Id("check"),[],Block([
                Block([
                    VarDecl(Id("a"),ClassType(Id("Rect")),
                        BinaryOp("+",
                            NewExpr(Id("Rect"),[]),
                            NewExpr(Id("PrevRect"),[]))),
                    VarDecl(Id("a"),ClassType(Id("Rect")),
                        BinaryOp("||",
                            BinaryOp(">=",Id("a"),Id("b")),
                            UnaryOp("!",BinaryOp("<",Id("a"),Id("b")))))])]))])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_333(self):
        input = """Class ArrayLit {
            Var a: Array[Int, 3] = Array(0, 1, 0 + 1);
            Var a: Array[String, 4] = Array("S", "3", "X", "Y");
            Var a: Array[Array[String, 1], 2] = Array(
                Array("This", "is"),
                Array("a", "multi-dimensional"),
                Array("array", "!")
            );
            check() {
                Var a: Array[Array[String, 1], 2] = Array(
                    Array("This", "is"),
                    Array("a", "multi-dimensional"),
                    Array("array", "!")
                );
            }
        }"""
        expect = str(Program([ClassDecl(Id("ArrayLit"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(3,IntType()),
                ArrayLiteral([IntLiteral(0),IntLiteral(1),BinaryOp("+",IntLiteral(0),IntLiteral(1))]))),
            AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(4,StringType()),
                ArrayLiteral([StringLiteral("S"),StringLiteral("3"),StringLiteral("X"),StringLiteral("Y")]))),
            AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,ArrayType(1,StringType())),
                ArrayLiteral([
                    ArrayLiteral([StringLiteral("This"),StringLiteral("is")]),
                    ArrayLiteral([StringLiteral("a"),StringLiteral("multi-dimensional")]),
                    ArrayLiteral([StringLiteral("array"),StringLiteral("!")])
                ]))),
            MethodDecl(Instance(),Id("check"),[],Block([
                VarDecl(Id("a"),ArrayType(2,ArrayType(1,StringType())),
                    ArrayLiteral([
                        ArrayLiteral([StringLiteral("This"),StringLiteral("is")]),
                        ArrayLiteral([StringLiteral("a"),StringLiteral("multi-dimensional")]),
                        ArrayLiteral([StringLiteral("array"),StringLiteral("!")])
                    ]))]))])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_334(self):
        input = """Class ArrayLit {
            Var a: Array[String, 2] = Array(New Rect(), New Rect());
            check() {
                Var a: Array[String, 2] = Array(New Rect(), New Rect());
            }
        }"""
        expect = str(Program([ClassDecl(Id("ArrayLit"),[
            AttributeDecl(Instance(),VarDecl(Id("a"),ArrayType(2,StringType()),
                ArrayLiteral([NewExpr(Id("Rect"),[]),NewExpr(Id("Rect"),[])]))),
            MethodDecl(Instance(),Id("check"),[],Block([
                VarDecl(Id("a"),ArrayType(2,StringType()),
                ArrayLiteral([NewExpr(Id("Rect"),[]),NewExpr(Id("Rect"),[])]))]))])]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_335(self):
        input = """Class Stmt {
            check() {
                Var a: Int;
                Var a: Int = 0;
                Var a: String = "Init";
                Var a: Object;
                Var a: Object = New Object();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[
            MethodDecl(Instance(),Id("check"),[],Block([
                VarDecl(Id("a"),IntType()),
                VarDecl(Id("a"),IntType(),IntLiteral(0)),
                VarDecl(Id("a"),StringType(),StringLiteral("Init")),
                VarDecl(Id("a"),ClassType(Id("Object")),NullLiteral()),
                VarDecl(Id("a"),ClassType(Id("Object")),NewExpr(Id("Object"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_336(self):
        input = """Class Stmt {
            check() {
                Val a: Int;
                Val a: Int = 0;
                Val a: String = "Init";
                Val a: Object;
                Val a: Object = New Object();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[
            MethodDecl(Instance(),Id("check"),[],Block([
                ConstDecl(Id("a"),IntType()),
                ConstDecl(Id("a"),IntType(),IntLiteral(0)),
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                ConstDecl(Id("a"),ClassType(Id("Object")),NullLiteral()),
                ConstDecl(Id("a"),ClassType(Id("Object")),NewExpr(Id("Object"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_337(self):
        input = """Class Stmt {
            check() {
                a = 1;
                a = Null;
                a = Self.instance;
                a = Something::$static;
                a = a.a();
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[
            MethodDecl(Instance(),Id("check"),[],Block([
                Assign(Id("a"),IntLiteral(1)),
                Assign(Id("a"),NullLiteral()),
                Assign(Id("a"),FieldAccess(SelfLiteral(),Id("instance"))),
                Assign(Id("a"),FieldAccess(Id("Something"),Id("$static"))),
                Assign(Id("a"),CallExpr(Id("a"),Id("a"),[]))]))])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_338(self):
        input = """Class Stmt {
            check() {
                a.a = a + 1_123.e-2;
                (1 + 2).a = Null;
                Null.value = Null;
                a.methodcall().a = True;
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            Assign(
                FieldAccess(Id("a"),Id("a")),
                BinaryOp("+",Id("a"),FloatLiteral(1123.e-2))),
            Assign(
                FieldAccess(BinaryOp("+",IntLiteral(1),IntLiteral(2)),Id("a")),
                NullLiteral()),
            Assign(
                FieldAccess(NullLiteral(),Id("value")),
                NullLiteral()),
            Assign(
                FieldAccess(CallExpr(Id("a"),Id("methodcall"),[]),Id("a")),
                BooleanLiteral(True))]))])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_339(self):
        input = """Class Stmt {
            check() {
                a[1] = New Variable();
                a[1]["index"] = something;
                a[1]["index"]["of"]["lhs"] = something;
                some.methodCall()[0] = something;
                Array(0, 1, 2)[1] = something;
            }
        }"""
        # TODO: This is not the way to represent multidimensional array ?????
        #Program([ClassDecl(Id(Stmt),[MethodDecl(Id(check),Instance,[],Block([AssignStmt(ArrayCell(Id(a),[IntLit(1)]),NewExpr(Id(Variable),[])),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[StringLit(index)]),Id(something)),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),StringLit(index),StringLit(of)]),[StringLit(lhs)]),Id(something)),AssignStmt(ArrayCell(CallExpr(Id(some),Id(methodCall),[]),[IntLit(0)]),Id(something)),AssignStmt(ArrayCell([IntLit(0),IntLit(1),IntLit(2)],[IntLit(1)]),Id(something))]))])])
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            Assign(ArrayCell(Id("a"),[IntLiteral(1)]),NewExpr(Id("Variable"),[])),
            Assign(
                ArrayCell(Id("a"),[IntLiteral(1),StringLiteral("index")]),
                Id("something")),
            Assign(
                ArrayCell(Id("a"),[IntLiteral(1),StringLiteral("index"),StringLiteral("of"),StringLiteral("lhs")]),
                Id("something")),
            Assign(
                ArrayCell(CallExpr(Id("some"),Id("methodCall"),[]),[IntLiteral(0)]),
                Id("something")),
            Assign(
                ArrayCell(ArrayLiteral([IntLiteral(0),IntLiteral(1),IntLiteral(2)]),[IntLiteral(1)]),
                Id("something"))]))])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_340(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    ## do something ##
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
                If(Id("condition"),Block([]))]))])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_341(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    a.a = a + 1_123.e-2;
                }
                Else {
                    a.a = a + 1_123.e-2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            If(Id("condition"),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]),
            Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]))]))])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_342(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    a.a = a + 1_123.e-2;
                }
                Elseif (!condition) {
                    Val a: String = "Init";
                    a = a + 2;
                }
                Else {
                    a.a = a + 1_123.e-2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            If(Id("condition"),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]),
            Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))])))]))])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_343(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    a.a = a + 1_123.e-2;
                }
                Elseif (!condition) {
                    Val a: String = "Init";
                    a = a + 2;
                }
                Elseif (!condition) {
                    Val a: String = "Init";
                    a = a + 2;
                }
                Elseif (!condition) {
                    Val a: String = "Init";
                    a = a + 2;
                }
                Else {
                    a.a = a + 1_123.e-2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            If(Id("condition"),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]),
            Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))])))))]))])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_344(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    a.a = a + 1_123.e-2;
                }
                Elseif (!condition) {
                    Val a: String = "Init";
                    a = a + 2;
                    If (a == a) {
                        ## do nothing ##
                    }
                    Else {
                        ## do something ##
                    }
                }
                Else {
                    a.a = a + 1_123.e-2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            If(Id("condition"),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                ConstDecl(Id("a"),StringType(),StringLiteral("Init")),
                Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),
                If(BinaryOp("==",Id("a"),Id("a")),Block([

                ]),Block([

                ]))]),
            Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))])))]))])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_345(self):
        input = """Class Stmt {
            check() {
                If (condition) {
                    a.a = a + 1_123.e-2;
                }
                Elseif (!condition) {
                    If (a == a) {
                        If (a != a) {
                            If (nestedIfs) {
                                Object.callAFunction();
                            }
                        }
                    }
                    Else {
                        ## do something ##
                    }
                }
                Else {
                    a.a = a + 1_123.e-2;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            If(Id("condition"),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))]),
            If(UnaryOp("!",Id("condition")),Block([
                If(BinaryOp("==",Id("a"),Id("a")),Block([
                    If(BinaryOp("!=",Id("a"),Id("a")),Block([
                        If(Id("nestedIfs"),Block([
                            CallStmt(Id("Object"),Id("callAFunction"),[])]))]))]),
                Block([]))
            ]),Block([
                Assign(FieldAccess(Id("a"),Id("a")),BinaryOp("+",Id("a"),FloatLiteral(1123.e-2)))])))]))])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_346(self):
        input = """Class Stmt {
            check() {
                Foreach (i In 1 .. 10) {
                    Out.printInt(i);
                }
            }
        }"""
        #Program([ClassDecl(Id(Stmt),[MethodDecl(Id(check),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),IntLit(1),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])
        #Program([ClassDecl(Id(Stmt),[MethodDecl(Id(check),Instance,[],Block([For(Id(i),IntLit(1),IntLit(10),Block([Call(Id(Out),Id(printInt),[Id(i)])])])]))])])
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                CallStmt(Id("Out"),Id("printInt"),[Id("i")])]),
                IntLiteral(1))
            ]))])]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_347(self):
        input = """Class Stmt {
            check() {
                Foreach (i In 10 .. 1) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            For(Id("i"),IntLiteral(10),IntLiteral(1),Block([
                CallStmt(Id("Out"),Id("printInt"),[Id("i")])]),
                IntLiteral(1)
            )]))])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_348(self):
        input = """Class Stmt {
            check() {
                Foreach (i In 0 .. array.size By 2) {
                    a.append(array[i]);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            For(Id("i"),IntLiteral(0),FieldAccess(Id("array"),Id("size")),Block([
                CallStmt(Id("a"),Id("append"),[ArrayCell(Id("array"),[Id("i")])])]),
                IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_349(self):
        input = """Class Stmt {
            check() {
                Foreach (i In 1 .. 10 By -2) {
                    If (i == 5) {
                        Out.print("Infinite loop maybe");
                    }
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id("Stmt"),[MethodDecl(Instance(),Id("check"),[],Block([
            For(Id("i"),IntLiteral(1),IntLiteral(10),Block([
                If(BinaryOp("==",Id("i"),IntLiteral(5)),Block([
                    CallStmt(Id("Out"),Id("print"),[StringLiteral("Infinite loop maybe")])]))]),
                UnaryOp("-",IntLiteral(2))
            )]))])]))
        self.assertTrue(TestAST.test(input,expect,349))

    # def test_350(self):
    #     input = """"""
    #     expect = str(Program([
    
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,350))

    # def test_351(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,351))

    # def test_352(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,352))

    # def test_353(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,353))

    # def test_354(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,354))

    # def test_355(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,355))

    # def test_356(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,356))

    # def test_357(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,357))

    # def test_358(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,358))

    # def test_359(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,359))

    # def test_360(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,360))

    # def test_361(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,361))

    # def test_362(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,362))

    # def test_363(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,363))

    # def test_364(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,364))

    # def test_365(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,365))

    # def test_366(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,366))

    # def test_367(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,367))

    # def test_368(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,368))

    # def test_369(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,369))

    # def test_370(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,370))

    # def test_371(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,371))

    # def test_372(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,372))

    # def test_373(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,373))

    # def test_374(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,374))

    # def test_375(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,375))

    # def test_376(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,376))

    # def test_377(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,377))

    # def test_378(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,378))

    # def test_379(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,379))

    # def test_380(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,380))

    # def test_381(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,381))

    # def test_382(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,382))

    # def test_383(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,383))

    # def test_384(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,384))

    # def test_385(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,385))

    # def test_386(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,386))

    # def test_387(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,387))

    # def test_388(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,388))

    # def test_389(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,389))

    # def test_390(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,390))

    # def test_391(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,391))

    # def test_392(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,392))

    # def test_393(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,393))

    # def test_394(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,394))

    # def test_395(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,395))

    # def test_396(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,396))

    # def test_397(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,397))

    # def test_398(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,398))

    # def test_399(self):
    #     input = """"""
    #     expect = str(Program([
    #
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,399))
