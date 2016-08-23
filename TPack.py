import time
from TStrip import TStrip
from ColorCycler import ColorCycler
from Spark import Spark
from MatrixRain import MatrixRain
from AcidRain import AcidRain
from Slasher import Slasher



##
## TPack
## Runs the 16x16 matrix on the pack.
##
class TPack(object):
  
    # init  
    # Animation 1: Matrix
    # Animation 2: 
    def __init__(self, dimmer, animation):
        # Init the strip as a matrix
        self.strip = TStrip(256, dimmer)
        self.strip.setMatrixWinding(16, 16)

        self.animation = animation
        if self.animation == 1:
            self.init1()
        elif self.animation == 2:
            self.init2()
        elif self.animation == 3:
            self.init3()

        return


    def init1(self):
        self.sparks = []
        for i in range(16):
            self.sparks.append(MatrixRain(self.strip))
        self.fadeRate = .80
        return


    def init2(self):
        self.sparks = []
        for i in range(30):
            self.sparks.append(AcidRain(self.strip))
        self.fadeRate = .80
        return


    def init3(self):
        self.sparks = []
        for i in range(2):
            self.sparks.append(Slasher(self.strip))
        self.fadeRate = .80
        return


    # run
    # Infinite loop that runs the animation
    def run(self):
        while True:
            self.strip.startFrame()

            self.strip.fade(self.fadeRate)

            for spark in self.sparks:
                spark.run()

            self.strip.endFrame()


    # run3
    # Runs the spark playground
    def run3(self):
        return



pack = TPack(0, 3)
pack.run()
