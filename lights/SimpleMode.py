from .lightsMode import LightsMode

class SimpleMode(LightsMode):
    def __init__(self, numLights, colorOn, colorOff):
        super(numLights)
        self.on = colorOn
        self.off = colorOff

    def processEvent(self, event):
        message, deltatime = event
        key = message[1]
        state = message[0]
        print(message, deltatime)
        if (state == 144):
            self.pixels[key % self.numLights] = self.on
        else:
            self.pixels[key % self.numLights] = self.off


