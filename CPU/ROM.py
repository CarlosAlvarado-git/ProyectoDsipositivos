class ROM:
    def __init__ (self):
        self.ROM = open("Instruction.txt", "r")
        self.Rom_array = []
        for linea in self.ROM.readlines():
            self.Rom_array.append(linea)
        #leo el archivo y guardo en lo que esta en la tabla de Set Instruccion.
        #prueba
    def BuscarInstru(self, buscar, R0, R1, data):
        for i in range(len(self.Rom_array)):
            strin = str(self.Rom_array[i])
           
            if(strin.find(buscar) != -1):
                pinicial = int(1 + int(strin.find("#")))
                pfinal = strin.find("!")
                instruc =  strin[pinicial: pfinal]
                return instruc