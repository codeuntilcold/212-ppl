from distutils.log import error
import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """Class A {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """Class A {"""
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """Class A {
            Var x: Int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_204(self):
        input = """Class A {{}}
        """
        expect = "Error on line 1 col 9: {"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_205(self):
        input = """Class A {
            VAR x: Int;
        }"""
        expect = "Error on line 2 col 16: x"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_206(self):
        input = """Class A {
            getArea() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_207(self):
        input = """Class A {
            $__private() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_208(self):
        input = """Class A {
            9slide () {}
        }"""
        expect = "Error on line 2 col 12: 9"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_209(self):
        input = """Var x: Int;"""
        expect = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_210(self):
        input = """Class Int {

        }"""
        expect = "Error on line 1 col 6: Int"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_211(self):
        input = """Class INT {
            Var x: Int = 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_212(self):
        input = """Class Point {
            Var x, y: Int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_213(self):
        input = """Class Point {
            Var x, y: Int = 0;
        }"""
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_214(self):
        input = """Class Point {
            Var x, y: Int = 0, 0.5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_215(self):
        input = """Class Point {
            Var x, y: Int;

            Constructor() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_216(self):
        input = """Class Point {
            Var x, y: Int;

            Constructor(x: Int; y: Int) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_217(self):
        input = """Class Point {
            Var x, y: Int;

            Constructor(x: Int, y: Int) {}
        }"""
        expect = "Error on line 4 col 30: ,"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_218(self):
        input = """Class Point {
            Var x, y: Int;

            Constructor(x: Int; y: Int) {}

            Destructor(x: Int; y: Int) {}
        }"""
        expect = "Error on line 6 col 23: x"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_219(self):
        input = """Class Point {
            Val $x, y: Int;

            Constructor(x: Int; y: Int) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_220(self):
        input = """Class Point {
            Var x, y: Int = 0.5, 0.5*2;

            Constructor(x: Int; y: Int) {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_221(self):
        input = """Class Point {
            Var x, y: Int;

            Constructor(x: Int; y: Int) {
                getPoint() {}   ## Can't have method declaration ##
                Return x;
            }
        }"""
        expect = "Error on line 5 col 24: ("
        self.assertTrue(TestParser.test(input,expect,221))

    def test_222(self):
        input = """Class Point {
            Var x, y: Int;

            ## 
                Valid
                syntaxically speaking
            ##
            Constructor(x: Int; y: Int) {
                getPoint();
                Return x;
            }
        }"""
        expect = "Error on line 9 col 24: ("
        self.assertTrue(TestParser.test(input,expect,222))

    def test_223(self):
        input = """Class ValidIdentifier {
            Var z, _z, z92c, $92z, $identifier: Float;    
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_224(self):
        input = """Class IntLit {
            Var oct: Int = 00;
            Var hex: Int = 0x1572;
            Var bin: Int = 0B10101;
            Var dec: Int = 17_258;
            Var err_underscore: Int = 17__228;
        }"""
        expect = "Error on line 6 col 40: __228"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_225(self):
        input = """Class StringLit {
            Var name: String = "Darwin";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_226(self):
        input = """Class StringLit {
            Var name: String = "Darwin
            and his creation";
        }"""
        expect = "Darwin"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_227(self):
        input = """Class StringLit {
            Var name: String = "Darwin \e and his illegal escape";
        }"""
        expect = "Darwin \e"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_228(self):
        input = """Class StringLit {
            Var name: String = "Charles '"the GOAT'" Darwin";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_229(self):
        input = """Class ArrayLit {
            Var $theArray : Array [Int, 5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))

    def test_230(self):
        input = """Class ArrayLit {
            Var $theArray : Array [Int, 5] = Array (1, 2, 3, 4, 5);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_231(self):
        input = """Class ArrayLit {
            Var $theArray : Array [ Array[Int, 3], 5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_232(self):
        input = """
        ## Number of nested array is checked ?????? ## 
        
        Class ArrayLit {
            Var $theArray : Array [ Array[String, 3], 5]
            = Array (
                Array ("Volvo", "22", "18"),
                Array ("Saab", "5", "2"),
                Array ("Land Rover", "17")
            );
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_233(self):
        input = """Class ArrayLit {
            Var $theArray : Array[Array[Array[Int, 1], 1], 1]
            = Array (
                Array (
                    Array (0)
                )
            );
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_234(self):
        input = """Class Ops {
            isThisValid() {
                Var x: Boolean = 1 || 2;
                Var y: Boolean = False;

                z = !x && y;
                
                z = x +. y;  ## No type checking and stuff ##
                z = x + y;

                z = x ==. y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_235(self):
        input = """Class Ops {
            isThisValid(x: Point; r: Int) {

            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_236(self):
        input = """Class Ops {
            isThisValid(x: Point; r: Int) {
                newX = x.translateX(r);
                newY = y.translateY(r);

                Return New Point(newX, newY);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_237(self):
        input = """Class Ops {
            isThisValid(x: Point; r: Int) {
                Self.newPoint = New Point(x.coords.translate(r));

                Return Self.newPoint;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_238(self):
        input = """Class Ops {
            Constructor(x: Point; r: Int) {
                (Self.point[0]).x = x;
                (Self.point[0]).r = r;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_239(self):
        input = """Class Ops {
            Constructor(x: Point; r: Int) {
                Self.x, Self.r = x, r;
            }
        }"""
        expect = "Error on line 3 col 22: ,"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_240(self):
        input = """Class Ops {
            draw(x: Point; r: Int) {
                Circle.$draw(x, r);
            }
        }"""
        expect = "Error on line 3 col 23: $draw"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_241(self):
        input = """Class Ops {
            arrayAccess() {
                x.member[0] = not_init;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_242(self):
        input = """Class Ops {
            multiDimArr() {
                x[0][1] = x.singleton();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_243(self):
        input = """Class Ops {
            multiDimArr() {
                x[0][ x.length - 1 ] = x.singleton();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_244(self):
        input = """Class Ops {
            static() {
                Return Array(1,2,3,4,5).last();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_245(self):
        input = """Class Ops {
            static() {
                Return aCircle.$radius;
            }
        }"""
        expect = "Error on line 3 col 31: $radius"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_246(self):
        input = """Class Ops {
            static() {
                Return school::$numOfClass;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_247(self):
        input = """Class Ops {
            static() {
                Return Array(1,2,3,4,5)::$totalArrayCreated;
            }
        }"""
        expect = "Error on line 3 col 39: ::"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_248(self):
        input = """Class Ops {
            objectCreation() {
                Return New Square(point).defaultArea();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_249(self):
        input = """Class Ops {
            objectCreation() {
                Return (x[index]).value;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_250(self):
        input = """Class Ops {
            $objectCreation() {
                Return New Object()::$totalObject;
            }
        }"""
        expect = "Error on line 3 col 35: ::"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_251(self):
        input = """Class Statements {
            Destructor() {
                x[x.length - 1] = "Value of last element";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_252(self):
        input = """Class Statements {
            Destructor() {
                employee.name = "Nam";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_253(self):
        input = """Class Statements {
            Destructor() {
                !false = True;
            }
        }"""
        expect = "Error on line 3 col 16: !"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_254(self):
        input = """Class Statements {
            Destructor() {
                x + 5 = 10;
            }
        }"""
        expect = "Error on line 3 col 18: +"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_255(self):
        input = """Class Statements {
            ifStatement() {
                If (Null) {
                    Out.print("Cool");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_256(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) print("Cool");
            }
        }"""
        expect = "Error on line 3 col 28: print"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_257(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif {
                    Out.print("Not cool\\n");
                }
            }
        }"""
        expect = "Error on line 6 col 23: {"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_258(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif (x ==. "Kimi no Na wa?") {
                    Out.print("Not cool\\n");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_259(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif (x == 1) {
                    Out.print("Not cool\\n");
                }
                Elseif {
                    Return 0;
                }
            }
        }"""
        expect = "Error on line 9 col 23: {"
        self.assertTrue(TestParser.test(input,expect,259))

    def test_260(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif (x==1) {
                    Out.print("Not cool\\n");
                }
                Else {
                    Return nothing;
                }
                Elseif {

                }
            }
        }"""
        expect = "Error on line 12 col 16: Elseif"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_261(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif (x == 1) {
                    Out.print("Not cool\\n");
                }
                Else {} Else {}
            }
        }"""
        expect = "Error on line 9 col 24: Else"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_262(self):
        input = """Class Statements {
            ifStatement() {
                If (x == 0) {
                    Out.print("Cool");
                }
                Elseif (x = 2) {
                    Out.print("Not cool\\n");
                }
            }
        }"""
        expect = "Error on line 6 col 26: ="
        self.assertTrue(TestParser.test(input,expect,262))

    def test_263(self):
        input = """Class Statements {
            forInStatement() {
                For (i = 1; i < 10; i++) {}
            }
        }"""
        expect = "Error on line 3 col 20: ("
        self.assertTrue(TestParser.test(input,expect,263))

    def test_264(self):
        input = """Class Statements {
            forInStatement() {
                For (index In 1 .. 10) {

                }
            }
        }"""
        expect = "Error on line 3 col 20: ("
        self.assertTrue(TestParser.test(input,expect,264))

    def test_265(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (index In arr.start() .. arr.end()) {
                    Out.print(arr[index]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

    def test_266(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (index In 1 .. 10 By -1) {
                    Suite::$printInt(index);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def test_267(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (class.var In 1 .. 10 By -1) {
                    Suite.printInt(index);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_268(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (class::$var In 5 .. 2) {
                    Suite.printInt(index);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_269(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (xr In 5 .. 2) {
                    Out.printInt(arr[x]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_270(self):
        input = """Class Statements {
            forInStatement() {
                Foreach (class::$var In 5 .. 2) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_271(self):
        input = """Class Statements {
            forInStatement() {
                If (i == 5) {
                    Break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def test_272(self):
        input = """Class Statements {
            forInStatement() {
                Continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_273(self):
        input = """Class Statements {
            forInStatement() {
                Return Null;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_274(self):
        input = """Class Statements {
            forInStatement() {
                Return x.getX().toCm().plus(5);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_275(self):
        input = """Class Statements {
            forInStatement() {
                Return (point[0]).getX().toMetrics()[5];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_276(self):
        input = """Class Statements {
            forInStatement() {
                Return Self.$static;
            }
        }"""
        expect = "Error on line 3 col 28: $static"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_277(self):
        input = """Class Statements {
            methodInvocation() {
                Return expr.newExpr();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_278(self):
        input = """Class Statements {
            methodInvocation() {
                {
                    this.willbelocal();
                    and = this.will() + run::$flawlessly;
                    hic.maybe().maybenot();
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_279(self):
        input = """Class Expr {
            main() {
                expr1 = a + b;
                expr2 = a * b;
                expr3 = scalar.var + not.scalar.var;
                expr4 = Lib.random() * 3.14 + probability;
                expr5 = New Point() + New Point()[5];
                expr7 = Null;
                expr6 = arraymem[5] + (arraymem[5])::$highestofall;
            }
        }"""
        expect = "Error on line 9 col 51: ::"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_280(self):
        input = """Class Expr {
            main() {
                expr = arraymem[5] + AllConst::$highestofall;
                expr1 = awesomeNumber + $notSoAwesome;
                expr2 = Self.member + $selfMemberMax();
                expr3 = -15;
                expr4 = .15E15 + 10E11;
                expr5 = _1234 + 0x0;
            }
        }"""
        expect = "Error on line 4 col 40: $notSoAwesome"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_281(self):
        input = """Class Expr {
            main() {
                a.very.nested.scalar.var = another.very.nested.scalar.var;
                a::$staticvar = another::$staticmethod();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_282(self):
        input = """Class Expr {
            main() {
                Foreach (x In 4 . r . g . b .. 2) {
                    Out.printInt(arr[x]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_283(self):
        input = """Class Expr {
            main() {
                Return Self + Self;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_284(self):
        input = """Class Expr {
            main() {
                Return Self.instance_attr + Expr::$static_attr;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_285(self):
        input = """Class Expr {
            main() {
                Return Self::$smth;
            }
        }"""
        expect = "Error on line 3 col 27: ::"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_286(self):
        input = """Class Expr {
            main() {
                Return Expr.$static;
            }
        }"""
        expect = "Error on line 3 col 28: $static"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_287(self):
        input = """Class Expr {
            main() {
                Return Null.attr;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_288(self):
        input = """Class Expr {
            main() {
                Return (1 + 2).map(x * x);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_289(self):
        input = """Class Arrtest {
            Var $a: Array[Boolean, 10] = Array(true, True);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def test_290(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(1 + 2, static::$mem);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_291(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(static::$var, $var);
        }"""
        expect = "Error on line 2 col 60: $var"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_292(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(normal.val, not.$normalval);
        }"""
        expect = "Error on line 2 col 62: $normalval"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_293(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(New Point(), True);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_294(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(true, True);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_295(self):
        input = """Class Arrtest {
            Var a: Array[Boolean, 10] = Array(True, True);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_296(self):
        input = """Class Arrtest {
            Var a: Int = Array();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_297(self):
        input = """Class Arrtest {
            Var a: Array[Point, 1];
        }"""
        expect = "Error on line 2 col 25: Point"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_298(self):
        input = """Class Arrtest { Var x: Array[Int, 0x0]; }"""
        expect = "Error on line 1 col 34: 0x0"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_299(self):
        input = """Class ThuongTest {
            test() {
                Var x: Int = _123; ## as identifiers ##
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def test_300(self):
        input = """
        ## Student ID : 1910101
        ##
        Class Shape {
            Val $numOfShape, _nVertex: Int = 0, 5 + 2;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            Constructor(len: Int; wid: Int) {
                Self.length = len;
                Self.width = wid;
            }

            Destructor() {}

            $getNumOfShape() {
                Return Shape::$numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

