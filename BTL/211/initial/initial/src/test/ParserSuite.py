import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """ Class A {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """Class A {"""
        expect = "Error on line 1 col 8: {"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """Class A {
            Var x: Int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))