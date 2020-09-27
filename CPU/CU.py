from Integratedcircuit import IC
from ALU import ALU
from RAM import RAM
from Register import Register
from ROM import ROM
from Clock import Clock
class CU(IC):
    def CargarRegistroR0(self, insertar):
        if (type(insertar) == int):
            if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
                self.Registros[0].VRam = insertar
                print(f"Load_R0: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction))
        else:
            if(len(insertar) <= 2 and (int(insertar) >= 0 and int(insertar) <= 15)):
                insertar = int(insertar)
                self.Registros[0].VRam = insertar
                print(f"Load_R0: valor: {insertar}")
            elif(len(insertar) == 4 and (int(insertar) >= 0 and int(insertar) <= 15)):
                #convertir de binario a decimal.
                insertar = int(str(insertar), 2)
                self.Registros[0].VRam = insertar
                print(f"Load_R0: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction))   
        
        #print(R0.VRam)

    def CargarRegistroR1(self, insertar):
        #print(type(insertar))
        if (type(insertar) == int):
            if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
                self.Registros[1].VRam = insertar
                print(f"Load_R1: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction))
        else:
            if(len(insertar) <= 2 and (int(insertar) >= 0 and int(insertar) <= 15)):
                insertar = int(insertar)
                self.Registros[1].VRam = insertar
                print(f"Load_R1: valor: {insertar}")
            elif(len(insertar) == 4 and (int(insertar) >= 0 and int(insertar) <= 15)):
                #convertir de binario a decimal.
                insertar = int(str(insertar), 2)
                self.Registros[1].VRam = insertar
                print(f"Load_R1: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction)) 

    def CargarRegistroR2(self, insertar):
        if (type(insertar) == int):
            if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
                self.Registros[2].VRam = insertar
                print(f"Load_R2: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction))
        else:
            if(len(insertar) <= 2 and (int(insertar) >= 0 and int(insertar) <= 15)):
                insertar = int(insertar)
                self.Registros[2].VRam = insertar
                print(f"Load_R2: valor: {insertar}")
            elif(len(insertar) == 4 and (int(insertar) >= 0 and int(insertar) <= 15)):
                #convertir de binario a decimal.
                insertar = int(str(insertar), 2)
                self.Registros[2].VRam = insertar
                print(f"Load_R2: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction)) 

    def CargarRegistroR3(self, insertar):
        if (type(insertar) == int):
            if(insertar != -1 and (insertar >= 0 and insertar <= 15)):
                self.Registros[3].VRam = insertar
                print(f"Load_R3: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction))
        else:
            if(len(insertar) <= 2 and (int(insertar) >= 0 and int(insertar) <= 15)):
                insertar = int(insertar)
                self.Registros[3].VRam = insertar
                print(f"Load_R3: valor: {insertar}")
            elif(len(insertar) == 4 and (int(insertar) >= 0 and int(insertar) <= 15)):
                #convertir de binario a decimal.
                insertar = int(str(insertar), 2)
                self.Registros[3].VRam = insertar
                print(f"Load_R3: valor: {insertar}")
            else:
                self.detener(len(self.ram.instruction)) 

    def Jump(self, registro):
        if (type(registro) == int and (registro >= 0 and registro <= 15)):
            self.i = registro - 1 
            print(f"Salto a la línea {self.i+1}")
        elif(len(registro) <= 2):
            registro = int(registro)
            if(registro >= 0 and registro <= 15):
                self.i = registro - 1
                print(f"Salto a la línea {self.i+1}")
            else: 
                self.detener(len(self.ram.instruction))
        elif(len(registro) == 4):
            #convertir de binario a decimal.
            registro = int(str(registro), 2)
            if(registro >= 0 and registro <= 15):
                self.i = registro - 1
                print(f"Salto a la línea {self.i+1}")
            else: 
                self.detener(len(self.ram.instruction))
        else:
            self.detener(len(self.ram.instruction))

    def JumpNeg(self, registro):
        if(self.alu.N > 0):
            if (type(registro) == int and (registro >= 0 and registro <= 15)):
                self.i = registro - 1
                print(f"Salto a la línea {self.i+1} por Negative true")
            else:
                if(len(registro) <= 2):
                    registro = int(registro)
                    if(registro >= 0 and registro <= 15):
                        self.i = registro - 1
                        print(f"Salto a la línea {self.i+1} por Negative true")
                    else: 
                        self.detener(len(self.ram.instruction))
                elif(len(registro) == 4):
                    #convertir de binario a decimal.
                    registro = int(str(registro), 2)
                    if(registro >= 0 and registro <= 15):
                        self.i = registro - 1
                        print(f"Salto a la línea {self.i+1} por Negative true")
                    else: 
                        self.detener(len(self.ram.instruction))
                else:
                    self.detener(len(self.ram.instruction))
        else:
            print("No hay salto de línea")
    def mostrarClock(self, clock, boolclock, rad):
        if(rad == "bin"):
            if(boolclock == True):
                clock = bin(clock)
                print(f"Clock: {clock}")
        elif(rad == "Oct"):
            if(boolclock == True):
                clock = oct(clock)
                print(f"Clock: {clock}")
        elif(rad == "Dec"):
            if(boolclock == True):
                print(f"Clock: {clock}")
        elif(rad == "Hex"):
            if(boolclock == True):
                clock = hex(clock)
                print(f"Clock: {clock}")
        else:
            pass
    def mostrarRam(self, ramdata, boolram, rad):
        if(rad == "bin"):
            if(boolram == True):
                fila = "["
                parar = len(ramdata)-1
                for i in range(len(ramdata)):
                    dtt = ramdata[i]
                    dtt = int(dtt)
                    dtt = bin(dtt)
                    fila += f"{str(dtt)}"
                    if(i != parar):
                        fila += ", "
                fila += "]"
                print(fila)
        elif(rad == "Oct"):
            if(boolram == True):
                fila = "["
                parar = len(ramdata)-1
                for i in range(len(ramdata)):
                    dtt = ramdata[i]
                    dtt = int(dtt)
                    dtt = oct(dtt)
                    fila += f"{str(dtt)}"
                    if(i != parar):
                        fila += ", "
                fila += "]"
                print(fila)
        elif(rad == "Dec"):
            if(boolram == True):
                print(f"Ram: {ramdata}")
        elif(rad == "Hex"):
            if(boolram == True):
                fila = "["
                parar = len(ramdata)-1
                for i in range(len(ramdata)):
                    dtt = ramdata[i]
                    dtt = int(dtt)
                    dtt = bin(dtt)
                    fila += f"{str(dtt)}"
                    if(i != parar):
                        fila += ", "
                fila += "]"
                print(fila)

    def mostrarRegistros(self, boolregistros, rad):
        if(boolregistros == True):
            if(rad == "bin"):
                r0 = bin(self.Registros[0].VRam)
                r1 = bin(self.Registros[1].VRam)
                r2 = bin(self.Registros[2].VRam)
                r3 = bin(self.Registros[3].VRam)
                r4 = bin(self.Registros[4].VRam)
                r6 = bin(self.Registros[6].VRam)
                print(f"Registros:\n Registro0: {r0}\n Registro1: {r1}\n Registro2: {r2}\n Registro3: {r3}\n Registro PC: {r4}\n Registro IAR {self.Registros[5].VRam}\n Registro OR: {r6}")
            elif(rad == "Oct"):
                r0 = oct(self.Registros[0].VRam)
                r1 = oct(self.Registros[1].VRam)
                r2 = oct(self.Registros[2].VRam)
                r3 = oct(self.Registros[3].VRam)
                r4 = oct(self.Registros[4].VRam)
                r6 = oct(self.Registros[6].VRam)
                print(f"Registros:\n Registro0: {r0}\n Registro1: {r1}\n Registro2: {r2}\n Registro3: {r3}\n Registro PC: {r4}\n Registro IAR {self.Registros[5].VRam}\n Registro OR: {r6}")
            elif(rad == "Dec"):
                print(f"Registros:\n Registro0: {(self.Registros[0].VRam)}\n Registro1: {(self.Registros[1].VRam)}\n Registro2: {(self.Registros[2].VRam)}\n Registro3: {(self.Registros[3].VRam)}\n Registro PC: {(self.Registros[4].VRam)}\n Registro IAR {(self.Registros[5].VRam)}\n Registro OR: {(self.Registros[6].VRam)}")        
            elif(rad == "Hex"):
                r0 = hex(self.Registros[0].VRam)
                r1 = hex(self.Registros[1].VRam)
                r2 = hex(self.Registros[2].VRam)
                r3 = hex(self.Registros[3].VRam)
                r4 = hex(self.Registros[4].VRam)
                r6 = hex(self.Registros[6].VRam)
                print(f"Registros:\n Registro0: {r0}\n Registro1: {r1}\n Registro2: {r2}\n Registro3: {r3}\n Registro PC: {r4}\n Registro IAR {self.Registros[5].VRam}\n Registro OR: {r6}")

    def MostrarAluflags(self, AluZero,AluOverflow, AluNegative,boolAluflags):
        if(boolAluflags == True):
            print(f"Zero: {AluZero}\nOverflow: {AluOverflow}\nNegative: {AluNegative}")
    def halt(self, tamano):
        self.i = tamano
        print("Program done")
    def detener(self,tamano):
        print(f"Error en la línea {self.i}: {self.ram.instruction[self.i]}")
        self.i = tamano
    def OR_(self, val, pos):
        self.Registros[6].VRam = int(val)
        print(f"OUTPUT: {pos}, valor: {val}")
    def PrinOneComplement(self, dato):
        comple = self.alu.Ocomplement(dato)
        print(f"One complemente de {dato} es: {comple}")
    def PrinTwoComplement(self, dato):
        comple = self.alu.Twcomplement(dato)
        print(f"Two´s complemente de {dato} es: {comple}")

    def main(self):
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
            elif(key == "Radix"):
                vistaRadix = valor
        
        #comentarear todo esto ----------------------------------------------------------------------------------------------    
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
        self.mostrarRegistros(vistaRegistros, vistaRadix)
        self.mostrarRam(self.ram.data,vistaRam, vistaRadix)
        self.mostrarClock(clock.frecuencia,vistaClock, vistaRadix)
        self.MostrarAluflags(self.alu.Zero, self.alu.Overflow, self.alu.Negative, vistaAlu)
        print("-----------PROGRAMA KEYSENSITIVE COMANDOS EN MAYUSCULAS---------")
        largo = len(self.ram.instruction)
        self.i = 0
        #print(i)
        #print(largo)
        while (self.i < largo):
            strin = str(self.ram.instruction[self.i])
            if(strin.find(";")!= -1):
                #print("Hola")
                self.i = self.i + 1
                pass
            else:
                print("---------Fetch-----------")
                print(strin)
                self.Registros[4].VRam = self.i
                self.Registros[5].VRam = strin.rstrip("\n")
                self.mostrarRegistros(vistaRegistros, vistaRadix)
                self.mostrarRam(self.ram.data,vistaRam, vistaRadix)
                self.mostrarClock(clock.frecuencia,vistaClock, vistaRadix)
                self.MostrarAluflags(self.alu.Zero, self.alu.Overflow, self.alu.Negative, vistaAlu)
                clock.sleepScreen()
                data = ""
                buscar = "" 
                pincio = 0
                pfinal = strin.find(" ")
                #print(pfinal)
                if(pfinal != -1):
                    buscar = strin[:pfinal]
                else:
                    buscar = strin.replace(" ", "")
                    buscar = buscar.rstrip("\n")
                pincio = pfinal
                if(pincio == -1):
                    data = ""
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
                    elif(len(data) <= 2 and (int(data) >= 0 and int(data) <= 15)):
                        eval(instruction)
                    else:
                        self.detener(len(self.ram.instruction))
                elif((data[0:2] == "R0" or data[0:2] == "R1" or data[0:2] == "R2" or data[0:2] == "R3") and (data[2:] == "R0" or data[2:] == "R1" or data[2:] == "R2" or data[2:] == "R3")):
                    eval(instruction)
                else:
                    #print(buscar)
                    #print(instruction)
                    if(instruction == "self.halt(len(self.ram.instruction))"):
                        eval(instruction)
                    else:
                        self.detener(len(self.ram.instruction))
                print("--------Execute------------")
                clock.sleepScreen()
                self.mostrarRegistros(vistaRegistros, vistaRadix)
                self.mostrarRam(self.ram.data,vistaRam, vistaRadix)
                self.mostrarClock(clock.frecuencia,vistaClock, vistaRadix)
                self.MostrarAluflags(self.alu.Zero, self.alu.Overflow, self.alu.Negative, vistaAlu)
                clock.sleepScreen()
                print("--------------------")
                self.i = self.i + 1
                self.alu.reset()
                #comentarear esto------------------------------------------------------------------
                if(opcion == 2):
                    Enter = input("press Enter to continue to the next instruction...")
                #----------------------------------------------------------------------------------
    
    #def __init__(self):
        #Integratedcircuit.__init__(self)
        #self.R0 = Register(0)
        #self.R1 = Register(0)
        #self.R2 = Register(0)
        #self.R3 = Register(0)
        #self.PC = Register(0) #PC = IR
        #self.IAR = Register("")
        #self.OR = Register(0)
        #self.Registros = [self.R0, self.R1, self.R2, self.R3, self.PC, self.IAR, self.OR]
        #self.i = 0
        #self.alu = ALU()
        #self.ram = RAM()
    def runmain(self):
        self.main()
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