import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", 1921))
    data = struct.pack('!H', 65535)
    sock.send(data)
except ConnectionRefusedError:
    print("Connection was refused")
    exit(0)
except struct.error:
    print('Received data was different than expected')
finally:
    sock.close()
