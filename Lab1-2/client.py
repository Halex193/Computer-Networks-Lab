import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", 1921))
    message = "This is a funny program"
    pack = struct.pack('!{0}s'.format(len(message) + 1), message.encode() + b'\0')
    sock.send(pack)
    data = sock.recv(struct.calcsize('!i'))
    numberOfSpaces = struct.unpack('!i', data)[0]
    print(numberOfSpaces)
except ConnectionRefusedError:
    print("Connection was refused")
    exit(0)
except struct.error:
    print('Received data was different than expected')
finally:
    sock.close()
