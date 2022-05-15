import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """Class Program {
            main() {}
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,500))
    
    def test_501(self):
        input = Program([ClassDecl(Id("Program"), [
            MethodDecl(Static(), Id("main"), [], Block([]))
        ])])
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,501))
