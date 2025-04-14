from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass

if __name__ == "__main__":
         server_address = ("", 8000)
         httpd = ThreadingHTTPServer(server_address, SimpleHTTPRequestHandler)
         print("Serving HTTP on port 8000...")
         httpd.serve_forever()
