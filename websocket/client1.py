import socket
s=socket.socket()
s.connect(('localhost',9999))
#run the server and then the client
#note the server after running the client: connected with address
#59730 is client's port no.
name=input('enter your name')
s.send(bytes(name,'utf-8'))
message=input(f"{name}:")
s.send(bytes(message,'utf-8'))
print(s.recv(1024))
message1=s.recv(1024).decode()
print("server:",message1)

#buffer size=1024
#run server to see new connection
# i.e. as many times we run we get new connection
#here only 3 times because only 3 clients

