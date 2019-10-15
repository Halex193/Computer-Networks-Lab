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


def recvNBytes(s, n):
    data = b''
    while len(data) < n:
        more = s.recv(n - len(data))
        if not more:
            raise EOFError()
        data += more
    return data


def recvValue(s, format):
    data = recvNBytes(s, struct.calcsize(format))
    return struct.unpack(format, data)[0]


def sendValue(s, format, value):
    data = struct.pack(format, value)
    s.send(data)


if __name__ == '__main__':
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            command = input("Enter command: ")
            sock.connect(("127.0.0.1", 1921))
            if command == 'exit':
                break
            command = command.encode()
            sendValue(sock, '!h', len(command))
            sock.send(command)
            while True:
                lineLength = recvValue(sock, '!h')
                if lineLength == -1:
                    break

                line = recvNBytes(sock, lineLength).decode()
                print(line)
            exitCode = recvValue(sock, '!h')
            print('\nExit code: ' + str(exitCode))
            sock.close()
        except (ConnectionRefusedError, ConnectionAbortedError):
            print("Connection was refused")
            exit(0)
        except struct.error:
            print('Received data was different than expected')
        finally:
            sock.close()
