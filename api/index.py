import os
import json
import psycopg2
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

        # Get the environment variables
        postgres_user = os.environ['POSTGRES_USER']
        postgres_password = os.environ['POSTGRES_PASSWORD']
        postgres_host = os.environ['POSTGRES_HOST']
        postgres_database = os.environ['POSTGRES_DATABASE']

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=postgres_database,
            user=postgres_user,
            password=postgres_password,
            host=postgres_host
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute a SQL query to fetch data from the "pilgrims" table
        cur.execute("SELECT num_pilgrims, date FROM pilgrims;")
        pilgrims_data_raw = cur.fetchall()

        # Format the data as a list of dictionaries
        pilgrims_data = [{"num_pilgrims": row[0], "date": row[1].strftime('%Y-%m-%d')} for row in pilgrims_data_raw]

        # Close the cursor and connection
        cur.close()
        conn.close()

        response_dict = {
            "message": "Hello guys!",
            "timestamp": madrid_time,
            "pilgrims_data": pilgrims_data
        }
        self.wfile.write(json.dumps(response_dict).encode('utf-8'))
        return
