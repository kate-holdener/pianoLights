import board
import neopixel
from .SimpleTimedMode import SimpleTimedMode

class SimpleRainbowMode(SimpleTimedMode):
    def __init__(self, numLights, delayOff=5):
        super().__init__(numLights, (255,255,255), (0,0,0))

    def processEvent(self, event):
        self.off = self.on
        print("nextLight", self.nextLight)        
        if (self.nextLight % (self.numLights * 2) == 0):
            self.nextLight = 0

        # pick the next color to turn on
        self.on = self.wheel(self.nextLight * 256 // self.numLights )

        # Only turn on one light for a chord
        message, deltatime = event
        if deltatime < 0.02:
            print('chord')
            return

        SimpleTimedMode.processEvent(self, event)
        
    def wheel(self, pos): ##Funtion that makes each light a different rainbow color
        if pos<0 or pos > 255:
            r= g= b=0
        elif pos<85:
            r= int(pos*3)
            g= int(255-pos*3)
            b=0
        elif pos<170:
            pos -=85
            r= int(255 -pos*3)
            g=0
            b=int(pos*3)
        else:
            pos-= 170
            r=0
            g=int(pos*3)
            b=int(255-pos*3)
        return (r,g,b)


