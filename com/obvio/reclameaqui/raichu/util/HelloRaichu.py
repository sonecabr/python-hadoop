__author__ = 'andre'


class HelloRaichu:
    count = 0

    def __init__(self):
        self.count = 0

    def showHello(self):
        print("Hello Raichu")
        self.count += 1
        print self.count

