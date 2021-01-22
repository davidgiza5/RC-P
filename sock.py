import socket
from _thread import *
import threading


local_ip = '127.0.0.1'
local_port = 5006
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((local_ip, local_port))

while 1:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    packRecv.set(data)
    head, mesg = packRecv.dispackPack()
    headerRecv.setHeader(head)
    headerRecv.buildHeader()
    headerRecv.setCode(headerRecv.getCodeClass(), headerRecv.getCodeDetail())
    if headerRecv.getCode() != 0:

        print("primire", len(data), "bytes de la ", addr)
        print("data de la client ", mesg)


        packSend.buildPack(headerSend, dataSent)

        headerSend.print()
        s.sendto(packSend.getPackege(), addr)
        print ("Start server pe ip " + local_ip + " si port: " + str(local_port))
        print (self.root.dump())

    else:
        print("ACK recive")

# sock.close()