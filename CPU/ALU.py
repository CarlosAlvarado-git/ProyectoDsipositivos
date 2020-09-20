#import Integratedcircuit
class ALU:
    zero = False
    Overflow = False
    Negative = False 
    Igual = False
    Mayor = False
    Menor = False
    def __init__ (self, Opcode,Input):
        self.Opcode = Opcode
        self.Input = Input
        
    
    def Add(self, R0, R1): #modificarlo para que sea con referencia y así de una se cambie el valor.
        R1 = R0 + R1
        self.Simbols(R1,15,">")

        if (self.Mayor == True):
            self.Overflow = True
            if (R1 % 2 == 0):
                R1 = 14
            else:
                R1 = 15
        self.Simbols(R1,0,"<")
        if (self.Menor == True):
            self.Negative == True
        self.Simbols(R1,0,"==")
        if(self.Igual == True):
            self.zero = True
        # var = R0 + R1 (Si me da más de 15, veo si es par o impar y lo trunco)
        # R0 = var (si es par, 14.)
        # overflow lo vuelvo  true. lo imprimo. luego otra vez false. eso con todo. 
        # si la suma da más de 15, si el número es par, lo truncamos a 14 y si es impar lo truncamos a 15
        
    def Subtraction(self, R0, R1): 
        R1 = R0- R1
        self.simbols(R1,0,"==")
        if(self.Igual == True):
            self.zero = True
        self.simbols(R1,0,"<")
        if(self.menor == True):
            self.Negative = True
        # llamo a esta si R0 es más grande que R1, sino llamo a Borrow
        # si la resta es 0, la variables Zero la vuelvo True
        
    def Subtract_with_borrow(self):
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
        Mayor = False
        Menor = False
        Igual = False
        if (simbolo == ">"):
            if(R1 > R0):
                Mayor = True
        elif (simbolo == "<"):
            if(R1 < R0):
                Menor = True
        elif (simbolo == "=="):
            if(R1 == R0):
                Igual = True
        elif (simbolo == ">="):
            if(R1 >= R0):
                Mayor = True
                Igual = True
        elif (simbolo == "<="):
            if (R1 <= R0):
                Menor = True
                Igual = True
        elif (simbolo == "!="):
            if(R1 != R0):
                Igual = False
        pass