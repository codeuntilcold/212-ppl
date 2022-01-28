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
        self.assertTrue(TestLexer.test("\"Normal string\"","\"Normal string\",<EOF>",117))

    def test_118(self):
        self.assertTrue(TestLexer.test("\"Normal string\\t\"","\"Normal string\\t\",<EOF>",118))

    def test_119(self):
        self.assertTrue(TestLexer.test("\"Illegal \\h\"","\"Illegal \\h\",<EOF>",119))

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
        self.assertTrue(TestLexer.test("Ox1957z2","0x1957,z2,<EOF>",129))

    def test_130(self):
        self.assertTrue(TestLexer.test("00123","00,123,<EOF>",130))