import struct
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

class MIPSEmitter:
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.mars = MIPSCode()

    @staticmethod
    def __float_to_hex__(f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    def emitMOCKPROGRAM(self):
        result = list()
        result.append(self.emitADDINT(20))
        result.append(self.emitADDINT(30))
        result.append(self.emitPRINTINT())
        return ''.join(result)

    def emitADDINT(self, in_):
        return self.mars.emitADDI(A0, A0, in_)

    def emitADDFLOAT(self, in_):
        result = list()
        hex_repr = MIPSEmitter.__float_to_hex__(float(in_))
        result.append(self.mars.emitLI(T1, hex_repr))
        result.append(self.mars.emitMTC1(T1, F1))
        result.append(self.mars.emitADDS(F12, F12, F1))
        return ''.join(result)

    def emitMERGEFLOATINT(self):
        result = list()
        result.append(self.mars.emitMTC1(A0, F1))
        result.append(self.mars.emitCVTSW(F1, F1))
        result.append(self.mars.emitADDS(F12, F12, F1))
        return ''.join(result)

    def emitPRINTINT(self):
        result = list()
        result.append(self.mars.emitLI(V0, 1))
        result.append(self.mars.emitSYSCALL())
        return ''.join(result)

    def emitPRINTFLOAT(self):
        result = list()
        result.append(self.mars.emitLI(V0, 2))
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