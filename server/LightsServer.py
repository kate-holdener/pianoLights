from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import urllib
from lights.SimpleMode import SimpleMode

class LightsRequestHandler(BaseHTTPRequestHandler):
    mode = None
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
        #if self.path == '/lights':
        #    do_lights(self)
        qs = urllib.parse.parse_qs(o.query)
        action=int(o.query.find('event'))
        key=int(o.query.find('key'))
        velocity=int(o.query.find('velocity'))
        deltatime=float(o.query.find('deltatime'))
        mode.processEvent(((action,key,velocity),deltatime))

    def do_lights(self):
        pass 

LightsRequestHandler.mode = SimpleMode(50, (255,0,0), (0,0,255))
httpd = HTTPServer(('', 8000), LightsRequestHandler)
httpd.serve_forever()
