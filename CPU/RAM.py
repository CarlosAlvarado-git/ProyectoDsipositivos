from ROM import ROM
class RAM:
    def __init__ (self):
        R = ROM()
        self.data = R.getdata()
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
    def valorData(self, valor):
        #Método usado para extraer un valor de la dada
        valor = int(valor)
        return self.data[valor]

    def insertarValor(self,valor, data):
        #Método usado para escribir un valor en la data
        self.data[valor] = data
    # una funcion que retorne el valor de data: valorData(data)
    # Store_R0: En el array RData