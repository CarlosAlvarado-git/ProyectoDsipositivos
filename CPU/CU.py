#import Integratedcircuit
from ROM import ROM
from ALU import ALU
from RAM import RAM
from Register import Register
R0 = Register(-1)
R1 = Register(-1)
def CargarRegistroR0(insertar):
    global R0
    R0.VRam = insertar
    #print(R0.VRam)
def CargarRegistroR1(insertar):
    global R1
    R1.VRam = insertar
    #print(R1.VRam)
if __name__ == "__main__":
    rom = ROM()
    ram = RAM()
    cpufm = open("1.cpufm", "r")
    cpufm_Instruc = []
    for linea in cpufm.readlines():
        cpufm_Instruc.append(linea)
    #ram = RAM()
    RAM.cargarInstruccion()
    print(cpufm_Instruc)
    for i in range (len(cpufm_Instruc)):
        strin = str(cpufm_Instruc[i])
        if(strin.find(";")!= -1):
            pass
        else:
           pincio = 0
           pfinal = strin.find(" ")
           buscar = strin[:pfinal]
           pincio = pfinal
           pfinal = strin.find(" ", pfinal+1)
           data = strin[pincio+1: pfinal]
           #print(buscar)
           #print(data)
           instruction = rom.BuscarInstru(buscar, R0, R1, data)
           #print(instruction)
           eval(instruction)
           break

        
    
    #ram = RAM()
    #instruction = rom.BuscarInstru(buscar, R0, R1, data)
    #eval(instruction)


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