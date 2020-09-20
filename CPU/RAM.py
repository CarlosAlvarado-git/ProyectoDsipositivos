import yaml 
data = [] 
class RAM:
    def __init__ (self):
        with open("RAM.yaml","r") as ymlfile:
            self.cfg = yaml.load(ymlfile)

        #for section in self.cfg:
         #   print(section)
        #print(self.cfg["visualization"])
        self.clock = self.cfg["clock"]
        self.visualizacion = self.cfg["visualization"]
        self.ram_ = self.cfg["RAM"]
        self.data = self.ram_.get("data")
        self.instruction = self.ram_.get("instructions")
        #print(ram_)
        #print(data)

        #data = cfg["data"]
        #instructions = cfg["instructions"]
        #leo el archivo y guardo en arrays la data y las instrucction. Los bios.yaml
        # self.RData = lo que está en data del archivo.
        pass
    #hola = RAM()
    def valorData(self, valor):
        valor = int(valor)
        return self.data[valor]
        pass

    def insertarValor(self,valor, data):
        pass
    # una funcion que retorne el valor de data: valorData(data)
    # Store_R0: En el array RData 