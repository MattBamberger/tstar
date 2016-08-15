# 1
import spidev
import time


class TStrip(object):

    def __init__(self, cPixels):
        self.frameRate = 60 #Target frame rate in Hz
        
        self.spi = spidev.SpiDev()
        self.spi.open(0,1)
        self.spi.max_speed_hz=8000000

        self.cPixels = cPixels
        self.pixels = [(0, 0, 0) for i in range(0, cPixels)]
        # Pin the entire system to 25 full-brightness LEDs or equivalent
        self.maxTotalBrightness = 25 * 3 * 0xff

        self.paint((0, 0, 0))
        return

    def setMatrixWinding(self, width, height):
        self.mapPixels = [[0 for j in range(height)] for i in range(width)]
        x = 0
        y = 0
        yDir = 1
        iPixel = 0
        while True:
            self.mapPixels[x][y] = iPixel
            iPixel += 1
            y += yDir
            if y < 0:
                x += 1
                y = 0
                yDir = 1
            if y >= height:
                x += 1
                y = height - 1
                yDir = -1
            if x >= width:
                return


    def writeBrightness(self, brightness):
        if self.cumulativeBrightness > self.maxTotalBrightness:
            brightness = 0
        self.spi.xfer2([brightness])
        self.cumulativeBrightness += brightness
        return


    def setPixel(self, iPixel, color):
        self.pixels[iPixel] = color
        return


    def setGridPixel(self, x, y, color):
        iPixel = self.mapPixels[x][y]
        self.pixels[iPixel] = color
        return


    def paint(self, color):
        for i in range(0, self.cPixels):
            self.pixels[i] = color
        return


    def startFrame(self):
        self.frameStartTime = time.time()
        return
    
        
    def endFrame(self):
        self.cumulativeBrightness = 0
        
        # Header block
        self.spi.xfer2([0x00, 0x00, 0x00, 0x00])

        # LEDs
        for i in range(0, self.cPixels):
            self.spi.xfer2([0xff])
            self.writeBrightness(self.pixels[i][2]) # B
            self.writeBrightness(self.pixels[i][1]) # G
            self.writeBrightness(self.pixels[i][0]) # R

        # End block
        self.spi.xfer2([0xff, 0xff, 0xff, 0xff])
        for i in range(0, 1 + (self.cPixels >> 5)):
            self.spi.xfer2([0x00, 0x00, 0x00, 0x00])

        extraTime = (1 / self.frameRate) - (time.time() - self.frameStartTime)
        if extraTime > 0:
            time.sleep(extraTime)

        return
