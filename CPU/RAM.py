import yaml  
class RAM:
    def __init__ (self):
        with open("RAM.yaml","r") as ymlfile:
            cfg = yaml.load(ymlfile)

        for section in cfg:
            print(section)
        print(cfg["visualization"])
        clock = cfg["clock"]
        visualizacion = cfg["visualization"]
        ram_ = cfg["RAM"]
        data = ram_.get("data")
        instruction = ram_.get("instructions")
        print(ram_)
        print(data)

        #data = cfg["data"]
        #instructions = cfg["instructions"]
        #leo el archivo y guardo en arrays la data y las instrucction. Los bios.yaml
        # self.RData = lo que está en data del archivo.
        pass
    #hola = RAM()
    def valorData(self, valor):
        pass

    def insertarValor(self,valor, data):
        pass
    # una funcion que retorne el valor de data: valorData(data)
    # Store_R0: En el array RData 