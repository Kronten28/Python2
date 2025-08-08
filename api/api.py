import BaseHTTPServer
import urlparse
import sqlite3
import logging

logging.basicConfig(filename='access.log', level=logging.INFO)

def init_db():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients
                 (id INTEGER PRIMARY KEY, name TEXT, ssn TEXT, diagnosis TEXT)''')
    c.execute("INSERT INTO patients (name, ssn, diagnosis) VALUES ('Alice', '123-45-6789', 'Anxiety')")
    conn.commit()
    conn.close()

class InsecureHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(parsed.query)
        if parsed.path == "/patient":
            name = params.get("name", [""])[0]

            logging.info("Query for patient: %s" % name)

            conn = sqlite3.connect('patients.db')
            c = conn.cursor()

            query = "SELECT * FROM patients WHERE name = '%s'" % name
            c.execute(query)
            result = c.fetchone()
            conn.close()

            if result:
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Name: %s, SSN: %s, Diagnosis: %s" % result[1:])
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("Patient not found")

def run():
    init_db()
    server = BaseHTTPServer.HTTPServer(('0.0.0.0', 8080), InsecureHandler)
    print("Starting insecure medical API on port 8080...")
    server.serve_forever()

if __name__ == '__main__':
    run()
