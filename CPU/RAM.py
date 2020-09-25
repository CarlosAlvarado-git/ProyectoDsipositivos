from ROM import ROM
import os
class RAM:
    #def __init__ (self):---
    def __init__ (self):
        R = ROM()
        self.data = R.getdata()
        self.instructioncon = []
        self.path = os.getcwd()
        #cpufm = open(self.path + "\\CPU\\1.cpufm", "r")---

        opcion = 0
        while(opcion < 1 or opcion > 7):
            print(" 1: 1.cpufm\n 2: 2.cpufm\n 3: 3.cpufm\n 4: 4.cpufm\n 5: 5.cpufm\n 6: 6.cpufm\n 7: 7.cpufm\n")
            opcion = int(input("Ingrese el numero del programa que desea ejecutar: "))
            if(opcion == 1):
                archivo = "1.cpufm"
            elif(opcion == 2):
                archivo = "2.cpufm"
            elif(opcion == 3):
                archivo = "3.cpufm"
            elif(opcion == 4):
                archivo = "4.cpufm"
            elif(opcion == 5):
                archivo = "5.cpufm"
            elif(opcion == 6):
                archivo = "6.cpufm"
            elif(opcion == 7):
                archivo = "7.cpufm"
            else:
                print(f"El numero {opcion} no esta en el rango")


        cpufm = open(self.path + "\\CPU\\" + archivo, "r")
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