from Tornus.TStrip import TStrip
import time


sparkSpeed = 60


class TPack(object):
    
    def __init__(self):
        self.strip = TStrip(256)
        self.strip.setMatrixWinding(16, 16)

        self.strip.paint((0x10, 0, 0x10))
        self.sparkPos = 0.0
        self.xSpark = 0
        self.ySpark = 0
        return


    def run(self):
        while True:
            self.strip.startFrame()

            # Move the spark
            self.strip.setGridPixel(self.xSpark, self.ySpark,(0x10, 0, 0x10))
            self.sparkPos += (sparkSpeed / self.strip.frameRate)
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

            self.strip.endFrame()


pack = TPack()
pack.run()
