import SimpleHTTPServer
import SocketServer
import os
import sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        os.system("sh $BASE_DIR/../etc/system-info.sh")
        html = open ('index.html', 'w')
        
        html.write('<html><head><title>System Info</title></head><body><strong>Data e hora do Sistema:</strong> ')
        date = open ('date.txt', 'r')        
        html.write(date.readline())
        date.close()

        html.write('<br/><strong>Uptime:</strong>')
        uptime = open ('uptime.txt', 'r')
        html.write(uptime.readline())
        uptime.close()

        html.write('<br/><strong>Modelo do processador:</strong> ')
        cpuinfo = open ('cpuinfo.txt', 'r')
        html.write(cpuinfo.readline())
        cpuinfo.close()
        
        
        html.write('<br/><strong>Quantidade de memoria RAM total e usada:</strong> ')        
        top = open ('top.txt', 'r')
        html.write(top.readline())
        
        html.write('<br/><strong>Capacidade ocupada do processador:</strong> ')    
        html.write(top.readline())
        
        html.write('<br/><strong>Versao do sistema:</strong> ')
        version = open ('version.txt', 'r')
        html.write(version.readline())
        version.close()

        html.write('<br/><strong>Lista de processos em execucao:</strong><br/>')
        top.readline()
        html.write('<table>')
        for line in top:
            html.write('<tr>')
            splitted = line.split()
            for word in splitted:
                html.write('<td>')
                html.write(word)
                html.write('</td>')
            html.write('</tr>')      
        top.close()
        html.write('</table>')
        html.write('</body>')
        html.write('</html>')
        html.close()

        self.path = '$BASE_DIR/../index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler

server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
