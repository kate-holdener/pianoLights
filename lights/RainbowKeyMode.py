from .lightsMode import LightsMode

class RainbowKeyMode(LightsMode):
    def __init__(self, numLights):
        super().__init__(numLights)
        self.color=[(255,0,0), (255, 127,0), (255,255,0), (0,255,0), (0,0,255), (46,43,95), (139,0,255)]

    def processEvent(self, event):
        message, deltatme = event
        state = message[0]
        key = message[1]
        intensity = message[2]
        if (state == LightsMode.DOWN):
            self.pixels.fill(self.pickColor(key))

    def pickColor(self, key):
        note = key % len(self.color)
        return self.color[note]


