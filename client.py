import socket
host="localhost"
port=5000

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host,port))
msg=server.recv(1024)
print("From Server: ",msg.decode())
string=input("Enter response (Enter exit to exit) :")

while string !='exit' :
    server.send(string.encode())
    data=server.recv(1024)
    
    print("From Server: ",data.decode())
    string=input("Enter response :")
server.close()
