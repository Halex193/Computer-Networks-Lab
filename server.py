import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))
print("Server started!")

while True:
    message, location = s.recvfrom(100)
    print(message.decode(), "-", location)
