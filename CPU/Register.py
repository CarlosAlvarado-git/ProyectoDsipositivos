#import Integratedcircuit
class Register:
    def __init__ (self, valorderam):
        valorderam = str(valorderam)
        if(valorderam.isdigit() == True):
            self.VRam = int(valorderam)
        else:
            self.VRam = valorderam
