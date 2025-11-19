import http.server
import socketserver
import os

# Print current directory
print(f"Current directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir('.')}")

# Check if admin_dashboard.html exists
if os.path.exists('admin_dashboard.html'):
    print("admin_dashboard.html found")
else:
    print("admin_dashboard.html NOT found")

PORT = 3001  # Changed from 3000 to 3001 to avoid conflicts

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend server running at http://localhost:{PORT}/")
    print(f"Open http://localhost:{PORT}/index.html in your browser")
    httpd.serve_forever()