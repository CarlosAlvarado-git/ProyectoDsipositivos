from Integratedcircuit import IC
#from ALU import ALU
#from RAM import RAM
#from Register import Register
#from ROM import ROM
#from Clock import Clock
class Register(IC):
    def ingresarvalor(self, valorderam):
        valorderam = str(valorderam)
        if(valorderam.isdigit() == True):
            self.VRam = int(valorderam)
        else:
            self.VRam = valorderam
