import http.server
from typing import Tuple

HOST_NAME: str = 'localhost'
PORT_NUMBER: int = 8080

class PatientHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        print(f"GET request for {self.path}")
        file_path: str = f'records/{self.path.lstrip("/")}'
        try:
            with open(file_path, 'r') as f:
                patient_data: str = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(patient_data.encode('utf-8'))
        except IOError:
            self.send_error(404, f"File Not Found: {self.path}")

if __name__ == '__main__':
    server: http.server.HTTPServer = http.server.HTTPServer((HOST_NAME, PORT_NUMBER), PatientHandler)
    print(f"Starting server on {HOST_NAME}:{PORT_NUMBER}...")
    server.serve_forever()