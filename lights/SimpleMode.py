from .lightsMode import LightsMode

class SimpleMode(LightsMode):
    def __init__(self, numLights, colorOn, colorOff):
        super().__init__(numLights)
        self.on = colorOn
        self.off = colorOff
        self.nextLight = 0
        self.prevLight = 0
    def processEvent(self, event):
        message, deltatime = event
        key = message[1]
        state = message[0]
        print(message, deltatime)
        if (state == 144):
            self.pixels[self.nextLight % self.numLights] = self.on
            self.nextLight+=1
        else:
            self.pixels[self.prevLight % self.numLights] = self.off
            self.prevLight+=1


