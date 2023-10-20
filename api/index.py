import json
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import pytz

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Get the current time in Madrid
        madrid_tz = pytz.timezone('Europe/Madrid')
        madrid_time = datetime.now(madrid_tz).strftime('%Y-%m-%d %H:%M:%S')

        response_dict = {
            "message": "Hello guys!",
            "timestamp": madrid_time
        }
        self.wfile.write(json.dumps(response_dict).encode('utf-8'))
        return
