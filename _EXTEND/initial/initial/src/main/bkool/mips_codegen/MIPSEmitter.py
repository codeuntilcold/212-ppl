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

F0      = '$f0'
F1      = '$f1'
F12     = '$f12'

ACC     = S0
TMP     = T1
ACCF    = F0
TMPF    = F1

"""
        FRAME WHEN CALLING METHOD
        ra
        old fp
        <- current fp
        (self)              \\
        params               >>  increase in index
        local vars          //
        <- current sp


"""

class MIPSEmitter:
    def __init__(self, filename):
        self.filename = filename
        self.datasec = ['\t.data\n']
        self.textsec = [
            '\t.text\n',
            '\tjal Program_m_main\n'
        ]
        self.mars = MIPSCode()

    @staticmethod
    def __float_to_hex__(f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    """
                GLOBAL ATTRIBUTE
    """
    def emitATTRIBUTE(self, name, typ, val):
        return self.datasec.append(name + ":\t\t" + typ + "\t\t" + val + "\n")
    
    """
                METHOD RELATED
    """
    def emitLABEL(self, label):
        return "\n" + label + ":\n"

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
        result.append(self.mars.emitSW(RA, SP, framesize * 4))
        result.append(self.mars.emitSW(FP, SP, (framesize - 1) * 4))
        # result.append(self.mars.emitMOVE(FP, SP))
        result.append(self.mars.emitADDI(FP, SP, (framesize - 2) * 4))
        return ''.join(result) + '\n'

    def emitFRAMERESET(self, framesize):
        result = list()
        # result.append(self.mars.emitMOVE(SP, FP))
        result.append(self.mars.emitADDI(SP, FP, -(framesize - 2) * 4))
        result.append(self.mars.emitLW(FP, SP, (framesize - 1) * 4))
        result.append(self.mars.emitLW(RA, SP, framesize * 4))
        result.append(self.mars.emitADDI(SP, SP, framesize * 4))
        return '\n' + ''.join(result) + '\n'

    """
            STATEMENTS RELATED
    """
    def emitJ(self, label):
        return self.mars.emitJ(label)

    def emitJAL(self, label):
        return self.mars.emitJAL(label)

    def emitJRA(self):
        return self.mars.emitJR(RA)

    def emitLOADRETURN(self, intype):
        if type(intype) == IntType:
            return self.mars.emitADDI(V0, ACC, 0)
        elif type(intype) == FloatType:
            return self.mars.emitMFC1(V0, ACCF)

    def emitLOADINDEX(self, idx, intype):
        if type(intype) == IntType:
            return self.mars.emitLW(ACC, FP, -idx * 4)
        elif type(intype) == FloatType:
            return self.mars.emitLWC1(ACCF, FP, -idx * 4)

    def emitSTOREINDEX(self, idx, intype):        
        if type(intype) == IntType:
            return self.mars.emitSW(ACC, FP, -idx * 4)
        elif type(intype) == FloatType:
            return self.mars.emitSWC1(ACCF, FP, -idx * 4)

    # Pre-allocate param value before calling FRAMEALLOC
    def emitSTOREPARAM(self, idx, intype):
        # Two words for $ra and $fp
        OFFSET = 2
        if type(intype) == IntType:
            return self.mars.emitSW(ACC, SP, -(idx + OFFSET) * 4)
        elif type(intype) == FloatType:
            return self.mars.emitSWC1(ACCF, SP, -(idx + OFFSET) * 4)


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
        result.append(self.mars.emitLI(TMP, hex_repr))
        result.append(self.mars.emitMTC1(TMP, ACCF))
        return ''.join(result)

    """
            OPERATORS
    """
    def emitADDOP(self, op, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.mars.emitLW(TMP, SP, 4))
        if type(intype) == FloatType:
            result.append(self.mars.emitLWC1(TMPF, SP, 4))
        
        if op == '+':
            result.append(
                self.mars.emitADD(ACC, TMP, ACC)
                if type(intype) == IntType else
                self.mars.emitADDS(ACCF, TMPF, ACCF)
            )
        elif op == '-':
            result.append(
                self.mars.emitSUB(ACC, TMP, ACC)
                if type(intype) == IntType else
                self.mars.emitSUBS(ACCF, TMPF, ACCF)
            )
        result.append(self.emitPOPSTACK())
        return ''.join(result)
    
    def emitMULOP(self, op, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.mars.emitLW(TMP, SP, 4))
        if type(intype) == FloatType:
            result.append(self.mars.emitLWC1(TMPF, SP, 4))
        
        if op == '*':
            result.append(
                self.mars.emitMUL(ACC, TMP, ACC)
                if type(intype) == IntType else
                self.mars.emitMULS(ACCF, TMPF, ACCF)
            )
        elif op == '/':
            result.append(
                self.mars.emitDIV(ACC, TMP, ACC)
                if type(intype) == IntType else
                self.mars.emitDIVS(ACCF, TMPF, ACCF)
            )
        else:
            result.append(
                self.mars.emitDIV(ACC, TMP, ACC)
                if type(intype) == IntType else
                self.mars.emitDIVS(ACCF, TMPF, ACCF)
            )
        result.append(self.emitPOPSTACK())
        return ''.join(result)

    # Move Int's TOS to Float's TOS
    def emitI2F(self):
        result = list()
        result.append(self.mars.emitMTC1(ACC, TMPF))
        result.append(self.mars.emitCVTSW(ACCF, TMPF))
        return ''.join(result)

    # Move Int's TOS to Float's TOS
    def emitI2FSTACK(self):
        result = list()
        result.append(self.mars.emitLWC1(TMPF, SP, 4))
        result.append(self.mars.emitCVTSW(TMPF, TMPF))
        result.append(self.mars.emitSWC1(TMPF, SP, 4))
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
        result.append(self.mars.emitADDI(A0, ACC, 0))
        result.append(self.mars.emitLI(V0, 1))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTINTLN(self):
        result = list()
        result.append(self.mars.emitADDI(A0, ACC, 0))
        result.append(self.mars.emitLI(V0, 1))
        result.append(self.mars.emitSYSCALL())
        result.append(self.mars.emitLI(A0, 10)) # LF
        result.append(self.mars.emitLI(V0, 11))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTFLOAT(self):
        result = list()
        result.append(self.mars.emitMOVS(F12, ACCF))
        result.append(self.mars.emitLI(V0, 2))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPUTFLOATLN(self):
        result = list()
        result.append(self.mars.emitMOVS(F12, ACCF))
        result.append(self.mars.emitLI(V0, 2))
        result.append(self.mars.emitSYSCALL())
        result.append(self.mars.emitLI(A0, 10)) # LF
        result.append(self.mars.emitLI(V0, 11))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitSOURCECODE(self):
        file = open(self.filename, "w")
        file.write(''.join(self.datasec))
        file.write(''.join(self.textsec))
        file.close()

    def printvar(self, in_):
        self.datasec.append(in_)

    def printout(self, in_):
        self.textsec.append(in_)
    
    def clearBuff(self):
        self.textsec.clear()