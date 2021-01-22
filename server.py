import getopt
import sys
from coapthon.server.coap import CoAP


class BasicResource():
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server)
        self.payload = "Basic Resource"
        self.resource_type = "resursa"
        self.content_type = "text"



class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        print ("Start server pe ip " + host + " si port: " + str(port))
        print (self.root.dump())


def main(argv):
    ip = "127.0.0.1"
    port = 5683

    try:
        opts, args = getopt.getopt(argv, "hi:p:m", ["ip=", "port="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = int(arg)

    server = CoAPServer(ip, port)
    try:
        server.listen(5)
    except KeyboardInterrupt:
        print ("Inchidere server")
        server.close()
        print ("Iesire")


if __name__ == "__main__":
    main(sys.argv[1:])