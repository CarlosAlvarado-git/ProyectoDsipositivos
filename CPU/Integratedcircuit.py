from CU import CU
class IC:
    def __init__ (self, manufacturer, builddate, purpose):
        self.man = manufacturer
        self.build = builddate
        self.pp = purpose
        CU1 = CU(self.man, self.build, self.pp)