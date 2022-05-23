import struct

from AST import BoolType, FloatType, IntType, StringType, ArrayType, ClassType
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
        self.prolog = ['\t.text\n']
        self.textsec = []
        self.mars = MIPSCode()

    @staticmethod
    def __float_to_hex__(f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    def getMIPSType(self, typ):
        if isinstance(typ, IntType):
            return '.word'
        elif isinstance(typ, FloatType):
            return '.float'
        elif isinstance(typ, StringType):
            return '.asciiz'
        elif isinstance(typ, BoolType):
            return '.word'
        else:
            return 'Not implemented type'
    
    def emitCOMMENT(self, message):
        return '\t# ' + str(message) + '\n'

    """
                GLOBAL ATTRIBUTE
    """
    def emitATTRIBUTE(self, name, typ, val):
        return str(name + ":\t\t" + self.getMIPSType(typ) + "\t\t" + str(val) + "\n")
    
    def emitASSIGNATTR(self, label, intype):
        if type(intype) == IntType:
            return self.mars.emitADDRSW(ACC, label)
        elif type(intype) == FloatType:
            return self.mars.emitSS(ACCF, label)
        else: return "Not implemented ASSIGNATTR\n"

    """
                METHOD RELATED
    """
    def emitLABEL(self, label):
        return "\n" + label + ":\n"

    def emitPOPSTACK(self):
        return ''.join([
            self.mars.emitADDI(SP, SP, 4)
        ])

    def emitPUSHSTACK(self, reg):
        result = list()
        result.append(self.emitCOMMENT('Push stack'))
        result.append(self.mars.emitSW(reg, SP, 0))
        result.append(self.mars.emitADDI(SP, SP, -4))
        return ''.join(result)

    def emitFRAMEALLOC(self, framesize):
        result = list()
        result.append(self.mars.emitADDI(SP, SP, -(framesize * 4)))
        result.append(self.mars.emitSW(RA, SP, framesize * 4))
        result.append(self.mars.emitSW(FP, SP, (framesize - 1) * 4))
        result.append(self.mars.emitADDI(FP, SP, (framesize - 2) * 4))
        return ''.join(result) + '\n'

    def emitFRAMERESET(self, framesize):
        result = list()
        result.append(self.mars.emitADDI(SP, FP, -(framesize - 2) * 4))
        result.append(self.mars.emitLW(FP, SP, (framesize - 1) * 4))
        result.append(self.mars.emitLW(RA, SP, framesize * 4))
        result.append(self.mars.emitADDI(SP, SP, framesize * 4))
        return ''.join(result) + '\n'

    """
            STATEMENTS RELATED
    """
    def emitJ(self, label):
        return ''.join([
            self.mars.emitJ(label)
        ])

    def emitJAL(self, label):
        return ''.join([
            self.mars.emitJAL(label)
        ])

    def emitJRA(self):
        return ''.join([
            self.mars.emitJR(RA)
        ])

    def emitLOADRETURN(self, intype):
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitADDI(V0, ACC, 0)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.mars.emitMFC1(V0, ACCF)
            ])
        else: return "Not implemented LOADRETURN\n"

    def emitIFFALSE(self, label):
        return ''.join([
            self.mars.emitBEQ(ACC, ZERO, label)
        ])

    def emitLOADSTATICATTR(self, label, intype):
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitADDRLW(ACC, label)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.mars.emitLS(ACCF, label)
            ])
        else: return "Not implemented LOADSTATICATTR\n"

    def emitSTORESTATICATTR(self, label, intype):
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitADDRSW(ACC, label)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.mars.emitSS(ACCF, label)
            ])
        else: return "Not implemented STORESTATICATTR\n"

    def emitLOADINDEX(self, idx, intype):
        if type(intype) == IntType:
            return ''.join([
                self.emitCOMMENT('Load local index {}'.format(idx)),
                self.mars.emitLW(ACC, FP, -idx * 4)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.emitCOMMENT('Load local index {}'.format(idx)),
                self.mars.emitLWC1(ACCF, FP, -idx * 4)
            ])
        elif type(intype) == ClassType:
            return ''.join([
                self.emitCOMMENT('Load local index {}'.format(idx)),
                self.mars.emitLW(ACC, FP, -idx * 4)
            ])
        else: return "Not implemented LOADINDEX\n"

    def emitSTOREINDEX(self, idx, intype):        
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitSW(ACC, FP, -idx * 4)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.mars.emitSWC1(ACCF, FP, -idx * 4)
            ])
        else:
            return ''.join([
                self.mars.emitSW(ACC, FP, -idx * 4)
            ])
        # else: return "Not implemented STOREINDEX\n"

    # Pre-allocate param value before calling FRAMEALLOC
    def emitSTOREPARAM(self, idx, intype):
        # Two words for $ra and $fp
        OFFSET = 2
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitSW(ACC, SP, -(idx + OFFSET) * 4)
            ])
        elif type(intype) == FloatType:
            return ''.join([
                self.mars.emitSWC1(ACCF, SP, -(idx + OFFSET) * 4)
            ])
        else:
            return ''.join([
                self.mars.emitSW(ACC, SP, -(idx + OFFSET) * 4)
            ])
        # else: return "Not implemented STOREPARAM\n"

    def emitNEW(self, size):
        return ''.join([
            self.emitCOMMENT('Heap alloc size {}'.format(size)),
            self.mars.emitLI(A0, size),
            self.mars.emitLI(V0, 9),    # sbrk
            self.mars.emitSYSCALL(),
            self.mars.emitMOVE(ACC, V0)
        ])
    
    def emitLOADFIELD(self, offset, intype):
        return ''.join([
            self.emitCOMMENT('Load field at {}'.format(offset)),
            self.mars.emitLW(ACC, ACC, offset * 4) if type(intype) == IntType else self.mars.emitLWC1(ACCF, ACC, offset * 4)
        ])

    def emitSTOREFIELD(self, offset, intype):
        return ''.join([
            self.emitCOMMENT('Save field at {}'.format(offset)),
            self.mars.emitLW(TMP, SP, 4) if type(intype) == IntType else self.mars.emitLWC1(TMPF, SP, 4),
            self.mars.emitSW(TMP, ACC, offset * 4) if type(intype) == IntType else self.mars.emitSWC1(TMPF, ACC, offset * 4)
        ])

    """
            WORK WITH ACCUMULATOR
    """
    def emitLOADACC(self, value, intype=IntType()):
        if type(intype) == IntType:
            return ''.join([
                self.mars.emitLI(ACC, int(value))
            ])
        elif type(intype) == FloatType:
            return self.emitLOADACCF(value)
        else: return "Not implemented LOADACC\n"

    def emitPUSHACC(self, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.emitPUSHSTACK(ACC))
        elif type(intype) == FloatType:
            result.append(self.mars.emitSWC1(ACCF, SP, 0))
            result.append(self.mars.emitADDI(SP, SP, -4))
        elif type(intype) == StringType:
            result.append("Not implemented PUSHACC\n")
        return ''.join(result)

    def emitLOADACCF(self, value):
        result = list()
        hex_repr = MIPSEmitter.__float_to_hex__(float(value))
        result.append(self.mars.emitLI(TMP, hex_repr))
        result.append(self.mars.emitMTC1(TMP, ACCF))
        return ''.join(result)

    def emitLOADSTACKTOACC(self):
        return ''.join([
            self.mars.emitLW(ACC, SP, 4)
        ])

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
                self.mars.emitDIV(TMP, ACC) + self.mars.emitMFLO(ACC)
                if type(intype) == IntType else
                self.mars.emitDIVS(ACCF, TMPF, ACCF)
            )
        else:
            result.append(
                self.mars.emitDIV(TMP, ACC) + self.mars.emitMFHI(ACC)
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
        return ''.join([
            self.mars.emitNOT(ACC, ACC)
        ])
    
    def emitNEG(self, intype):
        return ''.join([
            self.mars.emitNEG(ACC, ACC) \
            if type(intype) == IntType else \
            self.mars.emitNEGS(ACCF, ACCF)
        ])
    
    def emitSEQ(self):
        result = list()
        result.append(self.mars.emitLW(TMP, SP, 4))
        result.append(self.mars.emitSEQ(ACC, ACC, TMP))
        result.append(self.emitPOPSTACK())
        return ''.join(result)

    def emitSNE(self):
        result = list()
        result.append(self.mars.emitLW(TMP, SP, 4))
        result.append(self.mars.emitSNE(ACC, ACC, TMP))
        result.append(self.emitPOPSTACK())
        return ''.join(result)

    def emitBOOLOP(self, op):
        result = list()
        result.append(self.mars.emitLW(TMP, SP, 4))
        if op == '||':
            result.append(self.mars.emitOR(ACC, TMP, ACC))
        elif op == '&&':
            result.append(self.mars.emitAND(ACC, TMP, ACC))
        result.append(self.emitPOPSTACK())
        return ''.join(result)

    def emitRELOP(self, op, intype):
        result = list()
        if type(intype) == IntType:
            result.append(self.mars.emitLW(TMP, SP, 4))
            if op == '>': result.append(self.mars.emitSGT(ACC, TMP, ACC))
            if op == '>=': result.append(self.mars.emitSGE(ACC, TMP, ACC))
            if op == '<': result.append(self.mars.emitSLT(ACC, TMP, ACC))
            if op == '<=': result.append(self.mars.emitSLE(ACC, TMP, ACC))
        elif type(intype) == FloatType:
            result.append(self.mars.emitLWC1(TMPF, SP, 4))
            if op == '>': result.append(self.mars.emitCLES(ACCF, TMPF))
            if op == '>=': result.append(self.mars.emitCLTS(ACCF, TMPF))
            if op == '<': result.append(self.mars.emitCLTS(TMPF, ACCF))
            if op == '<=': result.append(self.mars.emitCLES(TMPF, ACCF))
        else: return "Not implemented RELOP\n"
        
        result.append(self.emitPOPSTACK())
        return ''.join(result)

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
        self.prolog.append(self.emitJAL('Program_m_main'))
        try:
            file.write(''.join(self.datasec))
            file.write(''.join(self.prolog))
            file.write(''.join(self.textsec))
        except TypeError as err:
            print(err)
            for line in self.textsec:
                if line:
                    print(line, end='')
                else:
                    print("None")
        file.close()

    def printvar(self, in_):
        self.datasec.append(in_)

    def printfirst(self, in_):
        self.prolog.append(in_)

    def printout(self, in_):
        self.textsec.append(in_)
    
    def clearBuff(self):
        self.textsec.clear()
