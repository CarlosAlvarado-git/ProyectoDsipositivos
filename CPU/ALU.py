import Integratedcircuit
class ALU(Integratedcircuit):
    zero = False
    Overflow = False
    Negative = False 
    
    def __init__ (self, Opcode,Input):
        self.Opcode = Opcode
        self.Input = Input
        pass
    
    def Add(self, R0, R1):
        # var = R0 + R1 (Si me da más de 15, veo si es par o impar y lo trunco)
        # R0 = var (si es par, 14.)
        # overflow lo vuelvo  true. lo imprimo. luego otra vez false. eso con todo. 
        # si la suma da más de 15, si el número es par, lo truncamos a 14 y si es impar lo truncamos a 15
        pass
    def Subtraction(self, R0, R1): # llamo a esta si R0 es más grande que R1, sino llamo a Borrow
        # si la resta es 0, la variables Zero la vuelvo True
        pass
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
        pass