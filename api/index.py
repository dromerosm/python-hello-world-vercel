import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_dict = {"message": "Hello guys!"}
        self.wfile.write(json.dumps(response_dict).encode('utf-8'))
        return
