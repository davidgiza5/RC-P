from random import randint


class Mesaj:
    def __init__(self):
        self.header = ""
        self.mesaj = ""
        self.token = ""
        self.pachet = ""

    def set(self, pachet):
        self.pachet = pachet

    def crearePachet(self, header, mesaj):
        self.header = header
        self.mesaj = mesaj
        self.token = randint(0, 65536)
        self.pachet = ("" + str(header.header)).encode('UTF-8')
        if 0 < header.getTokenLength() <= 8:
            self.pachet = self.pachet+(str(self.token)).encode('UTF-8')
        if mesaj != "":
            self.packet = self.pachet+(str(self.mesaj)).encode('UTF-8')
        return self.pachet

    def getP(self):
        return self.pachet