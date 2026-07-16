from http.server import BaseHTTPRequestHandler, HTTPServer
from core.pollard_rho import PollardRho
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        n = data['n']
        factors = PollardRho.factor(n)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'factors': factors}).encode())

def run_server(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...
')
    httpd.serve_forever()

def main():
    run_server()
if __name__ == '__main__':
    main()