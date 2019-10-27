import socket
import struct



if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        a = int(input("Latura 1: "))
        b = int(input("Latura 2: "))
        c = int(input("Latura 3: "))
        address = ('localhost', 1921)
        data = struct.pack('!iii', a, b, c)
        sock.sendto(data, address)
        data = sock.recvfrom(100)
        isTriangle = struct.unpack('!?', data[0])[0]
        print(isTriangle)
    except struct.error:
        print('Received data was different than expected')
    except ConnectionResetError:
        print('Connection was forcibly closed (maybe the server isn\'t started?)')
    finally:
        sock.close()
