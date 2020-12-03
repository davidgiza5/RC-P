import socket

class Socket:
    localIP = "192.168.0.1"
    localPort = 10000
    bufferSize = 1024
    UDPServerSocket = None
    flag  = False

    @staticmethod
    def init():
        if(Socket.flag == True):
            exit

        Socket.flag = True
        Socket.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        Socket.UDPServerSocket.bind((Socket.localIP, Socket.localPort))