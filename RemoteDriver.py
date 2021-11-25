from inputs.PianoReader import PianoReader
from controls.AudioToLights import AudioToLights
from controls.RemoteConnect import RemoteConnect

# use the MIDI inputs to get signals from the piano
pianoReader = PianoReader()
# specify how the lights are connected
lightsConnection = RemoteConnect()

# create the controller for the lights
lightControl = AudioToLights(pianoReader.getEventQueue(), lightsConnection)
lightControl.run()
