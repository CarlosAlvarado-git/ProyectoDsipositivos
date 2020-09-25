from ROM import ROM
import os
class RAM:
    def __init__ (self):
    #def __init__ (self, archivo):
        R = ROM()
        self.data = R.getdata()
        self.instructioncon = []
        self.path = os.getcwd()
        cpufm = open(self.path + "\\CPU\\1.cpufm", "r")
        #cpufm = open(self.path + "\\CPU\\" + archivo, "r")
        for linea in cpufm.readlines():
            self.instructioncon.append(linea)
        
        self.instruction = []
        for l in self.instructioncon:
            if(l.find(";") == -1):
                self.instruction.append(l)
        
        #for section in self.cfg:
         #   print(section)
        #print(self.cfg["visualization"])
        #self.clock = self.cfg["clock"]
        #self.visualizacion = self.cfg["visualization"]
        #print(ram_)
        #print(data)
        #data = cfg["data"]
        #instructions = cfg["instructions"]
        #leo el archivo y guardo en arrays la data y las instrucction. Los bios.yaml
        # self.RData = lo que está en data del archivo.
        pass
    #hola = RAM()

    def getRam(self):
        return self.data
    
    def valorData(self, valor):#Método usado para extraer un valor de la dada
        if(len(valor) <= 2):
            valor = int(valor)
            if(valor >= 0 and valor <= 15):
                return self.data[valor]
            else:
                return -1
        elif(len(valor) == 4):
            #convertir de binario a decimal.
            valor = int(str(valor), 2)
            if(valor >= 0 and valor <= 15):
                return self.data[valor]
            else:
                return -1
        

    def InsertarValor(self,valor, datas):
        #Método usado para escribir un valor en la data
        if(len(datas) <= 2):
            datas = int(datas)
            if(datas >= 0 and datas <= 15):
                self.data[datas] = valor
                print(f"STORE en registro {datas} el valor de: {valor}")
            else:
                #CU.detener(len(self.instruction))
                pass
        elif(len(datas) == 4):
            #convertir de binario a decimal.
            datas = int(str(datas), 2)
            if(datas >= 0 and datas <= 15):
                self.data[datas] = valor
                print(f"STORE en registro {datas} el valor de: {valor}")
            else:
                #CU.detener(len(self.instruction))
                pass
    # una funcion que retorne el valor de data: valorData(data)
    # Store_R0: En el array RData