import board
import neopixel

class LightsMode():
    DOWN = 144
    def __init__(self, numLights, pixelOrder=neopixel.RGB):
        self.pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=pixelOrder)
        self.pixels.fill((0,0,0))
        self.numLights = numLights

    def processEvent(self, event):
        pass
