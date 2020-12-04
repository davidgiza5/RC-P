import socket

class Socket:
    localIP = "192.168.0.1"
    localPort = 12345
    flag  = False

    @staticmethod
    def init(self, addr='', localPort='1234'):
        if(Socket.flag == True):
            exit

        Socket.flag = True
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((addr,local))
