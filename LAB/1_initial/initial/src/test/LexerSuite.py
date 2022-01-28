import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc abc","abc,abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    # def test_illegal_escape(self):
    #     """test illegal escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    # def test_unterminated_string(self):
    #     """test unclosed string"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    # def test_normal_string_with_escape(self):
    #     """test normal string with escape"""
    #     self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_ip_addr(self):
        self.assertTrue(TestLexer.checkLexeme("192.168.0.1", "192.168.0.1,<EOF>", 108))

    def test_pascal_real(self):
        self.assertTrue(TestLexer.checkLexeme("1.0 1e-12 1.0e-12 0.000000001", "1.0,1e-12,1.0e-12,0.000000001,<EOF>", 109))

    def test_pascal_string(self):
        self.assertTrue(TestLexer.checkLexeme("'Yanxi Palace didn''t do it - 2021'", "'Yanxi Palace didn''t do it - 2021',<EOF>", 110))
    
    def test_php_int(self):
        self.assertTrue(TestLexer.checkLexeme("1_234_567 0", "1234567,0,<EOF>", 111)) 
