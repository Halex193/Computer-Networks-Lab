import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0.0.0.0', 1921))
numbers = []
num = 0
while True:
    num = int(input("number = "))
    if num == 0:
        break
    numbers.append(num)
sock.send(struct.pack('!i', len(numbers)))
for i in numbers:
    sock.send(struct.pack('!i', i))
message = sock.recv(4)
print(struct.unpack('!i', message)[0])
sock.close()
