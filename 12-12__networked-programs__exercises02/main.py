import socket
url = input("Enter URL: ")
parts = url.split("/")
host = parts[2]
path = "/" + "/".join(parts[3:])
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = "GET " + path + " HTTP/1.0\r\nHost: " + host + "\r\n\r\n"
mysock.send(cmd.encode())
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    text = data.decode()
    if count < 3000:
        remain = 3000 - count
        print(text[:remain], end="")
    count = count + len(text)
print()
print("Count:", count)
mysock.close()
