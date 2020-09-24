#import Integratedcircuit
from Integratedcircuit import IC
from ALU import ALU
from RAM import RAM
from Register import Register
from ROM import ROM
from Clock import Clock
import os
R0 = Register(0)
R1 = Register(0)
R2 = Register(0)
R3 = Register(0)
Registros = [R0, R1, R2, R3]
i = 0
def CargarRegistroR0(insertar):
    global Registros
    Registros[0].VRam = insertar
    print(f"Load_R0: valor: {insertar}")
    #print(R0.VRam)
def CargarRegistroR1(insertar):
    global Registros
    Registros[1].VRam = insertar
    print(f"Load_R1: valor: {insertar}")
    #print(R1.VRam)
def CargarRegistroR2(insertar):
    global Registros
    Registros[2].VRam = insertar
    print(f"Load_R2: valor: {insertar}")
def CargarRegistroR3(insertar):
    global Registros
    Registros[3].VRam = insertar
    print(f"Load_R3: valor: {insertar}")

def mostrarClock(clock, boolclock):
    if(clock == True):
        print(f"Clock: {clock}")

def mostrarRam(ramdata, boolram):
    if(boolram == True):
        print(f"Ram: {ramdata}")

def mostrarRegistros(boolregistros):
    if(boolregistros == True):
        global Registros
        print(f"Registros:\n Registro0: {Registros[0].VRam}\n Registro1: {Registros[1].VRam}\n Registro2: {Registros[2].VRam}\n Registro3: {Registros[3].VRam}")

def MostrarAluflags(AluZero,AluOverflow, AluNegative,boolAluflags):
    if(boolAluflags == True):
        print(f"Zero: {AluZero}\nOverflow: {AluOverflow}\nNegative: {AluNegative}")
def halt(tamano):
    global i
    i = tamano
    print("Program done")




def main():
    global i
    rom = ROM()
    ram = RAM()
    alu = ALU()
    clock = Clock(rom.getclock())
    instruction = ""
    for key,valor in rom.getvisualizacion().items():
        if(key == "RAM"):
            vistaRam = valor
        elif(key == "Registers"):
            vistaRegistros = valor
        elif(key == "Clock"):
            vistaClock = valor
        elif(key == "ALU"):
            vistaAlu = valor

    #print(ram.instruction)
    mostrarRegistros(vistaRegistros)
    mostrarRam(ram.data,vistaRam)
    mostrarClock(clock.frecuencia,vistaClock)
    MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
    print("--------------------")
    largo = len(ram.instruction)
    i = 0
    #print(i)
    #print(largo)
    while (i < largo):
        strin = str(ram.instruction[i])
        if(strin.find(";")!= -1):
            #print("Hola")
            i = i + 1
            pass
        else:
            print("---------Fetch-----------")
            print(strin)
            mostrarRegistros(vistaRegistros)
            mostrarRam(ram.data,vistaRam)
            mostrarClock(clock.frecuencia,vistaClock)
            MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
            clock.sleepScreen()
            data = ""
            buscar = "" 
            pincio = 0
            pfinal = strin.find(" ")
            buscar = strin[:pfinal]
            pincio = pfinal
            if(pincio == -1):
                pass
            else:
                data = strin[pincio+1: ]
                data = data.replace(" ", "")
                data = data.rstrip("\n")
            #Fetch----------------------------------
            #print(buscar)
            #print(data)
            instruction = rom.BuscarInstru(buscar)
            clock.sleepScreen()
            print("--------------------")
            print("----------Decode----------")
            #print(instruction)
            #mostrarRegistros(vistaRegistros)
            #Decode---------------------------------
            #print(instruction)
            #print("Antes de eval\n")
            #print(f"{data}, el len es: {len(data)}")
            #print(f"{buscar}, el len es: {len(buscar)}")
            eval(instruction)
            print("--------Execute------------")
            clock.sleepScreen()
            mostrarRegistros(vistaRegistros)
            mostrarRam(ram.data,vistaRam)
            mostrarClock(clock.frecuencia,vistaClock)
            MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
            clock.sleepScreen()
            print("--------------------")
            i = i + 1
if __name__ == "__main__":
    main()
    #rom = ROM()
    #ram = RAM()
    #alu = ALU()
    #clock = Clock(rom.getclock())
    #instruction = ""
    #for key,valor in rom.getvisualizacion().items():
        #if(key == "RAM"):
            #vistaRam = valor
        #elif(key == "Registers"):
            #vistaRegistros = valor
        #elif(key == "Clock"):
            #vistaClock = valor
        #elif(key == "ALU"):
            #vistaAlu = valor

    #print(ram.instruction)
    #mostrarRegistros(vistaRegistros)
    #mostrarRam(ram.data,vistaRam)
    #mostrarClock(clock.frecuencia,vistaClock)
    #MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
    #print("--------------------")
    #largo = len(ram.instruction)
    #i = 0
    #print(i)
    #print(largo)
    #while (i < largo):
        #strin = str(ram.instruction[i])
        #if(strin.find(";")!= -1):
            #print("Hola")
            #i = i + 1
            #pass
        #else:
            #print("---------Fetch-----------")
            #print(strin)
            #mostrarRegistros(vistaRegistros)
            #mostrarRam(ram.data,vistaRam)
            #mostrarClock(clock.frecuencia,vistaClock)
            #MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
            #clock.sleepScreen()
            #data = ""
            #buscar = "" 
            #pincio = 0
            #pfinal = strin.find(" ")
            #buscar = strin[:pfinal]
            #pincio = pfinal
            #if(pincio == -1):
                #pass
            #else:
                #data = strin[pincio+1: ]
                #data = data.replace(" ", "")
                #data = data.rstrip("\n")
            #Fetch----------------------------------
            #print(buscar)
            #print(data)
            #instruction = rom.BuscarInstru(buscar)
            #clock.sleepScreen()
            #print("--------------------")
            #print("----------Decode----------")
            #print(instruction)
            #mostrarRegistros(vistaRegistros)
            #Decode---------------------------------
            #print(instruction)
            #print("Antes de eval\n")
            #print(f"{data}, el len es: {len(data)}")
            #print(f"{buscar}, el len es: {len(buscar)}")
            #eval(instruction)
            #print("--------Execute------------")
            #clock.sleepScreen()
            #mostrarRegistros(vistaRegistros)
            #mostrarRam(ram.data,vistaRam)
            #mostrarClock(clock.frecuencia,vistaClock)
            #MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
            #clock.sleepScreen()
            #print("--------------------")
            #i = i + 1
            #mostrarRegistros(True)
            #Execute--------------------------------
            #print("\n")
    #print(f"Estoy afuera del for y lo ultimo es: {instruction}")
        
    
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
