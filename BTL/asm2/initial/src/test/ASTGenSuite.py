import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class A {}"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """Class A {}"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """Class A {}"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,302))
   