#import Integratedcircuit
if __name__ == "__main__":
    from ROM import ROM
    rom = ROM()
    R0 = "Regristro 0"
    R1 = "Regristro 1"
    data = 13
    buscar = "0000"
    instruction = rom.BuscarInstru(buscar, R0, R1, data)
    eval(instruction)


#def __init__(self):
     #   pass
    #is the main controller for everything, it
    #is where everything is orchestrated. It should be the one
    #responsible for Fetch, Decode , Execute (send instruction decoded
    #to ALU if needed).
    #Se debería de leer los cpufm files.
    #Leer los comandos que el usuario ingrese
    #ya leí todo.
    # identificar las intrucciones del CPU
    # RAM es lo del archivo bios.yaml
    # Si es LOAD_R0 14, significa que creo un registro  que contiene lo que está en RAM(lo que tiene 14 en RAM.data).
    # Registro R0 = new Registro((Lo de la RAM.Data en la posición 14))
    # el array de RAM.data obtiene lo del archivo y luego de las operaciones se cambia.
    # primero ROM y luego Alu. 
    # al llamar ver que quiere restar, vero el orden, veo cual es mayor, y ya debende de eso uso Sub o Sub con borrow
    # a la ROM le mando la instrucions ROM.BuscarInstru(R0, R1, data)