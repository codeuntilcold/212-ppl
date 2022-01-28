import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
# 1912184 - Thuong
    def test_simple_program(self):
        """Simple program"""
        input = """Class A {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """Class Program {
            Var a: Float = 1 + 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss } """
        input = """Class A {"""
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_4(self):
        input = """Class student {
            Val $countNum: Int = 0;
            $getName(){
                Return student::$countNum;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5(self):
        input = """Class Student {
            Constructor(name, class: String; age: Int){
                Self.name = name;
                Self.class = class;
                Self.age = age;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6(self):
        """Destructor has argument"""
        input = """Class Student {
            Destructor(a: Int){}
        }"""
        expect = "Error on line 2 col 23: a"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7(self):
        """Constructor has no argument"""
        input = """Class Student {
            Var $age: Int;
            Constructor() {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8(self):
        input = """Class Student {
            Var $name: String = "Thuong";
            $getName(){
                A.printName();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9(self):
        """Wrong argument in method decl"""
        input = """Class Student {
            getName(a,b){}
        }"""
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10(self):
        """Not have operator ++"""
        input = """Class Student {
            Val a, $b: Boolean = True, False;
            foo(){
                a++;
            }
        }"""
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11(self):
        """Lack expression after assign"""
        input = """Class Student {
            Val a, $b: Float =;
        }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12(self):
        """Miss } in method foo"""
        input = """Class Student {
            foo(a: Int){
        }"""
        expect = "Error on line 3 col 9: <EOF>"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13(self):
        """Class not have name"""
        input = """Class {
            foo(a: Int){}
        }"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14(self):
        """Static variable in method"""
        input = """Class A {
            foo(a: Int){
                Var $b: Float;
            }
        }"""
        expect = "Error on line 3 col 20: $b"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15(self):
        """Inheritance"""
        input = """Class A: B {
            foo(a: Int){}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16(self):
        """Multiple inheritance"""
        input = """Class A: B, C {
            foo(a: Int){}
        }"""
        expect = "Error on line 1 col 10: ,"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17(self):
        """Array type"""
        input = """Class A {
            Val a: Array[Int, 5] = Array();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18(self):
        """index operator"""
        input = """Class A {
            Var x: Int = -1;
            foo(){
                a[1+2][2] = 1;
                Return Self.x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19(self):
        """more complex index operator"""
        input = """Class A {
            foo(){
                a[1 + method.someMethod(1,3)][2 * a[12]] = 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20(self):
        """empty index operator"""
        input = """Class A {
            foo(){
                a[] = 1;
            }
        }"""
        expect = "Error on line 3 col 18: ]"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21(self):
        """Program not have any class"""
        input = """Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
        }"""
        expect = "Error on line 1 col 0: Val"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22(self):
        """argument in method separated by COMMA not SEMI"""
        input = """Class A {
            foo(a,b: Int, c: String){
                a = 1;
                b = a + c;
                Return;
            }
        }"""
        expect = "Error on line 2 col 24: ,"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23(self):
        """comment in program"""
        input = """Class A {
            foo(a,b: Int){
                ## This is comment ##
                ## This is
                block
                comment ##
                Var name: Float = 12.3;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24(self):
        """wrong identifier in attribute"""
        input = """Class Student {
            Var 12age: Int = 0;
        }"""
        expect = "Error on line 2 col 16: 12"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25(self):
        """wrong array type"""
        input = """Class School {
            Var name: Array;
        }"""
        expect = "Error on line 2 col 27: ;"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26(self):
        """wrong array element separator"""
        input = """Class School {
            Var name: Array[String, 2] = Array("BK"; "HCM");
        }"""
        expect = "Error on line 2 col 51: ;"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27(self):
        """class type"""
        input = """Class School {
            Var name: Array[String, 2] = Array("BK", "HCM");
            Var student: Student = New Student();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28(self):
        """expr less than attribute"""
        input = """Class School {
            Var a, b, c: Int = 1, 2;
        }"""
        expect = "Error on line 2 col 35: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29(self):
        """expr more than attribute"""
        input = """Class School {
            Var a: Int = 1, 2;
        }"""
        expect = "Error on line 2 col 26: ,"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30(self):
        """balance in variable declare"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1;
            }
        }"""
        expect = "Error on line 3 col 33: ;"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a: Int = 1 + 2 * 3 / 4 % 5 - -2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Boolean = !True && False, True || a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1, 2;
                a = A.getNum();
                b = A.$show();
            }
        }"""
        expect = "Error on line 5 col 22: $show"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1, 2;
                a = New X(y).attr;
                b = New X().get();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1, 2;
                a = Student[0].attr;
            }
        }"""
        expect = "Error on line 4 col 30: ."
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1, 2;
                a = (Student[0]).attr;
                b = A.get()[1];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        """test expression"""
        input = """Class School {
            foo() {
                Var a, b: Int = 1, 2;
                a = A[c::$getA(a) == b[1][c::$name]];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        """test expression"""
        input = """Class School {
            foo(a: Int) {
                Var a, b: Int = 1, 2;
                Shape::$get(1+1::$attr);
            }
        }"""
        expect = "Error on line 4 col 31: ::"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        """test expression"""
        input = """Class School {
            foo(a: Int) {
                Var a, b: Int = 1/a.name[sth[A.attr] * !2], "BK" +. "HCM";
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        """test expression"""
        input = """Class School {
            foo(a: Int) {
                Var attr: Float = Shape.getY().attr;
                Var a: Int = Shape::getX();
            }
        }"""
        expect = "Error on line 4 col 36: getX"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        """static id in argument of method"""
        input = """Class School {
            foo(a, $b: Int) {}
        }"""
        expect = "Error on line 2 col 19: $b"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        """test statement"""
        input = """Class Point {
            foo(x, y: Int) {
                Var a: Int = "a"[1];
                a = 1 + 2 * !A.getX(x, y);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        """test statement"""
        input = """Class Point {
            Var $a: Int;
            foo(x, y: Int) {
                Point::$a = 1 + 2 * !A.getX(x, y);
                arr[2][3] = New P(x).Y();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        """test statement"""
        input = """Class Point {
            Var $a: Int;
            foo(x, y: Int) {
                x + 5 = 10;
            }
        }"""
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        """test statement"""
        input = """Class Point {
            Var $a: Int;
            foo(x, y: Int) {
                Point::$a.X = y;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        """test statement"""
        input = """Class Point {
            foo(x, y: Int) {
                If (x + y * 3 - 0) {
                    a = 1;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        """lack expr in Elseif"""
        input = """Class Point {
            foo(x, y: Int) {
                If (x + y * 3 - 0) {
                    a = 1;
                } Elseif {
                    y = a + x;
                }
            }
        }"""
        expect = "Error on line 5 col 25: {"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        """Else statement has expr"""
        input = """Class Point {
            foo(x, y: Int) {
                If (x + y * 3 - 0) {
                    a = 1;
                } Elseif(A[0] == True || !stu.attr) {
                    y = a + x;
                } Else(1 + 2) {}
            }
        }"""
        expect = "Error on line 7 col 22: ("
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49(self):
        """two Else statement"""
        input = """Class Point {
            foo(x, y: Int) {
                If (x + y * 3 - 0) {
                    a = 1;
                } Elseif(a == b) {
                    If (1 + 2) {}
                } Else{}
                Else{}
            }
        }"""
        expect = "Error on line 8 col 16: Else"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        """multiple Elseif statement"""
        input = """Class Point {
            foo(x, y: Int) {
                If (x + y * 3 - 0) {} 
                Elseif(a == b) {
                    If (1 + 2) {}
                } Elseif(Point::$a[123][234]){}
                Else{}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        """For In statement"""
        input = """Class Grade {
            getScore() {
                Foreach(i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                    Out.printInt(arr[x]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        """For In statement not scala var"""
        input = """Class Grade {
            getScore() {
                Foreach(s[1] In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Error on line 3 col 25: ["
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        """For In statement"""
        input = """Class Grade {
            getScore() {
                Foreach(Grade::$a.attr In 1 .. 50 + 1 - a[1 + A.foo(a,b)] By 2) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        """For In statement lack expr after By"""
        input = """Class Grade {
            getScore() {
                Foreach(Grade::$a.attr In 1 .. 50 By ) {
                    Out.printInt(i);
                }
            }
        }"""
        expect = "Error on line 3 col 53: )"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        """For In statement"""
        input = """Class Grade {
            getScore() {
                Foreach(i In 1 .. 50) {
                    Foreach(j In i + 1 .. New X().attr){}
                    Var a: String = "BK";
                    Self.a = "HCM";
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56(self):
        """Self expr"""
        input = """Class Grade {
            foo(){
                a = Self.X + Self.Y[1];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57(self):
        """Self expr"""
        input = """Class Grade {
            foo(){
                a = Self::$x + Self::$y();
            }
        }"""
        expect = "Error on line 3 col 24: ::"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58(self):
        """Break statement"""
        input = """Class Grade {
            foo(){
                Foreach(i In 1 .. 50 By 1) {
                    If (i % 2 == 0) {
                        Break;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59(self):
        """Continue statement"""
        input = """Class Grade {
            foo(){
                Foreach(i In 1 .. 50 By 1) {
                    If (i % 2 == 0) {
                        Continue;
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        """lack SEMI in Continue statement"""
        input = """Class Grade {
            foo(){
                Break;
                Continue
            }
        }"""
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61(self):
        """Return statement"""
        input = """Class Grade {
            Var a: Array[Int, 1];
            foo(){
                Return a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        """Return statement"""
        input = """Class Grade {
            Var a: Array[Int, 1];
            foo(x, y: Array[Int, 2]){
                Return a[1] + x[1]*y[x[1] + A.get(a[1])];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        """Return statement outside function"""
        input = """Class Grade {
            Var a: Int = 1 + 2;
            foo(x, y: Float){
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        """Return statement outside function"""
        input = """Class Grade {
            Var a: Int = 1 + 2;
            foo(x, y: Float){
                x = y + 11.e00;
                Return Self.a;
            }
            Return Grade.foo(1.2, .1e1);
        }"""
        expect = "Error on line 7 col 12: Return"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        """more complex Return statement"""
        input = """Class Grade {
            Var a: Int = 1 + 2;
            foo(x, y: String){
                If(x ==. y) {
                    Return Self.a;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        """Method invocation statement"""
        input = """Class Grade {
            foo(name: String){
                Student.getGrade(name);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        """Method invocation statement"""
        input = """Class Grade {
            foo(name: String){
                Student::$getGrade(name);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        """Method invocation statement"""
        input = """Class Grade {
            getGrade(name: String){
                Return grade;
            }
            foo(name: String){
                Grade.getGrade(name);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        """Method invocation statement"""
        input = """Class Grade {
            foo(name: String){
                New Grade().getGrade(name);
                Student.name.getName(arr[1] * 2);
                Room::$print();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        """complex statement"""
        input = """Class Grade {
            Var x, $y: Boolean = True, False;
            foo(name: String){
                If((name +. "HCM") ==. "BK HCM"){
                    x = x + 1;
                    Grade::$y = Student.show(name, Self.x);
                }
                Foreach(i In 1 .. 10 By (School::$getX()).attr[1] + 1){
                    A.foo(name);
                    Self.foo(name);
                }
                Return x + Grade::$y == True;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))


    def test_71(self):
        """test size in array"""
        input = """Class Shape {
            Var a: Array[Int, 0];
        }"""
        expect = "Error on line 2 col 30: 0"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        """test size in array"""
        input = """Class Shape {
            Var a: Array[Int, 10.e0];
        }"""
        expect = "Error on line 2 col 30: 10.e0"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73(self):
        """test size in array"""
        input = """Class Shape {
            Var a, b: Array[Int, 3] = Array(1,2,3);
        }"""
        expect = "Error on line 2 col 50: ;"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_74(self):
        """test int"""
        input = """Class Shape {
            Var a, b: Int = 0x12AF, 0X_123;
        }"""
        expect = "Error on line 2 col 37: X_123"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75(self):
        """Class name is static"""
        input = """Class $Shape {}"""
        expect = "Error on line 1 col 6: $Shape"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_76(self):
        """test mixed"""
        input = """Class Point {
            Foo(a, b: Int) {
                Return a + b;
            }
            Foo(a,b:Float) {
                Return a + b --a - c % 2 / 1 * a;
            }
            Foo(a,b:Boolean) {
                Return a || !b && !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(c == f);
            }
            Add(a, abcd: String) {
                Return a ==. b ==. (c ==. d ==. ("abc" ==. fffffffffffffff));
            }
        }"""
        expect = "Error on line 12 col 31: ==."
        self.assertTrue(TestParser.test(input,expect,276))
    def test_77(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_78(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_79(self):
        """test mixed"""
        input = """Class Point {
            Var a, $b: A = New A(value1, value2), New A();
            Function(x: X) {
                Var c: Boolean = True;
                If(c == True){
                    c = !c;
                    Break;
                } Elseif(Point::$b + a --x.getX()){
                    Return;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_80(self):
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
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_81(self):
        """test mixed"""
        input = """Class Shape {
            Val immutableAttribute: Rect = New Rect();
            getNumOfShape(){
                If(immutableAttribute != Null){
                    Return immutableAttribute.num;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_82(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Array[Array[Int, 3], 2];
            getShape(){
                a[1][1] = 1;
                If(a == 1){
                    If(a != 1){
                        Var x: Float = 1_23.4;
                    } Elseif(3 + 4 && Null){
                        Self.a = Array(Array(1,2,3), Array(4,5,6));
                    }
                } Else {
                    Return Null;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_83(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Array[Array[Int, 3], 2];
            getShape(x: Array[Int, 2]){
                a = a[x];
                func(){
                    Shape.getShape(x);
                }
            }
        }"""
        expect = "Error on line 5 col 20: ("
        self.assertTrue(TestParser.test(input,expect,283))
    def test_84(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Array[Array[Int, 3], 2];
            getShape(x: Rect){
                x = New Rect(point, a);
                Point::$draw(x);
                {
                    getSomething();
                    a = 1;
                }
            }
        }"""
        expect = "Error on line 6 col 16: {"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_85(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Array[Array[Int, 3], 2];
            getShape(x: Int){
                Return x;
            }
            getA(){
                Self.getShape(a);
                Elseif(!a ==. -a){

                }
            }
        }"""
        expect = "Error on line 7 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_86(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Point = New Point();
            getPoint(x: Int){
                a = New Point().get();
                Foreach(i In 1..100 By 1.e11 + True){}
            }
        }"""
        expect = "Error on line 5 col 32: 100"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_87(self):
        """test mixed"""
        input = """Class Shape {
            Val a: Point = New;
            getPoint(x: Int){}
        }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_88(self):
        """test mixed"""
        input = """Class Shape {
            Val a: String;
            getPoint(x: Int){
                Var b: String = a +. "HCM";
                If {
                    Return;
                }
            }
        }"""
        expect = "Error on line 5 col 19: {"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_89(self):
        """test mixed"""
        input = """Class Shape {
            Val a: String;
            getPoint(x: Int){
                Var b: String = (a ==. "HCM") && !!!!a;
                X[[1][2]] = 1;
            }
        }"""
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.test(input,expect,289))
    def test_90(self):
        """test mixed"""
        input = """Class Shape {
            Val a, b: Boolean, Int = True, 1;
            getPoint(x: Int){
                Var b: String = (a ==. "HCM") && !!!!a;
            }
        }"""
        expect = "Error on line 2 col 29: ,"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_91(self):
        """test mixed"""
        input = """Class Shape: Point {
            Val a, b: Boolean = True, False;
            getPoint(x: Int){
                Point::showPoint();
            }
        }"""
        expect = "Error on line 4 col 23: showPoint"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_92(self):
        """test mixed"""
        input = """Class Shape {
            Val a, b: Boolean = True, False;
            getPoint(){
                Var x: Array[Array[Int, 0], 1];
                Break;
                Continue;
            }
        }"""
        expect = "Error on line 4 col 40: 0"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_93(self):
        """test mixed"""
        input = """Class Shape {
            Val a, b: Array[Float, 1_23.e1];
        }"""
        expect = "Error on line 2 col 35: 123.e1"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94(self):
        """test mixed"""
        input = """Class Shape {
            Val a, b: Student;
            $foo(){
                New X() = a;
            }
        }"""
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95(self):
        """test mixed"""
        input = """Class Shape {
            Val a, b: Student;
            $foo(){
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96(self):
        """test mixed"""
        input = """Class Shape {
            Constructor(x, y: Int){
                Self.x = x;
                Self.y = y;
            }
            Destructor(){}
            Def(){
                Return;
            }
            Return;
        }"""
        expect = "Error on line 10 col 12: Return"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_97(self):
        """test mixed"""
        input = """Class Shape {
            Var a: String = "Hello, '" John ";
            Var b: Array[Int, 1] = Array(Array(1), Array(1,2));
            Array(){};
        }"""
        expect = "Error on line 4 col 12: Array"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_98(self):
        """test mixed"""
        input = """Class Shape {
            func(_: Int; __: Float){
                Val x: Int = 1_23_456;
                Var y: Float = 1_23.;
                Var z: Boolean = -!True;
            }
        }"""
        expect = "Error on line 5 col 34: !"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_99(self):
        """test mixed"""
        input = """Class Shape {
            func(x,y,z: Int){
                Val x, y: Int = 111 + Array(1,2) / New x(), 1;
                x = y = z = 1;
                Return;
            }
        }"""
        expect = "Error on line 4 col 22: ="
        self.assertTrue(TestParser.test(input,expect,299))
    def test_100(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

    