import BaseHTTPServer
import os

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

class PatientHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request for %s" % self.path)

        file_path = 'records/' + self.path.lstrip('/')
        try:
            with open(file_path, 'r') as f:
                patient_data = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(patient_data)
        except IOError:
            self.send_error(404, "File Not Found: %s" % self.path)

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer((HOST_NAME, PORT_NUMBER), PatientHandler)
    print("Starting server on %s:%s..." % (HOST_NAME, PORT_NUMBER))
    server.serve_forever()
