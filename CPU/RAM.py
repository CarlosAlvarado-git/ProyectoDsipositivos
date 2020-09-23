from ROM import ROM
import os
class RAM:
    def __init__ (self):
        R = ROM()
        self.data = R.getdata()
        self.instruction = []
        self.path = os.getcwd()
        cpufm = open(self.path + "\\CPU\\1.cpufm", "r")
        for linea in cpufm.readlines():
            self.instruction.append(linea)
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
    def valorData(self, valor):#Método usado para extraer un valor de la dada
        if(len(valor) <= 2):
            valor = int(valor)
        elif(len(valor) == 4):
            #convertir de binario a decimal.
            valor = int(str(valor), 2)
        return self.data[valor]

    def insertarValor(self,valor, data):
        #Método usado para escribir un valor en la data
        self.data[valor] = data
    # una funcion que retorne el valor de data: valorData(data)
    # Store_R0: En el array RData