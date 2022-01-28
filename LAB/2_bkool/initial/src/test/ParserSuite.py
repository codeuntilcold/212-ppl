import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """vardecl"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        """More complex program"""
        input = """vardecl funcdecl"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        """Miss ) int main( {}"""
        input = """vadecl"""
        expect = "Error on line 1 col 3: d"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_4(self):
        """Miss ) int main( {}"""
        input = """int a, b,c;
            float foo(int a; float c, d) body
            float goo (float a, b) body"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))