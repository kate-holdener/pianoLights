import board
import neopixel
from .lightsMode import LightsMode

class SimpleMode(LightsMode):
    def __init__(self, numLights, colorOn, colorOff):
        super()
        self.numLights = numLights
        self.on = colorOn
        self.off = colorOff
        self.pixels = neopixel.NeoPixel(board.D18, numLights, brightness=1, pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))

    def processEvent(self, event):
        message, deltatime = event
        key = message[1]
        state = message[0]
        print(message, deltatime)
        if (state == 144):
            self.pixels[key % self.numLights] = self.on
        else:
            self.pixels[key % self.numLights] = self.off


