import yaml
import os
class ROM:
    def __init__ (self):
        #Aqui se carga el instruction set table------------------------------------------
        path = os.getcwd()
        self.ROM = open(path + "\\CPU\\Instruction.txt", "r")
        self.Rom_array = []
        for linea in self.ROM.readlines():
            self.Rom_array.append(linea)

        #leo el archivo y guardo en lo que esta en la tabla de Set Instruccion.
        #prueba
        #Aqui se termina el instruction set table-----------------------------------------


        #Aqui se carga el Bios yml---------------------------------------------------
        with open(path + "\\CPU\\Bios.yaml","r") as ymlfile:
            self.cfg = yaml.load(ymlfile)

        for section in self.cfg:           
            self.clock = self.cfg["clock"]
            self.visualizacion = self.cfg["visualization"]
            self.ram_ = self.cfg["RAM"]
            self.data = self.ram_.get("data")
            self.instruction = self.ram_.get("instructions")
        #Aqui se termina de cargar el BIOS yml-----------------------------------------------  
    
    def getclock(self):
        return self.clock

    def getvisualizacion(self):
        return self.visualizacion
        
    def getdata(self):
        return self.data

    def BuscarInstru(self, buscar):
        instruc = ""
        for i in range(len(self.Rom_array)):
            strin = str(self.Rom_array[i])
            #print(buscar)
            if(strin.find(buscar) != -1):
                if(buscar == "OR"):
                    instruc = "self.alu.OR(data, self.Registros)"
                    break
                else:
                    pinicial = int(1 + int(strin.find("#")))
                    pfinal = strin.find("!")
                    instruc =  strin[pinicial: pfinal]
                    break
            else:
                instruc = "detener(len(ram.instruction))"
        
        return instruc