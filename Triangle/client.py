import socket
import struct


def sendInt(s, n):
    data = struct.pack('!i', n)
    s.send(data)


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        a = int(input("Latura 1: "))
        b = int(input("Latura 2: "))
        c = int(input("Latura 3: "))
        sock.connect(('localhost', 1921))
        sendInt(sock, a)
        sendInt(sock, b)
        sendInt(sock, c)
        data = sock.recv(100)
        isTriangle = struct.unpack('!?', data)[0]
        print(isTriangle)
    except (ConnectionRefusedError, ConnectionAbortedError):
        print("Connection was refused")
        exit(0)
    except struct.error:
        print('Received data was different than expected')
    finally:
        sock.close()
