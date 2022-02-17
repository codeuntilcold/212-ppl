import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        """Simple program: int main() {} """
        input = """Class A {}"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                []
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_301(self):
        """More complex program"""
        input = """Class A: B {}"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [],
                Id("B")
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_302(self):
        """More complex program"""
        input = """Class A {
            Var a: Int;
        }"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            Id("a"),
                            IntType()
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_303(self):
        input = """Class A {
            Var a, $b: Int;
        }"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            Id("a"),
                            IntType()
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        VarDecl(
                            Id("$b"),
                            IntType()
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_304(self):
        input = """Class A {
            Var a, $b: Int = 0, 0;
        }"""
        expect = str(Program([
            ClassDecl(
                Id("A"),
                [
                    AttributeDecl(
                        Instance(),
                        VarDecl(
                            Id("a"),
                            IntType(),
                            IntLiteral(0)
                        )
                    ),
                    AttributeDecl(
                        Static(),
                        VarDecl(
                            Id("$b"),
                            IntType(),
                            IntLiteral(0)
                        )
                    )
                ]
            )
        ]))
        self.assertTrue(TestAST.test(input,expect,304))

    # def test_305(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,305))

    # def test_306(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,306))

    # def test_307(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,307))

    # def test_308(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,308))

    # def test_309(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,309))

    # def test_310(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,310))

    # def test_311(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,311))

    # def test_312(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,312))

    # def test_313(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,313))

    # def test_314(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,314))

    # def test_315(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,315))

    # def test_316(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,316))

    # def test_317(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,317))

    # def test_318(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,318))

    # def test_319(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,319))

    # def test_320(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,320))

    # def test_321(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,321))

    # def test_322(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,322))

    # def test_323(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,323))

    # def test_324(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,324))

    # def test_325(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,325))

    # def test_326(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,326))

    # def test_327(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,327))

    # def test_328(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,328))

    # def test_329(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,329))

    # def test_330(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,330))

    # def test_331(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,331))

    # def test_332(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,332))

    # def test_333(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,333))

    # def test_334(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,334))

    # def test_335(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,335))

    # def test_336(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,336))

    # def test_337(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,337))

    # def test_338(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,338))

    # def test_339(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,339))

    # def test_340(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,340))

    # def test_341(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,341))

    # def test_342(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,342))

    # def test_343(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,343))

    # def test_344(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,344))

    # def test_345(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,345))

    # def test_346(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,346))

    # def test_347(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,347))

    # def test_348(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,348))

    # def test_349(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,349))

    # def test_350(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,350))

    # def test_351(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,351))

    # def test_352(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,352))

    # def test_353(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,353))

    # def test_354(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,354))

    # def test_355(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,355))

    # def test_356(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,356))

    # def test_357(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,357))

    # def test_358(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,358))

    # def test_359(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,359))

    # def test_360(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,360))

    # def test_361(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,361))

    # def test_362(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,362))

    # def test_363(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,363))

    # def test_364(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,364))

    # def test_365(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,365))

    # def test_366(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,366))

    # def test_367(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,367))

    # def test_368(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,368))

    # def test_369(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,369))

    # def test_370(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,370))

    # def test_371(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,371))

    # def test_372(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,372))

    # def test_373(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,373))

    # def test_374(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,374))

    # def test_375(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,375))

    # def test_376(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,376))

    # def test_377(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,377))

    # def test_378(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,378))

    # def test_379(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,379))

    # def test_380(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,380))

    # def test_381(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,381))

    # def test_382(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,382))

    # def test_383(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,383))

    # def test_384(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,384))

    # def test_385(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,385))

    # def test_386(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,386))

    # def test_387(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,387))

    # def test_388(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,388))

    # def test_389(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,389))

    # def test_390(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,390))

    # def test_391(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,391))

    # def test_392(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,392))

    # def test_393(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,393))

    # def test_394(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,394))

    # def test_395(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,395))

    # def test_396(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,396))

    # def test_397(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,397))

    # def test_398(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,398))

    # def test_399(self):
    #     input = """"""
    #     expect = str(Program([
    #         ClassDecl()
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,399))
   