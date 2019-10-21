# UDP client

import socket
import struct

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        data = "Salut servitorule".encode()
        sock.sendto(data, ('localhost', 1921))

    except struct.error:
        print('Received data was different than expected')
    finally:
        sock.close()
