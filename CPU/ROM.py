class ROM:
    def __init__ (self):
        self.ROM = open("Instruction.txt", "r")
        self.Rom_array = []
        for linea in self.Rom.readlines():
            self.Rom_array.append(linea)
        for i in range (len(self.Rom_array)):  
            print(f" : {self.Rom_array[i]} \n")
        #leo el archivo y guardo en lo que esta en la tabla de Set Instruccion.
        #prueba
    def BuscarInstru(buscar, R0, R1, data):
        #for i in range(len(ROM.int)):
            # p = ""
            # while(p == "- -")
                # str = ROM.int[i]
                # busco el - p = 0000
                # if(p == buscar):
                    # s = str[se corta la parte de intruction]
                    # eval(s)
        pass