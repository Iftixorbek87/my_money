from http.server import HTTPServer, SimpleHTTPRequestHandler
import signal
import sys

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'<h1>SERVER ISHLAYAPTI!</h1><p>Server is running on port 8000</p>')

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    def signal_handler(sig, frame):
        print('\nShutting down the server...')
        httpd.server_close()
        print('Server stopped')
        sys.exit(0)
    
    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, signal_handler)
    
    print(f'Starting server on port {port}...')
    print('Press Ctrl+C to stop the server')
    httpd.serve_forever()

if __name__ == '__main__':
    run()