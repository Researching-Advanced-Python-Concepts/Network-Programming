# Socket works at transport layer of the OSI model
# 1. Choose whether to use internet socket or UNIX socket
# 2. Type of protocol to use (TCP or UDP)
    # - TCP for connection oriented, for sensible data
        # 
    # - UDP connection less, faster, loss can occur
# 3. Which IP we're going to use?
# 4. Which port to use?

import socket

# kind of socket, internet socket
# protocol, tcp
# SOCK_DGRAM for udp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 55_555))
# to have our server or places our socket into listening mode
s.listen()


# accept the connection
while True:
    # when a client tries to connect to the server or to the socket here
    # and we accept it
    client, address = s.accept()
    # we can send data to this client
    print(f"Connected to {address}")
    # encode with UTF-8 default
    client.send("You are connected!".encode())
    client.close()

# this works everywhere, if we provide a public server ip
# and someone from the other end of the world could use the client
# to connect to the server
# we can run this across networks
