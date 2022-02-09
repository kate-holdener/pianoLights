import requests
class RemoteConnect:
    def __init__(self, host):
        self.host = host

    def processEvent(self, event):
        message,deltatime = event
        p = {'event': message[0], 'key': message[1], 'velocity':message[2], 'deltatime':deltatime}
        r = requests.get(self.host+"/lights", params=p)
        print(r)

if __name__=='__main__':
    rc = RemoteConnect('http://192.168.3.120:8000')
    rc.processEvent(((1,2,3),0.3))
