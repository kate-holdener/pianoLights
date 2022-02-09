class AudioToLights:
    def __init__(self, eventQ, lightsInterface):
        self.eventQ = eventQ
        self.lightsInterface = lightsInterface
        self.terminate = True

    def run(self):
        self.terminate = False
        while not self.terminate:
            event = self.eventQ.get()
            self.lightsInterface.processEvent(event)

    def stop(self):
        self.terminate = True
