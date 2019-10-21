import socket
import struct


def sendInt(s, n, address):
    data = struct.pack('!i', n)
    s.sendto(data, address)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        a = int(input("Latura 1: "))
        b = int(input("Latura 2: "))
        c = int(input("Latura 3: "))
        address = ('localhost', 1921)
        sendInt(sock, a, address)
        sendInt(sock, b, address)
        sendInt(sock, c, address)
        data = sock.recvfrom(100)
        isTriangle = struct.unpack('!?', data[0])[0]
        print(isTriangle)
    except struct.error:
        print('Received data was different than expected')
    finally:
        sock.close()
