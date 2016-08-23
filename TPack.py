from TStrip import TStrip
from ColorCycler import ColorCycler
import time



##
## TPack
## Runs the 16x16 matrix on the pack.
##
class TPack(object):
  
    # init  
    # Animation 1: violet background with orbiting spark
    # Animation 2: Matrix
    def __init__(self, dimmer, animation):
        # Init the strip as a matrix
        self.strip = TStrip(256, dimmer)
        self.strip.setMatrixWinding(16, 16)

        self.animation = animation
        if self.animation == 1:
            self.init1()
        elif self.animation == 2:
            self.init2()

        return


    # init1
    # Inits the cycling spark animation
    def init1(self):
        self.sparkSpeed = 60        # Spark speed in pixels per second

        self.strip.paint((0x10, 0, 0x10))
        self.sparkPos = 0.0
        self.xSpark = 0
        self.ySpark = 0
        return


    # init2
    # Inits the speedball animation
    def init2(self):
        self.ballX = 0
        self.ballY = 0
        self.ballDX = 1.2
        self.ballDY = 0.73

        self.colorCycler = ColorCycler(.01, [
            (255.0,     0.0,        255.0),
            (255.0,     0.0,        0.0),
            (0.0,       255.0,      0.0),
            ])

        self.strip.paint((0, 0, 0))
        return


    # run
    # Infinite loop that runs the animation
    def run(self):
        while True:
            self.strip.startFrame()

            if self.animation == 1:
                self.run1()
            elif self.animation == 2:
                self.run2()

            self.strip.endFrame()


    # run1
    # Runs the orbiting spark animation
    def run1(self):
        # Move the spark
        self.strip.setGridPixel(self.xSpark, self.ySpark,(0x10, 0, 0x10))
        self.sparkPos += (self.sparkSpeed / self.strip.frameRate)
        if self.sparkPos >= 60:
            self.sparkPos = 0

        if self.sparkPos <= 15:
            self.xSpark = int(self.sparkPos)
            self.ySpark = 0
        elif self.sparkPos <= 30:
            self.xSpark = 15
            self.ySpark = int(self.sparkPos - 15)
        elif self.sparkPos <= 45:
            self.xSpark = int(15 - (self.sparkPos - 30))
            self.ySpark = 15
        else:
            self.xSpark = 0
            self.ySpark = int(15 - (self.sparkPos - 45))

        self.strip.setGridPixel(self.xSpark, self.ySpark, (0xff, 0xff, 0xff))
        return


    # run2
    # Runs the speedball animation
    def run2(self):
        self.strip.fade(.80)
        self.colorCycler.cycle()
        
        self.ballX += self.ballDX
        if self.ballX < 0:
            self.ballX = - self.ballX
            self.ballDX = - self.ballDX
        if self.ballX > 15:
            self.ballX = 15 - (self.ballX - 15)
            self.ballDX = - self.ballDX

        self.ballY += self.ballDY
        if self.ballY < 0:
            self.ballY = - self.ballY
            self.ballDY = - self.ballDY
        if self.ballY > 15:
            self.ballY = 15 - (self.ballY - 15)
            self.ballDY = - self.ballDY

        self.strip.drawBall(self.ballX, self.ballY, 1.5, self.colorCycler.currentColor)
        return



pack = TPack(0, 2)
pack.run()
