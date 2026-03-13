import http.server
import socketserver
import os

PORT = 3000
DIRECTORY = "/Users/saikrishna/Downloads/NextleapProjects /Bengaluru_-Restaurant_AIrecommendations_Zomato-"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
