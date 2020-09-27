from ALU import ALU
from RAM import RAM
from Register import Register
from ROM import ROM
from Clock import Clock
class IC:
    def __init__(self, manufacturer, builddate, purpose):
        self.man = manufacturer
        self.build = builddate
        self.pp = purpose
        self.R0 = Register(0)
        self.R1 = Register(0)
        self.R2 = Register(0)
        self.R3 = Register(0)
        self.PC = Register(0) #PC = IR
        self.IAR = Register("")
        self.OR = Register(0)
        self.Registros = [self.R0, self.R1, self.R2, self.R3, self.PC, self.IAR, self.OR]
        self.i = 0
        self.alu = ALU()
        self.ram = RAM()