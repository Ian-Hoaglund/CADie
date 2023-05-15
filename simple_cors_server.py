#!/usr/bin/env python3
# encoding: utf-8

"""Use instead of `python3 -m http.server` when you need CORS"""
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()


httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
httpd.serve_forever()

"""

from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)

#httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
#httpd.serve_forever()