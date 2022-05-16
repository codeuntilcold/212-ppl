

class MIPSCode:

    END = '\n'
    INDENT = '\t'

    def emitDATA(self):
        return MIPSCode.INDENT + ".data" + MIPSCode.END

    def emitTEXT(self):   
        return MIPSCode.INDENT + ".text" + MIPSCode.END

    def emitADD(self, rd, rs, rt):
        return MIPSCode.INDENT + "add\t\t" + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitADDU(self, rd, rs, rt):
        return MIPSCode.INDENT + "addu\t" + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitSUB(self, rd, rs, rt):
        return MIPSCode.INDENT + "sub\t\t" + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitSUBU(self, rd, rs, rt):
        return MIPSCode.INDENT + "subu\t" + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitADDI(self, rt, rs, imm):
        return MIPSCode.INDENT + "addi\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitADDIU(self, rt, rs, imm):
        return MIPSCode.INDENT + "addiu\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitMULT(self, rs, rt):
        return MIPSCode.INDENT + "mult\t" + ", ".join([rs, rt]) + MIPSCode.END

    def emitMULTU(self, rs, rt):
        return MIPSCode.INDENT + "multu\t" + ", ".join([rs, rt]) + MIPSCode.END

    def emitDIV(self, rs, rt):
        return MIPSCode.INDENT + "div\t\t" + ", ".join([rs, rt]) + MIPSCode.END

    def emitDIVU(self, rs, rt):
        return MIPSCode.INDENT + "divu\t" + ", ".join([rs, rt]) + MIPSCode.END

    def emitMFHI(self, rd):
        return MIPSCode.INDENT + "mfhi\t" + rd + MIPSCode.END

    def emitMFLO(self, rd):
        return MIPSCode.INDENT + "mflo\t" + rd + MIPSCode.END

    def emitAND(self, rd, rs, rt):
        return MIPSCode.INDENT + "and\t\t" + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "or\t\t" + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitNOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "nor\t\t" + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitXOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "xor\t\t" + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitANDI(self, rt, rs, imm):
        return MIPSCode.INDENT + "andi\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitORI(self, rt, rs, imm):
        return MIPSCode.INDENT + "ori\t\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitXORI(self, rt, rs, imm):
        return MIPSCode.INDENT + "xori\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLL(self, rd, rt, sh):
        return MIPSCode.INDENT + "sll\t\t" + ", ".join([rd, rt, sh]) + MIPSCode.END

    def emitSRL(self, rd, rt, sh):
        return MIPSCode.INDENT + "sll\t\t" + ", ".join([rd, rt, sh]) + MIPSCode.END

    def emitLUI(self, rt, imm):
        return MIPSCode.INDENT + "lui\t\t" + ", ".join([rt, str(imm)]) + MIPSCode.END

    def emitLW(self, rt, rs, imm):
        return MIPSCode.INDENT + "lw\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLH(self, rt, rs, imm):
        return MIPSCode.INDENT + "lh\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLB(self, rt, rs, imm):
        return MIPSCode.INDENT + "lb\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLHU(self, rt, rs, imm):
        return MIPSCode.INDENT + "lhu\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLBU(self, rt, rs, imm):
        return MIPSCode.INDENT + "lbu\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSW(self, rt, rs, imm):
        return MIPSCode.INDENT + "sw\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSH(self, rt, rs, imm):
        return MIPSCode.INDENT + "sh\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSB(self, rt, rs, imm):
        return MIPSCode.INDENT + "sb\t\t" + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitJ(self, addr):
        return MIPSCode.INDENT + "j\t\t" + addr + MIPSCode.END

    def emitJR(self, rs):
        return MIPSCode.INDENT + "jr\t\t" + rs + MIPSCode.END

    def emitJAL(self, addr):
        return MIPSCode.INDENT + "jal\t\t" + addr + MIPSCode.END

    def emitBEQ(self, rt, rs, imm):
        return MIPSCode.INDENT + "beq\t\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitBNE(self, rt, rs, imm):
        return MIPSCode.INDENT + "bne\t\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLT(self, rd, rs, rt):
        return MIPSCode.INDENT + "slt\t\t" + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitSLTU(self, rd, rs, rt):
        return MIPSCode.INDENT + "sltu\t" + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitSLTI(self, rt, rs, imm):
        return MIPSCode.INDENT + "slti\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLTIU(self, rt, rs, imm):
        return MIPSCode.INDENT + "sltiu\t" + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitBEQ(self, rx, ry, imm):
        return MIPSCode.INDENT + "beq\t\t" + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBGE(self, rx, ry, imm):
        return MIPSCode.INDENT + "bge\t\t" + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBGT(self, rx, ry, imm):
        return MIPSCode.INDENT + "bgt\t\t" + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBLE(self, rx, ry, imm):
        return MIPSCode.INDENT + "ble\t\t" + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBLT(self, rx, ry, imm):
        return MIPSCode.INDENT + "blt\t\t" + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitLA(self, rx, label):
        return MIPSCode.INDENT + "la\t\t" + ", ".join([rx, label]) + MIPSCode.END

    def emitLI(self, rx, imm):
        return MIPSCode.INDENT + "li\t\t" + ", ".join([rx, str(imm)]) + MIPSCode.END

    def emitMOVE(self, rx, ry):
        return MIPSCode.INDENT + "move\t" + ", ".join([rx, ry]) + MIPSCode.END

    def emitNOP(self):
        return MIPSCode.INDENT + "nop" + MIPSCode.END

    def emitSYSCALL(self):
        return MIPSCode.INDENT + "syscall" + MIPSCode.END

    def emitMTC1(self, r, fr):
        return MIPSCode.INDENT + "mtc1\t" + ", ".join([r, fr]) + MIPSCode.END

    def emitCVTSW(self, fr1, fr2):
        return MIPSCode.INDENT + "cvt.s.w\t" + ", ".join([fr1, fr2]) + MIPSCode.END

    def emitADDS(self, frd, fr1, fr2):
        return MIPSCode.INDENT + "add.s\t" + ", ".join([frd, fr1, fr2]) + MIPSCode.END
