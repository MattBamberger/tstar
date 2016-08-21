from TStrip import TStrip
import time


class TBike(object):

    def __init__(self):
        # Init the strip and set up our geometry
        self.strip = TStrip(44)
        self.iHeadLight = 19
        self.iTailLight = 39
        self.sides = [
            (18, 20),
            (17, 21),
            (16, 22),
            (15, 23),
            (14, 24),
            (13, 25),
            (12, 26),
            (11, 27),
            (10, 28),
            ( 9, 29),
            ( 8, 30),
            ( 7, 31),
            ( 6, 32), 
            ( 5, 33), 
            ( 4, 34), 
            ( 3, 35),
            ( 2, 36),
            ( 1, 37) ]
        self.sideLevels = [0.0 for i in range(len(self.sides))]

        # Configure ourselves
        self.headLightColor = (0xff, 0xff, 0xff)
        self.tailLightColor = (0xff, 0x00, 0x00)
        self.sparkColor = (0xff, 0xff, 0xff)
        self.glowColor = (0xff, 0x00, 0xff)
        self.sparkSpeed = 30
        self.fadeSpeed = 12.0
        self.persistence = 1.0 - (self.fadeSpeed / self.strip.frameRate)

        # Init ourselves
        self.strip.setPixel(self.iHeadLight, self.headLightColor)
        self.strip.setPixel(self.iTailLight, self.tailLightColor)
        self.sparkPos = 0

        return


    def setSide(self, iPixel, color):
        self.strip.setPixel(self.sides[iPixel][0], color)
        self.strip.setPixel(self.sides[iPixel][1], color)
        return


    def run(self):
        while True:
            self.strip.startFrame()
            
            # Move the spark
            self.sparkPos += self.sparkSpeed / self.strip.frameRate
            if self.sparkPos >= len(self.sides):
                self.sparkPos = 0
            pos = int(self.sparkPos)

            # Fade every pixel
            for iPixel in range(len(self.sides)):
                self.sideLevels[iPixel] = self.sideLevels[iPixel] * self.persistence

            # Set the spark pixel to maximum
            self.sideLevels[pos] = 1.0

            # Apply the pixel levels
            for iPixel in range(len(self.sides)):
                red = int(self.sideLevels[iPixel] * self.glowColor[0])
                green = int(self.sideLevels[iPixel] * self.glowColor[1])
                blue = int(self.sideLevels[iPixel] * self.glowColor[2])
                self.setSide(iPixel, (red, green,blue))

            # Draw the spark
            self.setSide(pos, self.sparkColor)

            self.strip.endFrame()





bike = TBike()
bike.run()
