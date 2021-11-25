from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import urllib
import queue
from lights.SimpleMode import SimpleMode
from lights.SimpleRainbowMode import SimpleRainbowMode

class LightsRequestHandler(BaseHTTPRequestHandler):
    mode = None
    mapping = {}
    commandQ = queue.Queue(3);
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        o = urlparse(self.path)
        print(o)

        qs = urllib.parse.parse_qs(o.query)
        action=int(o.query.find('event'))
        key=int(o.query.find('key'))
        velocity=int(o.query.find('velocity'))
        deltatime=float(o.query.find('deltatime'))
        mode.processEvent(((action,key,velocity),deltatime))

        # store the last pressed key in the command queue
        # command queue is used to switch light modes
        if (commandQueue.full()):
            commandQueue.get();
        if (action > FIRST_KEY and action <= LAST_KEY):
            commandQ.put(1)
        elif (action == FIRST_KEY):
            commandQ.put(0)

        command = self.checkCommandQ()
        if command in mapping:
            mode = mapping[command]

    def check_command_q(self):
        total = 0
        for val, index in commandQ:
            total = val * (2 ** index)
        return total

    def do_lights(self):
        pass 

LightsRequestHandler.mode = SimpleMode(50, (255,0,0), (0,0,255))
LightsRequestHandler.mapping[0]=SimpleMode(50, (255,0,0), (0,0,255))
LightsRequestHandler.mapping[1]=SimpleRainbowMode(50)

httpd = HTTPServer(('', 8000), LightsRequestHandler)
httpd.serve_forever()
