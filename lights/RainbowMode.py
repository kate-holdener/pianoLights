from .lightsMode import LightsMode

class RainbowMode(LightsMode):
    def __init__(self, numLights):
        super().__init__(numLights)
        self.zeroBlue = 20
        self.zeroGreen = 50
        
    def processEvent(self, event):
        message, deltatme = event
        state = message[0]
        key = message[1]
        intensity = message[2]
        if (state == LightsMode.DOWN):
            self.pixels.fill(self.pickColor(intensity))

    def pickColor(self,intensity):
        if intensity<0 or intensity > 255:
            r= g= b=0
        elif intensity < self.zeroBlue:
            r= int(intensity*3)
            g= int(255-intensity*3)
            b=0
        elif intensity < self.zeroGreen:
            intensity -=self.zeroBlue
            r= int(255 -intensity*3)
            g=0
            b=int(intensity*3)
        else:
            intensity-= self.zeroGreen
            r=0
            g=int(intensity*3)
            b=int(255-intensity*3)
        return (r,g,b)

