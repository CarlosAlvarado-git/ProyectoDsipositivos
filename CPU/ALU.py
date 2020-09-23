#import Integratedcircuit
class ALU:
    def __init__ (self):
        #self.Opcode = Opcode
        #self.Input = Input
        self.zero = False
        self.Overflow = False
        self.Negative = False 
        self.Igual = False
        self.Mayor = False
        self.Menor = False
        
    #Add(self, data, Register R0, R1, R2, R3)
    #la data de divede y se ve que registro es. "00 0 R0" = R0, 01 = R1, 10 = R2, 11 = R3
    def EncontrarReg(self, data):
        bit1 = data[0:2]
        x = 0
        if(bit1 == "00" or bit1 == "R0"):
            x = 0
            return int(x)
        elif(bit1 == "01" or bit1 == "R1"):
            x = 1
            return int(x)
        elif(bit1 == "10" or bit1 == "R2"):
            x = 2
            return int(x)
        elif(bit1 == "11" or bit1 == "R3"):
            x = 3
            return int(x)
    def EncontrarReg2(self, data):
        bit2 = data[2:4]
        y = 0
        if(bit2 == "00" or bit2 == "R0"):
            y = 0
            return int(y)
        elif(bit2 == "01" or bit2 == "R1"):
            y = 1
            return int(y)
        elif(bit2 == "10" or bit2 == "R2"):
            y = 2
            return int(y)
        elif(bit2 == "11" or bit2 == "R3"):
            y = 3
            return int(y)
    def Add(self, data, Registros): #modificarlo para que sea con referencia y así de una se cambie el valor.
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        Registros[y].VRam = Registros[x].VRam + Registros[y].VRam
        self.Simbols(Registros[y].VRam,15,">")
        if (self.Mayor == True):
            self.Overflow = True
            if (Registros[y].VRam % 2 == 0):
                Registros[y].VRam = 14
            else:
                Registros[y].VRam = 15
        self.Simbols(Registros[y].VRam,0,"<")
        if (self.Menor == True):
            self.Negative == True
        self.Simbols(Registros[y].VRam,0,"==")
        if(self.Igual == True):
            self.zero = True
        # var = R0 + R1 (Si me da más de 15, veo si es par o impar y lo trunco)
        # R0 = var (si es par, 14.)
        # overflow lo vuelvo  true. lo imprimo. luego otra vez false. eso con todo. 
        # si la suma da más de 15, si el número es par, lo truncamos a 14 y si es impar lo truncamos a 15 
    def Subtraction(self, data, Registros): 
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        Registros[y].VRam = Registros[x].VRam - Registros[y].VRam
        self.Simbols(Registros[y].VRam,0,"==")
        if(self.Igual == True):
            self.zero = True
        self.Simbols(Registros[y].VRam,0,"<")
        if(self.Menor == True):
            self.Substract_with_borrow(Registros, y)
        # llamo a esta si R0 es más grande que R1, sino llamo a Borrow
        # si la resta es 0, la variables Zero la vuelvo True
        
    def Subtract_with_borrow(self, Registros,y):#llamar al ser la resta negativa.
        self.Negative = True
        Registros[y].VRam = (Registros[y].VRam)*(-1)
        
    def Ocomplement(self):
        pass
    def Twcomplement(self):
        pass
    def AND(self):
        pass
    def OR(self):
        pass
    def shift(self):
        pass
    def Simbols(self, R1, R0, simbolo):
        #self.Mayor = False
        #self.Menor = False
        #self.Igual = False
        if (simbolo == ">"):
            if(R1 > R0):
                self.Mayor = True
        elif (simbolo == "<"):
            if(R1 < R0):
                self.Menor = True
        elif (simbolo == "=="):
            if(R1 == R0):
                self.Igual = True
        elif (simbolo == ">="):
            if(R1 >= R0):
                self.Mayor = True
                self.Igual = True
        elif (simbolo == "<="):
            if (R1 <= R0):
                self.Menor = True
                self.Igual = True
        elif (simbolo == "!="):
            if(R1 != R0):
                self.Igual = False
        pass