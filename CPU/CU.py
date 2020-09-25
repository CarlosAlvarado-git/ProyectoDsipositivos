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
alu = ALU()
#ram = RAM() ----
def CargarRegistroR0(insertar):
    global Registros, ram
    if (type(insertar) == int):
        if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
            Registros[0].VRam = insertar
            print(f"Load_R0: valor: {insertar}")
        else:
            detener(len(ram.instruction))
    else:
        if(len(insertar) <= 2 and (insertar >= 0 and insertar <= 15)):
            insertar = int(insertar)
            Registros[0].VRam = insertar
            print(f"Load_R0: valor: {insertar}")
        elif(len(insertar) == 4 and (insertar >= 0 and insertar <= 15)):
            #convertir de binario a decimal.
            insertar = int(str(insertar), 2)
            Registros[0].VRam = insertar
            print(f"Load_R0: valor: {insertar}")
        else:
            detener(len(ram.instruction))   
    
    #print(R0.VRam)

def CargarRegistroR1(insertar):
    global Registros, ram
    if (type(insertar) == int):
        if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
            Registros[1].VRam = insertar
            print(f"Load_R1: valor: {insertar}")
        else:
            detener(len(ram.instruction))
    else:
        if(len(insertar) <= 2 and (insertar >= 0 and insertar <= 15)):
            insertar = int(insertar)
            Registros[1].VRam = insertar
            print(f"Load_R1: valor: {insertar}")
        elif(len(insertar) == 4 and (insertar >= 0 and insertar <= 15)):
            #convertir de binario a decimal.
            insertar = int(str(insertar), 2)
            Registros[1].VRam = insertar
            print(f"Load_R1: valor: {insertar}")
        else:
            detener(len(ram.instruction)) 

def CargarRegistroR2(insertar):
    if (type(insertar) == int):
        if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
            Registros[2].VRam = insertar
            print(f"Load_R2: valor: {insertar}")
        else:
            detener(len(ram.instruction))
    else:
        if(len(insertar) <= 2 and (insertar >= 0 and insertar <= 15)):
            insertar = int(insertar)
            Registros[2].VRam = insertar
            print(f"Load_R2: valor: {insertar}")
        elif(len(insertar) == 4 and (insertar >= 0 and insertar <= 15)):
            #convertir de binario a decimal.
            insertar = int(str(insertar), 2)
            Registros[2].VRam = insertar
            print(f"Load_R2: valor: {insertar}")
        else:
            detener(len(ram.instruction)) 

def CargarRegistroR3(insertar):
    if (type(insertar) == int):
        if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
            Registros[3].VRam = insertar
            print(f"Load_R3: valor: {insertar}")
        else:
            detener(len(ram.instruction))
    else:
        if(len(insertar) <= 2 and (insertar >= 0 and insertar <= 15)):
            insertar = int(insertar)
            Registros[3].VRam = insertar
            print(f"Load_R3: valor: {insertar}")
        elif(len(insertar) == 4 and (insertar >= 0 and insertar <= 15)):
            #convertir de binario a decimal.
            insertar = int(str(insertar), 2)
            Registros[3].VRam = insertar
            print(f"Load_R3: valor: {insertar}")
        else:
            detener(len(ram.instruction)) 

def Jump(registro):
    global i, ram
    if (type(registro) == int and (registro >= 0 and registro <= 15)):
        i = registro
    elif(len(registro) <= 2):
        registro = int(registro)
        if(registro >= 0 and registro <= 15):
            i = registro
        else: 
            detener(len(ram.instruction))
    elif(len(registro) == 4):
        #convertir de binario a decimal.
        registro = int(str(registro), 2)
        if(registro >= 0 and registro <= 15):
            i = registro
        else: 
            detener(len(ram.instruction))
    else:
        detener(len(ram.instruction))

