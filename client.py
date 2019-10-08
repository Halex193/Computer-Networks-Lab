import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    s.sendto(input("Mesaj: ").encode(), ("172.30.115.144", 9999))
