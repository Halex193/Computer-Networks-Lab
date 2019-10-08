import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("172.30.114.144", 1234))
while True:
    s.sendto(input("Hori: ").encode(), ("172.30.114.152", 1234))
    print("Andu:", s.recvfrom(100)[0].decode())