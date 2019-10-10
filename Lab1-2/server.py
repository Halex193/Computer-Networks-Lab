import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = None
try:
    sock.bind(('0.0.0.0', 1921))
    sock.listen(1)
    print('Server started')
    while True:
        connection, address = sock.accept()
        numberOfSpaces = 0
        done = False
        while not done:
            data = connection.recv(1)
            if data != b'\0':
                if data.decode() == ' ':
                    numberOfSpaces += 1
            else:
                done = True
        connection.send(struct.pack('!i', numberOfSpaces))
        print('Sent {0}'.format(numberOfSpaces))
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
