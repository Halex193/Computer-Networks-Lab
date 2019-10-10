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
connection = None
try:
    sock.bind(('0.0.0.0', 1921))
    sock.listen(1)
    print('Server started')
    connection, address = sock.accept()
    message = readString(connection)[::-1]
    connection.send(message.encode() + b'\0')
except OSError:
    print('Port is already taken')
except ConnectionRefusedError:
    print("Connection was refused")
    exit(0)
except struct.error:
    print('Received data was different than expected')
finally:
    sock.close()
    if connection is not None:
        connection.close()
