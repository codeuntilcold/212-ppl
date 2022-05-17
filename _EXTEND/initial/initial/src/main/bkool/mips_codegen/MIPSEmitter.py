import struct

from AST import FloatType, IntType
from .MIPSMachineCode import MIPSCode

ZERO    = '$zero'
AT      = '$at'
V0      = '$v0'
V1      = '$v1'
A0      = '$a0'
A1      = '$a1'
A2      = '$a2'
A3      = '$a3'

T0      = '$t0'
T1      = '$t1'
T2      = '$t2'
T3      = '$t3'
T4      = '$t4'
T5      = '$t5'
T6      = '$t6'
T7      = '$t7'
T8      = '$t8'
T9      = '$t9'

S0      = '$s0'
S1      = '$s1'
S2      = '$s2'
S3      = '$s3'
S4      = '$s4'
S5      = '$s5'
S6      = '$s6'
S7      = '$s7'

K0      = '$k0'
K1      = '$k1'

GP      = '$gp'
SP      = '$sp'
FP      = '$fp'
RA      = '$ra'

F1      = '$f1'
F12     = '$f12'

ACC     = A0
ACCF    = F12

class MIPSEmitter:
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.mars = MIPSCode()

    @staticmethod
    def __float_to_hex__(f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    """
                METHOD RELATED
    """
    def emitLABEL(self, label):
        return label + ":\n"

    def emitPOPSTACK(self):
        return self.mars.emitADDI(SP, SP, 4)

    def emitPUSHSTACK(self, reg):
        result = list()
        result.append(self.mars.emitSW(reg, SP, 0))
        result.append(self.mars.emitADDI(SP, SP, -4))
        return ''.join(result)

    def emitFRAMEALLOC(self, framesize):
        result = list()
        result.append(self.mars.emitADDI(SP, SP, -(framesize * 4)))
        result.append(self.mars.emitSW(FP, SP, framesize * 4))
        result.append(self.mars.emitMOVE(FP, SP))
        return ''.join(result) + '\n'

    def emitFRAMERESET(self, framesize):
        result = list()
        result.append(self.mars.emitMOVE(SP, FP))
        result.append(self.mars.emitLW(FP, SP, framesize * 4))
        result.append(self.mars.emitADDI(SP, SP, framesize * 4))
        return '\n' + ''.join(result) + '\n'

    def emitSTOREINDEX(self, idx, intype):        
        if type(intype) == IntType:
            return self.mars.emitSW(ACC, FP, (idx + 1) * 4)
        elif type(intype) == FloatType:
            return self.mars.emitSWC1(ACCF, FP, (idx + 1) * 4)

    def emitLOADINDEX(self, idx, intype):
        if type(intype) == IntType:
            return self.mars.emitLW(ACC, FP, (idx + 1) * 4)
        elif type(intype) == FloatType:
            return self.mars.emitLWC1(ACCF, FP, (idx + 1) * 4)


    """
            WORK WITH ACCUMULATOR
    """
    def emitLOADACC(self, value, intype=IntType()):
        if type(intype) == IntType:
            return self.mars.emitLI(ACC, int(value))
        elif type(intype) == FloatType:
            return self.emitLOADACCF(value)

    def emitPUSHACC(self, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.emitPUSHSTACK(ACC))
        elif type(intype) == FloatType:
            result.append(self.mars.emitSWC1(ACCF, SP, 0))
            result.append(self.mars.emitADDI(SP, SP, -4))
        return ''.join(result)

    def emitLOADACCF(self, value):
        result = list()
        hex_repr = MIPSEmitter.__float_to_hex__(float(value))
        result.append(self.mars.emitLI(T1, hex_repr))
        result.append(self.mars.emitMTC1(T1, ACCF))
        return ''.join(result)

    """
            OPERATORS
    """
    def emitADDOP(self, op, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.mars.emitLW(T1, SP, 4))
        if type(intype) == FloatType:
            result.append(self.mars.emitLWC1(F1, SP, 4))
        
        if op == '+':
            result.append(
                self.mars.emitADD(ACC, T1, ACC)
                if type(intype) == IntType else
                self.mars.emitADDS(ACCF, F1, ACCF)
            )
        elif op == '-':
            result.append(
                self.mars.emitSUB(ACC, T1, ACC)
                if type(intype) == IntType else
                self.mars.emitSUBS(ACCF, F1, ACCF)
            )
        result.append(self.emitPOPSTACK())
        return ''.join(result)
    
    def emitMULOP(self, op, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.mars.emitLW(T1, SP, 4))
        if type(intype) == FloatType:
            result.append(self.mars.emitLWC1(F1, SP, 4))
        
        if op == '*':
            result.append(
                self.mars.emitMUL(ACC, T1, ACC)
                if type(intype) == IntType else
                self.mars.emitMULS(ACCF, F1, ACCF)
            )
        elif op == '/':
            result.append(
                self.mars.emitDIV(ACC, T1, ACC)
                if type(intype) == IntType else
                self.mars.emitDIVS(ACCF, F1, ACCF)
            )
        else:
            result.append(
                self.mars.emitDIV(ACC, T1, ACC)
                if type(intype) == IntType else
                self.mars.emitDIVS(ACCF, F1, ACCF)
            )
        result.append(self.emitPOPSTACK())
        return ''.join(result)

    # Move Int's TOS to Float's TOS
    def emitI2F(self):
        result = list()
        result.append(self.mars.emitMTC1(ACC, F1))
        result.append(self.mars.emitCVTSW(ACCF, F1))
        return ''.join(result)

    # Move Int's TOS to Float's TOS
    def emitI2FSTACK(self):
        result = list()
        result.append(self.mars.emitLWC1(F1, SP, 4))
        result.append(self.mars.emitCVTSW(F1, F1))
        result.append(self.mars.emitSWC1(F1, SP, 4))
        return ''.join(result)

    def emitNOT(self):
        return self.mars.emitNOT(ACC, ACC)
    
    def emitNEG(self, intype):
        return self.mars.emitNEG(ACC, ACC) \
            if type(intype) == IntType else \
            self.mars.emitNEGS(ACCF, ACCF)

    """
                BUILT-IN METHODS
    """
    def emitPUTINT(self):
        result = list()
        result.append(self.mars.emitLI(V0, 1))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTINTLN(self):
        result = list()
        result.append(self.mars.emitLI(V0, 1))
        result.append(self.mars.emitSYSCALL())
        result.append(self.mars.emitLI(A0, 10)) # LF
        result.append(self.mars.emitLI(V0, 11))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTFLOAT(self):
        result = list()
        result.append(self.mars.emitLI(V0, 2))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTFLOATLN(self):
        result = list()
        result.append(self.mars.emitLI(V0, 2))
        result.append(self.mars.emitSYSCALL())
        result.append(self.mars.emitLI(A0, 10)) # LF
        result.append(self.mars.emitLI(V0, 11))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPROLOG(self):
        result = list()
        result.append(self.mars.emitTEXT())
        return ''.join(result)

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    def printout(self, in_):
        self.buff.append(in_)
    
    def clearBuff(self):
        self.buff.clear()