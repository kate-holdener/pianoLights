from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import urllib
from lights.SimpleMode import SimpleMode

class LightsRequestHandler(BaseHTTPRequestHandler):
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
        print(qs)
        #imsi = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('imsi', None)
        #print(imsi)

    def do_lights(self):
        pass 

    def do_POST(self):
        self._set_headers()
        print(self.headers)
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}".format(post_body))

class LightsServer(HTTPServer):
    def __init__(self, hostPort, handler):
        super().__init__(hostPort, handler)
        self.mode = None

    def setLightsMode(self, mode):
        self.mode = mode
        
httpd = LightsServer(('', 8000), LightsRequestHandler)
mode = SimpleMode(50, (255,0,0), (0,0,255))
httpd.setLightsMode(mode)
httpd.serve_forever()
