from inputs.PianoReader import PianoReader
from lights.SimpleTimedMode import SimpleTimedMode
from lights.RainbowMode import RainbowMode
from lights.SimpleMode import SimpleMode

from controls.AudioToLights import AudioToLights
from controls.DirectConnect import DirectConnect

# use the MIDI inputs to get signals from the piano
pianoReader = PianoReader()

# mode is the program we want to use for processing
# signals from the piano
#mode = SimpleTimedMode(50, (255,0,0), (0,0,255))
mode = RainbowMode(50)
#mode = SimpleMode(50, (255,0,0), (0,0,255))

# specify how the lights are connected
lightsConnection = DirectConnect(mode)

# create the controller for the lights
lightControl = AudioToLights(pianoReader.getEventQueue(), lightsConnection)
lightControl.run()
