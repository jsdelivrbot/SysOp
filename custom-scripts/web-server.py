import SimpleHTTPServer
import SocketServer
import os
import sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        os.system("sh $BASE_DIR/../etc/system-info.sh > info.txt")
        info = open ('info.txt', 'r')
        html = open ('index.html', 'w')
        html.write('<html><head><title>System Info</title></head><strong>Data e hora do Sistema:</strong> ')
        html.write(info.readline())
        html.write('<strong>Uptime:</strong>')
        html.write(info.readline())
        html.write('</html>')
        html.close()
        info.close()
        self.path = '$BASE_DIR/../index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
