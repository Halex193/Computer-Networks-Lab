import socket
import struct


def readString(s):
    result = b''
    done = False
    while not done:
        readData = s.recv(100)
        result += readData
        for byte in readData:
            if byte == 0:
                done = True
    return result.decode()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("127.0.0.1", 1921))
    message = "This is the string"
    data = message.encode() + b'\0'
    sock.send(data)
    print(readString(sock))
except ConnectionRefusedError:
    print("Connection was refused")
    exit(0)
except struct.error:
    print('Received data was different than expected')
finally:
    sock.close()
