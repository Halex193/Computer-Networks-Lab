import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 1921))
print('Server started!')
sock.listen(1)
connection, address = sock.accept()
print(address)
numberSum = 0
nr = connection.recv(4)
nr = struct.unpack('!i', nr)[0]
for i in range(nr):
    numberSum += struct.unpack('!i', connection.recv(4))[0]
connection.send(struct.pack('!i', numberSum))
connection.close()
sock.close()
