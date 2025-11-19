#!/usr/bin/env python3
"""
Simple HTTP server to serve frontend files
"""
import http.server
import socketserver
import os

# Check if we're in the frontend directory already
if not os.path.exists('index.html'):
    # Check if frontend directory exists
    if os.path.exists('frontend'):
        # Change to frontend directory
        os.chdir('frontend')

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend server running at http://localhost:{PORT}/")
    print(f"Open http://localhost:{PORT}/index.html in your browser")
    httpd.serve_forever()