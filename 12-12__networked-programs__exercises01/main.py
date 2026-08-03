import socket
import sys
url = input("Enter URL: ")
try:
    parts = url.split('/')
    host = parts[2]
    path = '/' + '/'.join(parts[3:])
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
except Exception as e:
    sys.exit("Error: " + str(e))
cmd = f"GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n"
mysock.send(cmd.encode())
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()
