import socket
import threading

class ThreadedServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("localhost", 14567))

    def listen(self):
        self.sock.listen(5)
        while True:
            connection, addr = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (connection, addr)).start()
            
    def listenToClient(self, connection, addr):
        def whois( request, whois_server):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((whois_server, 43))
                request = socket.gethostbyname(request)
                sock.sendall(b"%b\n" % request.encode("utf-8"))
                page = ""
                while True:
                    data = sock.recv(8196)
                    if not data:
                        break
                    page = page + data.decode("utf-8")
                return page
        
        while True:
            data = connection.recv(1024)
            print(data.decode('utf-8'))
            result = whois(data.decode('utf-8'), "whois.ripe.net")
            if not data:
                break
            connection.sendall(result.encode('utf-8'))


if __name__ == "__main__":
    ThreadedServer().listen()
