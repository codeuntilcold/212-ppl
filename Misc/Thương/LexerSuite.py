import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

# 1912184 - Thuong
    # def test_problem_1(self):
    #     self.assertTrue(TestLexer.test(""" "abc\\"  ""","""Unclosed String: she \'\"  """,101))
    # def test_problem_2(self):
    #     self.assertTrue(TestLexer.test(""" "something \p something""","""Illegal Escape In String: something \p""",102))
    # def test_problem_3(self):
    #     self.assertTrue(TestLexer.test(""" "something something \p  ""","""Illegal Escape In String: something something \p""",103))
    # def test_problem_4(self):
    #     self.assertTrue(TestLexer.test(""" "something ' something"  ""","""something ' something,<EOF>""",104))
    # def test_problem_5(self):
    #     self.assertTrue(TestLexer.test(""" \"she \'\"""","""Unclosed String: she \'\"""",105))
    # def test_problem_6(self):
    #     self.assertTrue(TestLexer.test(""" "something \' something"  ""","""something ' something,<EOF>""",106))
    # def test_10(self):
    #     self.assertTrue(TestLexer.test("StringInt","String,Int,<EOF>",101))
    def test_lower_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>",101))
    def test_lower_upper_identifier(self):
        self.assertTrue(TestLexer.test("abcABc", "abcABc,<EOF>",102))
    def test_id_1(self):
        self.assertTrue(TestLexer.test("abc1_d", "abc1_d,<EOF>",103))
    def test_id_2(self):
        self.assertTrue(TestLexer.test("ab?12", "ab,Error Token ?",104))
    def test_id_3(self):
        self.assertTrue(TestLexer.test("$ab12", "$ab12,<EOF>",105))
    def test_id_4(self):
        self.assertTrue(TestLexer.test("$$_12ab", "Error Token $",106))
    def test_id_5(self):
        self.assertTrue(TestLexer.test("count num123", "count,num123,<EOF>",107))
    def test_id_6(self):
        self.assertTrue(TestLexer.test("my_name_is 19_k19", "my_name_is,19,_k19,<EOF>",108))
    def test_id_7(self):
        self.assertTrue(TestLexer.test("_number1", "_number1,<EOF>",109))
    def test_id_8(self):
        self.assertTrue(TestLexer.test("$_____a _____init_____", "$_____a,_____init_____,<EOF>",110))

    def test_mixed_id_1(self):
        """test mixed identifier"""
        self.assertTrue(TestLexer.test("HELLO X_men", "HELLO,X_men,<EOF>",111))
    def test_mixed_id_2(self):
        self.assertTrue(TestLexer.test("_ABc123", "_ABc123,<EOF>",112))
    def test_mixed_id_3(self):
        self.assertTrue(TestLexer.test("_$123Num", "_,$123Num,<EOF>",113))
    def test_mixed_id_4(self):
        self.assertTrue(TestLexer.test("$Hello__12$", "$Hello__12,Error Token $",114))
    def test_mixed_id_5(self):
        self.assertTrue(TestLexer.test("_HeLLo_12_$Abc", "_HeLLo_12_,$Abc,<EOF>",115))
    
    def test_int_lit_1(self):
        """test integer literal"""
        self.assertTrue(TestLexer.test("1234 000","1234,00,0,<EOF>",116))
    def test_int_lit_2(self):
        self.assertTrue(TestLexer.test("00123 0x22 0XAF14 0b1101","00,123,0x22,0XAF14,0b1101,<EOF>",117))
    def test_int_lit_3(self):
        self.assertTrue(TestLexer.test("0x0123","0x0,123,<EOF>",118))
    def test_int_lit_4(self):
        self.assertTrue(TestLexer.test("012488","0124,88,<EOF>",119))
    def test_int_lit_5(self):
        self.assertTrue(TestLexer.test("0X23DGH","0X23D,GH,<EOF>",120))
    def test_int_lit_6(self):
        self.assertTrue(TestLexer.test("12_143_2 012_344 0xAB_23 0B1_101","121432,012344,0xAB23,0B1101,<EOF>",121))
    def test_int_lit_7(self):
        self.assertTrue(TestLexer.test("12__12","12,__12,<EOF>",122))
    def test_int_lit_8(self):
        self.assertTrue(TestLexer.test("0b_110 0123_","0,b_110,0123,_,<EOF>",123))
    def test_int_lit_9(self):
        self.assertTrue(TestLexer.test("000_000_000","00,0,_000_000,<EOF>",124))
    def test_int_lit_10(self):
        self.assertTrue(TestLexer.test("0B0x002468","0B0,x002468,<EOF>",125))
    
    def test_float_lit_1(self):
        """test float literal"""
        self.assertTrue(TestLexer.test("12.3e10","12.3e10,<EOF>",126))
    def test_float_lit_2(self):
        self.assertTrue(TestLexer.test("12.0000 12E-10","12.0000,12E-10,<EOF>",127))
    def test_float_lit_3(self):
        self.assertTrue(TestLexer.test("000.0000","00,0.0000,<EOF>",128))
    def test_float_lit_4(self):
        self.assertTrue(TestLexer.test("1200E0","1200E0,<EOF>",129))
    def test_float_lit_5(self):
        self.assertTrue(TestLexer.test("12.00012","12.00012,<EOF>",130))
    def test_float_lit_6(self):
        self.assertTrue(TestLexer.test("12.","12.,<EOF>",131))
    def test_float_lit_7(self):
        self.assertTrue(TestLexer.test(".e123",".e123,<EOF>",132))
    def test_float_lit_8(self):
        self.assertTrue(TestLexer.test("12.000e+000","12.000e+000,<EOF>",133))
    def test_float_lit_9(self):
        self.assertTrue(TestLexer.test("12.a123","12.,a123,<EOF>",134))
    def test_float_lit_10(self):
        self.assertTrue(TestLexer.test("120.e$12","120.,e,$12,<EOF>",135))
    
    def test_boolean_lit_1(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.test("Var a: Boolean = True","Var,a,:,Boolean,=,True,<EOF>",136))
    def test_boolean_lit_2(self):
        self.assertTrue(TestLexer.test("Var a: Boolean = False","Var,a,:,Boolean,=,False,<EOF>",137))
    def test_boolean_lit_3(self):
        self.assertTrue(TestLexer.test("Var a: Boolean = false","Var,a,:,Boolean,=,false,<EOF>",138))
    def test_boolean_lit_4(self):
        self.assertTrue(TestLexer.test("Var a: Boolean = tr@e","Var,a,:,Boolean,=,tr,Error Token @",139))
    
    def test_string_lit_1(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "Hello honey" ""","Hello honey,<EOF>",140))
    def test_string_lit_2(self):
        self.assertTrue(TestLexer.test(""" "Hello honey \\t \\n" ""","Hello honey \\t \\n,<EOF>",141))
    def test_string_lit_3(self):
        self.assertTrue(TestLexer.test(""" "Hello honey '" hi" ""","""Hello honey '" hi,<EOF>""",142))
    def test_string_lit_4(self):
        self.assertTrue(TestLexer.test(""" "Hello honey \\' hi" ""","""Hello honey \\' hi,<EOF>""",143))
    def test_string_lit_5(self):
        self.assertTrue(TestLexer.test(""" "Hello honey ' hi" ""","""Hello honey ' hi,<EOF>""",144))
    def test_string_lit_6(self):
        self.assertTrue(TestLexer.test(""" "Hello honey \\\\c" ""","""Hello honey \\\\c,<EOF>""",145))
    def test_string_lit_7(self):
        self.assertTrue(TestLexer.test(""" 'Hello honey' ""","""Error Token '""",146))
    def test_string_lit_8(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test(""" "Hello honey \\h" ""","Illegal Escape In String: Hello honey \\h",147))
    def test_string_lit_9(self):
        self.assertTrue(TestLexer.test(""" "Hello honey \ " ""","Illegal Escape In String: Hello honey \ ",148))
    def test_string_lit_10(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test(""" "Hello \n honey" ""","""Unclosed String: Hello """,149))
    def test_string_lit_11(self):
        self.assertTrue(TestLexer.test(""" "Hello honey" "hi ""","""Hello honey,Unclosed String: hi """,150))
    
    def test_comment_1(self):
        """test comment"""
        self.assertTrue(TestLexer.test("##Hello honey##","<EOF>",151))
    def test_comment_2(self):
        self.assertTrue(TestLexer.test("## Hello honey \n How are you ##","<EOF>",152))
    def test_comment_3(self):
        self.assertTrue(TestLexer.test("### Hello honey ###","Error Token #",153))
    def test_comment_4(self):
        self.assertTrue(TestLexer.test("## Hello honey ## ## ","Error Token #",154))
    
    def test_keyword_1(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("Break Continue If Elseif Else Foreach","Break,Continue,If,Elseif,Else,Foreach,<EOF>",155))
    def test_keyword_2(self):
        self.assertTrue(TestLexer.test("True False Array In Int Float","True,False,Array,In,Int,Float,<EOF>",156))    
    def test_keyword_3(self):
        self.assertTrue(TestLexer.test("Boolean String Return Null Class Val","Boolean,String,Return,Null,Class,Val,<EOF>",157))
    def test_keyword_4(self):
        self.assertTrue(TestLexer.test("Var Constructor Destructor New By","Var,Constructor,Destructor,New,By,<EOF>",158))
    
    def test_operator_1(self):
        """test operator"""
        self.assertTrue(TestLexer.test("+ - * / %","+,-,*,/,%,<EOF>",159)) 
    def test_operator_2(self):
        self.assertTrue(TestLexer.test("! && || == =","!,&&,||,==,=,<EOF>",160))
    def test_operator_3(self):
        self.assertTrue(TestLexer.test("!= > < >= <=","!=,>,<,>=,<=,<EOF>",161))
    def test_operator_4(self):
        self.assertTrue(TestLexer.test("==. +. . :: New","==.,+.,.,::,New,<EOF>",162))
    
    def test_separator(self):
        """test separator"""
        self.assertTrue(TestLexer.test("[ ] ( ) . , ; { }","[,],(,),.,,,;,{,},<EOF>",163))
    
    def test_array_lit_1(self):
        """test simple array"""
        self.assertTrue(TestLexer.test("Array(1,2,3)","Array,(,1,,,2,,,3,),<EOF>",164))
    def test_array_lit_2(self):
        """test array with expr"""
        self.assertTrue(TestLexer.test("Array(1+2,2*3,3)","Array,(,1,+,2,,,2,*,3,,,3,),<EOF>",165))
    def test_array_lit_3(self):
        """test array"""
        self.assertTrue(TestLexer.test("Array()","Array,(,),<EOF>",166))
    def test_array_lit_4(self):
        """test array"""
        self.assertTrue(TestLexer.test("Array(\"Hello\", \"my\", \"fen\")","Array,(,Hello,,,my,,,fen,),<EOF>",167))
    def test_array_lit_5(self):
        """test multi array"""
        self.assertTrue(TestLexer.test("Array(Array(1, 2, 3), Array(4, 5, 6))","Array,(,Array,(,1,,,2,,,3,),,,Array,(,4,,,5,,,6,),),<EOF>",168))

    def test_mixed_1(self):
        """test mixed"""
        self.assertTrue(TestLexer.test("Var x: Int = 3;","Var,x,:,Int,=,3,;,<EOF>",169))
    def test_mixed_2(self):
        self.assertTrue(TestLexer.test("Val x: Float = 10.e-12 + 12.3;","Val,x,:,Float,=,10.e-12,+,12.3,;,<EOF>",170))
    def test_mixed_3(self):
        self.assertTrue(TestLexer.test("a = -3 and b <= 10 : True","a,=,-,3,and,b,<=,10,:,True,<EOF>",171))
    def test_mixed_4(self):
        self.assertTrue(TestLexer.test("Foreach(i In 1 .. 100 By 1)","Foreach,(,i,In,1,..,100,By,1,),<EOF>",172))
    def test_mixed_5(self):
        self.assertTrue(TestLexer.test("Self.width = 10*3; Self.height = 10","Self,.,width,=,10,*,3,;,Self,.,height,=,10,<EOF>",173))
    def test_mixed_6(self):
        self.assertTrue(TestLexer.test("Class Student {}","Class,Student,{,},<EOF>",174))
    def test_mixed_7(self):
        self.assertTrue(TestLexer.test("Student::$getName()","Student,::,$getName,(,),<EOF>",175))
    def test_mixed_8(self):
        self.assertTrue(TestLexer.test("foo(a,b : Int){ Return a / b; }","foo,(,a,,,b,:,Int,),{,Return,a,/,b,;,},<EOF>",176))
    def test_mixed_9(self):
        self.assertTrue(TestLexer.test("\"This is a string \" +. \"and another string\"","This is a string ,+.,and another string,<EOF>",177))
    def test_mixed_10(self):
        self.assertTrue(TestLexer.test("x + 1 -23 && abc_ass f(a||b) $_a_","x,+,1,-,23,&&,abc_ass,f,(,a,||,b,),$_a_,<EOF>",178))
    def test_mixed_11(self):
        self.assertTrue(TestLexer.test("a+b-c/$d*$e=10%2!False##","a,+,b,-,c,/,$d,*,$e,=,10,%,2,!,False,Error Token #",179))
    def test_mixed_12(self):
        self.assertTrue(TestLexer.test("Val a: String = \"Hi\"; Val b: String = \"fen","Val,a,:,String,=,Hi,;,Val,b,:,String,=,Unclosed String: fen",180))

    def test_full_1(self):
        """test full program in lexer"""
        input = """
                    Class Program {
                        main(){
                            Out.printInt(Shape::$numOfShape);
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,181))
    def test_full_2(self):
        input = """
                    Class Program {
                        main(){}
                    }
                """
        expect = """Class,Program,{,main,(,),{,},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,182))
    def test_full_3(self):
        input = """
                    Class Program {
                        main(){
                            Var a: Int = 0;
                            Var b: Int = 2;
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,Var,a,:,Int,=,0,;,Var,b,:,Int,=,2,;,},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,183))
    def test_full_4(self):
        input = """
                    Class A {
                        Var $a: Boolean;
                    }
                    Class B: A {}
                """
        expect = """Class,A,{,Var,$a,:,Boolean,;,},Class,B,:,A,{,},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,184))
    def test_full_5(self):
        input = """
                    Class Program {
                        main(){
                            Foreach(i In 1 .. 10){
                                a = a + i;
                            }
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,Foreach,(,i,In,1,..,10,),{,a,=,a,+,i,;,},},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,185))
    def test_full_6(self):
        input = """
                    Class Program {
                        main(){
                            Val x: String = "This string is true";
                            x = "This string unclosed ;
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,Val,x,:,String,=,This string is true,;,x,=,Unclosed String: This string unclosed ;"""
        self.assertTrue(TestLexer.test(input,expect,186))
    def test_full_7(self):
        input = """
                    Class Program {
                        main(){
                            If (a == True || b != $_count_) {
                                x = 12.3e10 + 0x1AB;
                            } Elseif(){} Else {}
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,If,(,a,==,True,||,b,!=,$_count_,),{,x,=,12.3e10,+,0x1AB,;,},Elseif,(,),{,},Else,{,},},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,187))
    def test_full_8(self):
        input = """
                    Class Program {
                        main(){
                            ## This is comment
                            !@#$%^&*() everything will not read
                            until the end <> "" ''
                            ##
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,188))
    def test_full_9(self):
        input = """
                    Class Program {
                        main(){
                            a[1][More] and more__more_id -> Break through -> Continue
                        }
                    }
                """
        expect = """Class,Program,{,main,(,),{,a,[,1,],[,More,],and,more__more_id,-,>,Break,through,-,>,Continue,},},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,189))
    def test_full_10(self):
        input = """
                    {
                        Var r,s: Int;
                        r = 2.0;
                        s = r*r*Self.PI;
                        Var c: String = "";
                    }
                """
        expect = """{,Var,r,,,s,:,Int,;,r,=,2.0,;,s,=,r,*,r,*,Self,.,PI,;,Var,c,:,String,=,,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,190))

    def test_another_1(self):
        """test something else"""
        self.assertTrue(TestLexer.test("a[a[1*2-3+4%5]]","a,[,a,[,1,*,2,-,3,+,4,%,5,],],<EOF>",191))
    def test_another_2(self):
        self.assertTrue(TestLexer.test("Array[Float,3]","Array,[,Float,,,3,],<EOF>",192))
    def test_another_3(self):
        self.assertTrue(TestLexer.test(""" "This string has comment ## comment ## !@#$%^&*()-_+=" ""","This string has comment ## comment ## !@#$%^&*()-_+=,<EOF>",193))
    def test_another_4(self):
        self.assertTrue(TestLexer.test("0_0.000e00_x0","0,_0,.000e00,_x0,<EOF>",194))
    def test_another_5(self):
        self.assertTrue(TestLexer.test(""" "This string has backsclash \\\ " ""","This string has backsclash \\\ ,<EOF>",195))
    def test_another_6(self):
        self.assertTrue(TestLexer.test(""" "This string has carried return \r " ""","Unclosed String: This string has carried return ",196))
    def test_another_7(self):
        self.assertTrue(TestLexer.test("10_000_00.00e-12","1000000.00e-12,<EOF>",197))
    def test_another_8(self):
        """test floatlit absent two part"""
        self.assertTrue(TestLexer.test("E-100","E,-,100,<EOF>",198))
    def test_another_9(self):
        self.assertTrue(TestLexer.test("++i $Abc100_$","+,+,i,$Abc100_,Error Token $",199))
    def test_another_10(self):
        self.assertTrue(TestLexer.test(""" "Single Quote \' " ""","""Single Quote ' ,<EOF>""",200))