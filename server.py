import socket
host='localhost'
port=5000


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
client, addr=s.accept()
print("Connection accepted from :",str(addr))
client.send(b"Hello client!")
while True:
    data=client.recv(1024)
    if not data:
        break
    print("From Client :", str(data.decode()))
    reply= input("Enter Response :")
    client.send(reply.encode())

client.close()
