import CU
class IC:
    def __init__(self, manufacturer, builddate, purpose):
        self.man = manufacturer
        self.build = builddate
        self.pp = purpose
    def crearCu(self):
        CU1 = CU()