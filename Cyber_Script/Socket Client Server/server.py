import socket

host="127.0.0.1"
port=2125

with socket.socket() as socket:
    socket.bind((host,port))
    socket.listen()
    conn,addr=socket.accept()
    with conn:
        print('Bağlantı yapılıd: ',addr)
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)