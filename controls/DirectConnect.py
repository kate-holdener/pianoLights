class DirectConnect:
    def __init__(self, mode):
        self.mode = mode

    def processEvent(self, event):
        self.mode.processEvent(event)