def JumpNeg(registro):
    global i,alu
    if(alu.Negative == True):
        if (type(registro) == int and (registro >= 0 and registro <= 15)):
            i = registro
        else:
            if(len(registro) <= 2):
                registro = int(registro)
                if(registro >= 0 and registro <= 15):
                    i = registro
                else: 
                    detener(len(ram.instruction))
            elif(len(registro) == 4):
                #convertir de binario a decimal.
                registro = int(str(registro), 2)
                if(registro >= 0 and registro <= 15):
                    i = registro
                else: 
                    detener(len(ram.instruction))
            else:
                detener(len(ram.instruction))

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
def detener(tamano):
    global i, ram
    print(f"Error en la línea {i}: {ram.instruction[i]}")
    i = tamano




def main():
    global i,alu, ram
    rom = ROM()
    #alu = ALU()
    #ram = RAM()
    #clock = Clock(rom.getclock())---
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
    
    #comentarear todo esto ----------------------------------------------------------------------------------------------
    opcion = 0
    while(opcion < 1 or opcion > 7):
        
        print(" 1: 1.cpufm\n 2: 2.cpufm\n 3: 3.cpufm\n 4: 4.cpufm\n 5: 5.cpufm\n 6: 6.cpufm\n 7: 7.cpufm\n")
        opcion = int(input("Ingrese el numero del programa que desea ejecutar: "))
        if(opcion == 1):
            ram = RAM("1.cpufm")
        elif(opcion == 2):
            ram = RAM("2.cpufm")
        elif(opcion == 3):
            ram = RAM("3.cpufm")
        elif(opcion == 4):
            ram = RAM("4.cpufm")
        elif(opcion == 5):
            ram = RAM("5.cpufm")
        elif(opcion == 6):
            ram = RAM("6.cpufm")
        elif(opcion == 7):
            ram = RAM("7.cpufm")
        else:
            print(f"El numero {opcion} no esta en el rango")
    
    opcion = 0
    while(opcion <1 or opcion>2):
        print("\nComo desea correr el programa")
        print(" 1: Clock\n 2: Debug Mode")
        opcion = int(input("Ingrese numero de la opcion: "))
        if(opcion == 1):
            clock = Clock(rom.getclock())
        elif(opcion == 2):
            clock = Clock(0)
        else:
            print(f"El numero {opcion} no esta en el rango")
    #----------------------------------------------------------------------------------------------------------------------------
    
    # si es debug clock = Clock(0)
    #print(ram.instruction)
    mostrarRegistros(vistaRegistros)
    mostrarRam(ram.data,vistaRam)
    mostrarClock(clock.frecuencia,vistaClock)
    MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
    print("-----------PROGRAMA KEYSENSITIVE COMANDOS EN MAYUSCULAS---------")
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
            if(data.isdigit() == True):
                if(len(data) == 4):
                    eval(instruction)
                elif(len(data) == 2 and (int(data) >= 0 and int(data) <= 15)):
                    eval(instruction)
                else:
                    detener(len(ram.instruction))
            elif((data[0:2] == "R0" or data[0:2] == "R1" or data[0:2] == "R2" or data[0:2] == "R3") and (data[2:] == "R0" or data[2:] == "R1" or data[2:] == "R2" or data[2:] == "R3")):
                eval(instruction)
            else:
                if(instruction == "halt(len(ram.instruction))" or instruction == "print(ram.data(data))"):
                    eval(instruction)
                else:
                    detener(len(ram.instruction))
            print("--------Execute------------")
            clock.sleepScreen()
            mostrarRegistros(vistaRegistros)
            mostrarRam(ram.data,vistaRam)
            mostrarClock(clock.frecuencia,vistaClock)
            MostrarAluflags(alu.Zero, alu.Overflow, alu.Negative, vistaAlu)
            clock.sleepScreen()
            print("--------------------")
            i = i + 1
            #comentarear esto------------------------------------------------------------------
            if(opcion == 2):
                Enter = input("press Enter to continue to the next instruction...")
            #----------------------------------------------------------------------------------
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
