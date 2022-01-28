import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))

    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",103))   #?????????????????????????

    def test_integer(self):
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))    #?????????????????
    
    def test_105(self):
        self.assertTrue(TestLexer.test("anan$as","anan,$as,<EOF>",105))

    def test_106(self):
        self.assertTrue(TestLexer.test("## this comment ##","<EOF>",106))

    def test_107(self):
        self.assertTrue(TestLexer.test("## this comment ## annoying","annoying,<EOF>",107))

    def test_108(self):
        self.assertTrue(TestLexer.test("_identifiers","_identifiers,<EOF>",108))

    def test_109(self):
        self.assertTrue(TestLexer.test("9slide","9,slide,<EOF>",109))

    def test_110(self):
        self.assertTrue(TestLexer.test("0x1A","0x1A,<EOF>",110))

    def test_111(self):
        self.assertTrue(TestLexer.test("0a","0,a,<EOF>",111))

    def test_112(self):
        self.assertTrue(TestLexer.test("1_234","1234,<EOF>",112))

    def test_113(self):
        self.assertTrue(TestLexer.test("0b12","0b1,2,<EOF>",113))

    def test_114(self):
        self.assertTrue(TestLexer.test("1b123","1,b123,<EOF>",114))

    def test_115(self):
        self.assertTrue(TestLexer.test("$9valid","$9valid,<EOF>",115))

    def test_116(self):
        self.assertTrue(TestLexer.test("Var x: Int = 0","Var,x,:,Int,=,0,<EOF>",116))

    def test_117(self):
        self.assertTrue(TestLexer.test("\"Normal string\"","Normal string,<EOF>",117))

    def test_118(self):
        self.assertTrue(TestLexer.test("\"Normal string\\t\"","Normal string\\t,<EOF>",118))

    def test_119(self):
        self.assertTrue(TestLexer.test("\"abc\\h\"","Illegal Escape In String: abc\h",119))

    def test_120(self):
        self.assertTrue(TestLexer.test("a .> b","a,.,>,b,<EOF>",120))

    def test_121(self):
        self.assertTrue(TestLexer.test("a +. b","a,+.,b,<EOF>",121))

    def test_122(self):
        self.assertTrue(TestLexer.test("a @ b","a,Error Token @",122))

    def test_123(self):
        self.assertTrue(TestLexer.test("Var $x: Int;","Var,$x,:,Int,;,<EOF>",123))

    def test_124(self):
        self.assertTrue(TestLexer.test("$getNum()","$getNum,(,),<EOF>",124))

    def test_125(self):
        self.assertTrue(TestLexer.test("\f","<EOF>",125))

    def test_126(self):
        self.assertTrue(TestLexer.test(""" ##This is a 
        multi-line
        comment
        ## ""","<EOF>",126))

    def test_127(self):
        self.assertTrue(TestLexer.test("?","Error Token ?",127))

    def test_128(self):
        self.assertTrue(TestLexer.test("a << b","a,<,<,b,<EOF>",128))

    def test_129(self):
        self.assertTrue(TestLexer.test("0x1957z2","0x1957,z2,<EOF>",129))

    def test_130(self):
        self.assertTrue(TestLexer.test("000123","00,0123,<EOF>",130))

    def test_131(self):
        self.assertTrue(TestLexer.test("-1234_567","-,1234567,<EOF>",131))

    def test_132(self):
        self.assertTrue(TestLexer.test("__123","__123,<EOF>",132))

    def test_133(self):
        self.assertTrue(TestLexer.test("_123_456","_123_456,<EOF>",133))

    def test_134(self):
        self.assertTrue(TestLexer.test("$23cents","$23cents,<EOF>",134))

    def test_135(self):
        self.assertTrue(TestLexer.test("a::b","a,::,b,<EOF>",135))

    def test_136(self):
        self.assertTrue(TestLexer.test("a==.b","a,==.,b,<EOF>",136))

    def test_137(self):
        self.assertTrue(TestLexer.test("a & b","a,Error Token &",137))

    def test_138(self):
        self.assertTrue(TestLexer.test("<key, value>","<,key,,,value,>,<EOF>",138))

    def test_139(self):
        self.assertTrue(TestLexer.test("0x1234","0x1234,<EOF>",139))

    def test_140(self):
        self.assertTrue(TestLexer.test("0x_1475","0,x_1475,<EOF>",140))

    def test_141(self):
        self.assertTrue(TestLexer.test("0b157","0b1,57,<EOF>",141))

    def test_142(self):
        self.assertTrue(TestLexer.test("0_175984","0,_175984,<EOF>",142))

    def test_143(self):
        self.assertTrue(TestLexer.test("0175_14","017514,<EOF>",143))

    def test_144(self):
        self.assertTrue(TestLexer.test("001247_19","00,124719,<EOF>",144))

    """
        What error will this raise ?????
    """
    def test_145(self):
        self.assertTrue(TestLexer.test("12__34","12,__34,<EOF>",145))

    def test_146(self):
        self.assertTrue(TestLexer.test("0.1E12","0.1E12,<EOF>",146))

    def test_147(self):
        self.assertTrue(TestLexer.test("0.1e-15","0.1e-15,<EOF>",147))

    def test_148(self):
        self.assertTrue(TestLexer.test(".145E145",".145E145,<EOF>",148))

    def test_149(self):
        self.assertTrue(TestLexer.test("15e10","15e10,<EOF>",149))

    def test_150(self):
        self.assertTrue(TestLexer.test("1.0000140","1.0000140,<EOF>",150))

    """
        Is this valid ?
    """
    def test_151(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",151))


    def test_152(self):
        self.assertTrue(TestLexer.test(".123",".,123,<EOF>",152))

    def test_153(self):
        self.assertTrue(TestLexer.test(".00124e15",".00124e15,<EOF>",153))

    def test_154(self):
        self.assertTrue(TestLexer.test(".0x1457",".,0x1457,<EOF>",154))

    def test_155(self):
        self.assertTrue(TestLexer.test("1_234.56","1234.56,<EOF>",155))

    def test_156(self):
        self.assertTrue(TestLexer.test(" \"Normal string\" ","Normal string,<EOF>",156))

    def test_157(self):
        self.assertTrue(TestLexer.test(" \"A bit more \\t abnormal\" ","A bit more \\t abnormal,<EOF>",157))

    def test_158(self):
        self.assertTrue(TestLexer.test(" \"It is getting '\"interesting'\"\" ","It is getting '\"interesting'\",<EOF>",158))

    def test_159(self):
        self.assertTrue(TestLexer.test(" \"An unclosed string \\","Illegal Escape In String: An unclosed string \\",159))

    def test_160(self):
        self.assertTrue(TestLexer.test(" \"An unclosed string \\\"","Illegal Escape In String: An unclosed string \\\"",160))

    def test_161(self):
        self.assertTrue(TestLexer.test(" \"An unclosed string '","Unclosed String: An unclosed string '",161))

    def test_162(self):
        self.assertTrue(TestLexer.test(" \"An unclosed string \n","Unclosed String: An unclosed string ",162))

    def test_163(self):
        self.assertTrue(TestLexer.test(" \"Very weird !@#$%^&*() string\"","Very weird !@#$%^&*() string,<EOF>",163))

    def test_164(self):
        self.assertTrue(TestLexer.test(" \"Extremely weird string indeed \\1\"","Illegal Escape In String: Extremely weird string indeed \\1",164))

    def test_165(self):
        self.assertTrue(TestLexer.test("a[0]","a,[,0,],<EOF>",165))

    def test_166(self):
        self.assertTrue(TestLexer.test("\"String A\" +. \"String B\"","String A,+.,String B,<EOF>",166))

    def test_167(self):
        self.assertTrue(TestLexer.test(".123e0 + True",".123e0,+,True,<EOF>",167))

    def test_168(self):
        self.assertTrue(TestLexer.test("12 || 5.78","12,||,5.78,<EOF>",168))

    def test_169(self):
        self.assertTrue(TestLexer.test("17 % 3","17,%,3,<EOF>",169))

    def test_170(self):
        self.assertTrue(TestLexer.test("Array[Int,5]","Array,[,Int,,,5,],<EOF>",170))

    def test_171(self):
        self.assertTrue(TestLexer.test("Array()","Array,(,),<EOF>",171))

    def test_172(self):
        self.assertTrue(TestLexer.test("\"String in the town!@#$%^&*(\"","String in the town!@#$%^&*(,<EOF>",172))

    def test_173(self):
        self.assertTrue(TestLexer.test("@decorator.life","Error Token @",173))

    def test_174(self):
        self.assertTrue(TestLexer.test("a::a","a,::,a,<EOF>",174))

    def test_175(self):
        self.assertTrue(TestLexer.test("one..two","one,..,two,<EOF>",175))

    def test_176(self):
        self.assertTrue(TestLexer.test("1..2","1.,.,2,<EOF>",176))

    def test_177(self):
        self.assertTrue(TestLexer.test("1 ..2","1,..,2,<EOF>",177))

    def test_178(self):
        self.assertTrue(TestLexer.test("0b00","0b0,0,<EOF>",178))

    def test_179(self):
        self.assertTrue(TestLexer.test("0b1_000_100_111","0b1000100111,<EOF>",179))

    def test_180(self):
        self.assertTrue(TestLexer.test("0127_895","0127,_895,<EOF>",180))

    def test_181(self):
        self.assertTrue(TestLexer.test("012__78","012,__78,<EOF>",181))

    def test_182(self):
        self.assertTrue(TestLexer.test("\"String","Unclosed String: String",182))

    def test_183(self):
        self.assertTrue(TestLexer.test("\"String\\","Illegal Escape In String: String\\",183))

    def test_184(self):
        self.assertTrue(TestLexer.test("\"String\\n","Unclosed String: String\\n",184))

    def test_185(self):
        self.assertTrue(TestLexer.test("\"String''","Unclosed String: String''",185))

    def test_186(self):
        self.assertTrue(TestLexer.test("Var x: Int = 3;","Var,x,:,Int,=,3,;,<EOF>",186))
   
    def test_187(self):
        self.assertTrue(TestLexer.test("Val x: Float = 10.e-12 + 12.3;",
            "Val,x,:,Float,=,10.e-12,+,12.3,;,<EOF>",187))
   
    def test_188(self):
        self.assertTrue(TestLexer.test("a = -3 and b <= 10 : True",
            "a,=,-,3,and,b,<=,10,:,True,<EOF>",188))
   
    def test_189(self):
        self.assertTrue(TestLexer.test("Foreach(i In 1 .. 100 By 1)",
            "Foreach,(,i,In,1,..,100,By,1,),<EOF>",189))
   
    def test_190(self):
        self.assertTrue(TestLexer.test("Self.width = 10*3; Self.height = 10",
            "Self,.,width,=,10,*,3,;,Self,.,height,=,10,<EOF>",190))
   
    def test_191(self):
        self.assertTrue(TestLexer.test("Class Student {}",
            "Class,Student,{,},<EOF>",191))
   
    def test_192(self):
        self.assertTrue(TestLexer.test("Student::$getName()",
            "Student,::,$getName,(,),<EOF>",192))
   
    def test_193(self):
        self.assertTrue(TestLexer.test("foo(a,b : Int){ Return a / b; }",
            "foo,(,a,,,b,:,Int,),{,Return,a,/,b,;,},<EOF>",193))
   
    def test_194(self):
        self.assertTrue(TestLexer.test("\"This is a string \" +. \"and another string\"",
            "This is a string ,+.,and another string,<EOF>",194))
   
    def test_195(self):
        self.assertTrue(TestLexer.test("x + 1 -23 && abc_ass f(a||b) $_a_",
            "x,+,1,-,23,&&,abc_ass,f,(,a,||,b,),$_a_,<EOF>",195))
   
    def test_196(self):
        self.assertTrue(TestLexer.test("a+b-c/$d*$e=10%2!False##",
            "a,+,b,-,c,/,$d,*,$e,=,10,%,2,!,False,Error Token #",196))
   
    def test_197(self):
        self.assertTrue(TestLexer.test("Val a: String = \"Hi\"; Val b: String = \"fen",
            "Val,a,:,String,=,Hi,;,Val,b,:,String,=,Unclosed String: fen",197))

    def test_198(self):
        self.assertTrue(TestLexer.test(
            "\"The string: \\",
            "Illegal Escape In String: The string: \\",198)
        )

    def test_199(self):
        self.assertTrue(TestLexer.test(
            "\"String with single quote 'this is good'\"",
            "Unclosed String: String with single quote 'this is good'\"",199)
        )

    def test_200(self):
        self.assertTrue(TestLexer.test("\"PPL\\f-HCMUTK19\"","PPL\\f-HCMUTK19,<EOF>",200))


