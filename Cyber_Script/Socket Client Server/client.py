import socket
host="127.0.0.1"
port=2125
with socket.socket() as socket:
     socket.connect((host,port))
     socket.sendall(b"Merhaba siber")
     data=socket.recv(1024)
print(data)
