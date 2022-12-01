import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to connect to a server
s.connect(("127.0.0.1", 55_555))

# receive the msg that the client sends
msg = s.recv(1024) # size to the msg to receive
s.close()

print(msg.decode())
