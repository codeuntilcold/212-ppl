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

class Register:
    def __init__(self):
        pass

    def resetRegisters(self):
        self.registerDescriptor = {
			T0: None, T1: None, T2: None, T3: None, T4: None, 
            T5: None, T6: None, T7: None, T8: None, T9: None, 
            S0: None, S1: None, S2: None, S3: None, S4: None 
        }
        self.busyRegisters = []
        self.freeRegisters = []
        for register in self.registerDescriptor.keys():
            self.freeRegisters.append(register)

    def getRegister(self, temp):
        if temp in self.registerDescriptor.values():
            register = self.ST.addressDescriptor[temp]['register']
        else:
            if len(self.freeRegisters) == 0:
                register = self.busyRegisters.pop(0)
                tempReg = self.registerDescriptor[register]
                self.ST.addressDescriptor[tempReg]['register'] = None
                self.registerDescriptor[register] = temp
                
                if self.ST.addressDescriptor[tempReg]['memory'] != None:
                    (level, offset) = self.ST.addressDescriptor[tempReg]['memory']
                    self.putAbsoluteAddressInRegister(level, offset)
                    self.addLineToCode(['sw', register, '0($s7)', ''])
                    self.ST.addressDescriptor[tempReg]['store'] = True

                if self.ST.addressDescriptor[temp]['memory'] != None:
                    (level, offset) = self.ST.addressDescriptor[temp]['memory']
                    self.putAbsoluteAddressInRegister(level, offset)
                    self.addLineToCode(['lw', register, '0($s7)', ''])	
            else:
                register = self.freeRegisters.pop()
                if self.ST.addressDescriptor[temp]['memory'] != None and self.ST.addressDescriptor[temp]['store']:
                    (level, offset) = self.ST.addressDescriptor[temp]['memory']
                    # print (level, offset)
                    self.putAbsoluteAddressInRegister(level, offset)
                    self.addLineToCode(['lw', register, '0($s7)', ''])
            
            self.ST.addressDescriptor[temp]['register'] = register
            self.busyRegisters.append(register)
            self.registerDescriptor[register] = temp

        return register