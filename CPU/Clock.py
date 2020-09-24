import time
class Clock:
    def __init__(self,frecuencia):
        #if (frecuencia > 0):
        self.frecuencia = (1/frecuencia)
        #else:
            #self.frecuencia = 0
    
    def sleepScreen(self):
        time.sleep(self.frecuencia)