#import Integratedcircuit
class ALU:
    def __init__ (self):
        #self.Opcode = Opcode
        #self.Input = Input
        self.Zero = False
        self.Z = 0
        self.Overflow = False
        self.O = 0
        self.Negative = False 
        self.N = 0
        self.Igual = False
        self.Mayor = False
        self.Menor = False
        
    #Add(self, data, Register R0, R1, R2, R3)
    #la data de divede y se ve que registro es. "00 0 R0" = R0, 01 = R1, 10 = R2, 11 = R3
    def reset(self):
        self.Zero = False
        self.Overflow = False
        self.Negative = False
        self.Igual = False
        self.Mayor = False
        self.Meno = False
        
    def EncontrarReg(self, data):
        bit1 = data[0:2]
        x = 0
        if(bit1 == "00" or bit1 == "R0"):
            x = 0
            return x
        elif(bit1 == "01" or bit1 == "R1"):
            x = 1
            return x
        elif(bit1 == "10" or bit1 == "R2"):
            x = 2
            return x
        elif(bit1 == "11" or bit1 == "R3"):
            x = 3
            return x
    def EncontrarReg2(self, data):
        bit1 = data[2:4]
        #print(f"Esto es bit1 en la segunda funcion: {bit1} y esto es data: {data}")
        x = 0
        if(bit1 == "00" or bit1 == "R0"):
            x = 0
            return x
        elif(bit1 == "01" or bit1 == "R1"):
            x = 1
            return x
        elif(bit1 == "10" or bit1 == "R2"):
            x = 2
            return x
        elif(bit1 == "11" or bit1 == "R3"):
            x = 3
            return x
    def Add(self, data, Registros): #modificarlo para que sea con referencia y así de una se cambie el valor.
        #data = data.replace(" ", "")
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        #print(type(Registros))
        #print(type(x))
        #print(type(y))
        Registros[y].VRam = Registros[x].VRam + Registros[y].VRam
        self.Simbols(Registros[y].VRam,15,">")
        if (self.Mayor == True):
            self.Overflow = True
            self.O = self.O + 1
            if (Registros[y].VRam % 2 == 0):
                Registros[y].VRam = 14
            else:
                Registros[y].VRam = 15
        self.Simbols(Registros[y].VRam,0,"==")
        if(self.Igual == True):
            self.zero = True
        print(f"Suma de registros: {data[0:2]} y {data[2:4]}, poniendo el resultado en {data[2:4]}")
        # var = R0 + R1 (Si me da más de 15, veo si es par o impar y lo trunco)
        # R0 = var (si es par, 14.)
        # overflow lo vuelvo  true. lo imprimo. luego otra vez false. eso con todo. 
        # si la suma da más de 15, si el número es par, lo truncamos a 14 y si es impar lo truncamos a 15 
    def Subtraction(self, data, Registros): 
        #data = data.replace(" ", "")
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        Registros[y].VRam = Registros[x].VRam - Registros[y].VRam
        self.Simbols(Registros[y].VRam,0,"==")
        if(self.Igual == True):
            self.zero = True
            self.Z = self.Z + 1
        self.Simbols(Registros[y].VRam,0,"<")
        if(self.Menor == True):
            self.Substract_with_borrow(Registros, y)
            print(f"Sub with borrow a los registros {data[0:2]} y {data[2:4]} poniendo el valor en {data[2:4]}")
        else:
            print(f"Sub a los registros {data[0:2]} y {data[2:4]} poniendo el valor en {data[2:4]}")
        # llamo a esta si R0 es más grande que R1, sino llamo a Borrow
        # si la resta es 0, la variables Zero la vuelvo True
        
    def Substract_with_borrow(self, Registros,y):#llamar al ser la resta negativa.
        self.Negative = True
        self.N = self.N + 1
        Registros[y].VRam = (Registros[y].VRam)*(-1)
        
    def Ocomplement(self,dato):
        dato = bin(dato)[2:]
        for i in dato:
            if (dato[i]=="1"):
                dato[i] = "0"
            elif (dato[i]=="0"):
                dato[i] = "1"
        dato = int(str(dato),2)
        return dato

    def Twcomplement(self,dato):
        dato = self.Ocomplement(dato) + 1
        return dato
        
    def AND(self,data,Registros):
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        Registros[y].VRam = Registros[x].VRam and Registros[y].VRam
        
    def OR(self, data, Registros):
        x = self.EncontrarReg(data)
        y = self.EncontrarReg2(data)
        Registros[y].VRam = Registros[x].VRam or Registros[y].VRam

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