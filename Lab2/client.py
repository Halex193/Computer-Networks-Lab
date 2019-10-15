import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(('127.0.0.1', 1921))
    num = struct.pack('!i', 193)
    sock.send(num)
    num = sock.recv(struct.calcsize('!h'))
    num = struct.unpack('!h', num)[0]
    data = sock.recv(num)
    print(data.decode())
except:
    print('No connection')
finally:
    sock.close()