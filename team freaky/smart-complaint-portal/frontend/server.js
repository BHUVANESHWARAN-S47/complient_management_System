const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3000;

const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.wav': 'audio/wav',
  '.mp4': 'video/mp4',
  '.woff': 'application/font-woff',
  '.ttf': 'application/font-ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'application/font-otf',
  '.wasm': 'application/wasm'
};

const server = http.createServer((req, res) => {
  console.log(`Request received: ${req.method} ${req.url}`);
  
  // Parse the request URL
  const parsedUrl = url.parse(req.url);
  let pathname = `.${parsedUrl.pathname}`;
  
  // Handle root path
  if (pathname === './') {
    pathname = './index.html';
  }
  
  // Get the file extension
  const ext = path.parse(pathname).ext;
  const map = MIME_TYPES[ext] || 'text/plain';
  
  // Read the file
  fs.readFile(pathname, (err, data) => {
    if (err) {
      console.log(`File not found: ${pathname}`);
      res.writeHead(404);
      res.end('File not found');
    } else {
      console.log(`File served: ${pathname}`);
      res.writeHead(200, { 'Content-Type': map });
      res.end(data);
    }
  });
});

server.listen(PORT, () => {
  console.log(`Frontend server running at http://localhost:${PORT}/`);
  console.log(`Open http://localhost:${PORT}/index.html in your browser`);
});