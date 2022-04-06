
class MIPSCodeGenerator:

    def gen(self, ast, dir):
        f = open(dir + "/BKOOLClass.asm", "w")
        file_mac_dinh = open("./test.asm", "r")
        f.write(file_mac_dinh.read())
        f.close()
