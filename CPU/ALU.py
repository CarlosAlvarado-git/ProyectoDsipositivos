#import Integratedcircuit
class ALU:
    def __init__ (self, Opcode,Input):
        self.Opcode = Opcode
        self.Input = Input
        self.zero = False
        self.Overflow = False
        self.Negative = False 
        self.Igual = False
        self.Mayor = False
        self.Menor = False
        
    #Add(self, data, Register R0, R1, R2, R3)
    #la data de divede y se ve que registro es. "00 0 R0" = R0, 01 = R1, 10 = R2, 11 = R3
    def Add(self, x, y): #modificarlo para que sea con referencia y así de una se cambie el valor.
        y.VRam = x.VRam + y.VRam
        self.Simbols(y,15,">")
        if (self.Mayor == True):
            self.Overflow = True
            if (y % 2 == 0):
                y = 14
            else:
                y = 15
        self.Simbols(y,0,"<")
        if (self.Menor == True):
            self.Negative == True
        self.Simbols(y,0,"==")
        if(self.Igual == True):
            self.zero = True
        # var = R0 + R1 (Si me da más de 15, veo si es par o impar y lo trunco)
        # R0 = var (si es par, 14.)
        # overflow lo vuelvo  true. lo imprimo. luego otra vez false. eso con todo. 
        # si la suma da más de 15, si el número es par, lo truncamos a 14 y si es impar lo truncamos a 15
        
    def Subtraction(self, R0, R1): 
        R1.VRam = R0.VRam - R1.VRam
        self.Simbols(R1,0,"==")
        if(self.Igual == True):
            self.zero = True
        self.Simbols(R1,0,"<")
        if(self.Menor == True):
            self.Negative = True
        # llamo a esta si R0 es más grande que R1, sino llamo a Borrow
        # si la resta es 0, la variables Zero la vuelvo True
        
    def Subtract_with_borrow(self):#llamar al ser la resta negativa.
        pass
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