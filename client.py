import socket
import sys
 
 
def main():
    args = sys.argv
    result = whois(args[1], args[2])
    print(result)
 
 
def whois(request, whois_server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((whois_server, 14567))
        request = socket.gethostbyname(request)
        sock.sendall(b"%b\n" % request.encode("utf-8"))
        page = ""
        data = sock.recv(8196)
        page = page + data.decode("utf-8")
        return page
 
#result = whois(b' 95.82.220.91', "whois.ripe.net")
result = whois(b'95.82.220.91', "localhost")
print(result)
#main()
