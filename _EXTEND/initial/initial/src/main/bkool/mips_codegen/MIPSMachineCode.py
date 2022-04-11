

class MIPSCode:

    END = '\n'
    INDENT = '\t'

    def emitDATA(self):
        return MIPSCode.INDENT + ".data" + MIPSCode.END

    def emitTEXT(self):   
        return MIPSCode.INDENT + ".text" + MIPSCode.END

    def emitADD(self, rd, rs, rt):
        return MIPSCode.INDENT + "add " + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitADDU(self, rd, rs, rt):
        return MIPSCode.INDENT + "addu " + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitSUB(self, rd, rs, rt):
        return MIPSCode.INDENT + "sub " + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitSUBU(self, rd, rs, rt):
        return MIPSCode.INDENT + "subu "+  ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitADDI(self, rt, rs, imm):
        return MIPSCode.INDENT + "addi " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitADDIU(self, rt, rs, imm):
        return MIPSCode.INDENT + "addiu " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitMULT(self, rs, rt):
        return MIPSCode.INDENT + "mult " + ", ".join([rs, rt]) + MIPSCode.END

    def emitMULTU(self, rs, rt):
        return MIPSCode.INDENT + "multu " + ", ".join([rs, rt]) + MIPSCode.END

    def emitDIV(self, rs, rt):
        return MIPSCode.INDENT + "div " + ", ".join([rs, rt]) + MIPSCode.END

    def emitDIVU(self, rs, rt):
        return MIPSCode.INDENT + "divu " + ", ".join([rs, rt]) + MIPSCode.END

    def emitMFHI(self, rd):
        return MIPSCode.INDENT + "mfhi " + rd + MIPSCode.END

    def emitMFLO(self, rd):
        return MIPSCode.INDENT + "mflo " + rd + MIPSCode.END

    def emitAND(self, rd, rs, rt):
        return MIPSCode.INDENT + "and " + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "or " + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitNOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "nor " + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitXOR(self, rd, rs, rt):
        return MIPSCode.INDENT + "xor " + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitANDI(self, rt, rs, imm):
        return MIPSCode.INDENT + "andi " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitORI(self, rt, rs, imm):
        return MIPSCode.INDENT + "ori " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitXORI(self, rt, rs, imm):
        return MIPSCode.INDENT + "xori " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLL(self, rd, rt, sh):
        return MIPSCode.INDENT + "sll " + ", ".join([rd, rt, sh]) + MIPSCode.END

    def emitSRL(self, rd, rt, sh):
        return MIPSCode.INDENT + "sll " + ", ".join([rd, rt, sh]) + MIPSCode.END

    def emitLUI(self, rt, imm):
        return MIPSCode.INDENT + "lui " + ", ".join([rt, str(imm)]) + MIPSCode.END

    def emitLW(self, rt, rs, imm):
        return MIPSCode.INDENT + "lw " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLH(self, rt, rs, imm):
        return MIPSCode.INDENT + "lh " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLB(self, rt, rs, imm):
        return MIPSCode.INDENT + "lb " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLHU(self, rt, rs, imm):
        return MIPSCode.INDENT + "lhu " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitLBU(self, rt, rs, imm):
        return MIPSCode.INDENT + "lbu " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSW(self, rt, rs, imm):
        return MIPSCode.INDENT + "sw " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSH(self, rt, rs, imm):
        return MIPSCode.INDENT + "sh " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitSB(self, rt, rs, imm):
        return MIPSCode.INDENT + "sb " + rt + ", " + str(imm) + "(" + rs + ")" + MIPSCode.END

    def emitJ(self, addr):
        return MIPSCode.INDENT + "j " + addr + MIPSCode.END

    def emitJR(self, rs):
        return MIPSCode.INDENT + "jr " + rs + MIPSCode.END

    def emitJAL(self, addr):
        return MIPSCode.INDENT + "jal " + addr + MIPSCode.END

    def emitBEQ(self, rt, rs, imm):
        return MIPSCode.INDENT + "beq " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitBNE(self, rt, rs, imm):
        return MIPSCode.INDENT + "bne " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLT(self, rd, rs, rt):
        return MIPSCode.INDENT + "slt " + ", ".join([rd, rs, rt]) +  MIPSCode.END

    def emitSLTU(self, rd, rs, rt):
        return MIPSCode.INDENT + "sltu " + ", ".join([rd, rs, rt]) + MIPSCode.END

    def emitSLTI(self, rt, rs, imm):
        return MIPSCode.INDENT + "slti " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitSLTIU(self, rt, rs, imm):
        return MIPSCode.INDENT + "sltiu " + ", ".join([rt, rs, str(imm)]) + MIPSCode.END

    def emitBEQ(self, rx, ry, imm):
        return MIPSCode.INDENT + "beq " + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBGE(self, rx, ry, imm):
        return MIPSCode.INDENT + "bge " + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBGT(self, rx, ry, imm):
        return MIPSCode.INDENT + "bgt " + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBLE(self, rx, ry, imm):
        return MIPSCode.INDENT + "ble " + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitBLT(self, rx, ry, imm):
        return MIPSCode.INDENT + "blt " + ", ".join([rx, ry, str(imm)]) +  MIPSCode.END

    def emitLA(self, rx, label):
        return MIPSCode.INDENT + "la " + ", ".join([rx, label]) + MIPSCode.END

    def emitLI(self, rx, imm):
        return MIPSCode.INDENT + "li " + ", ".join([rx, str(imm)]) + MIPSCode.END

    def emitMOVE(self, rx, ry):
        return MIPSCode.INDENT + "move " + ", ".join([rx, ry]) + MIPSCode.END

    def emitNOP(self):
        return MIPSCode.INDENT + "nop" + MIPSCode.END

    def emitSYSCALL(self):
        return MIPSCode.INDENT + "syscall" + MIPSCode.END