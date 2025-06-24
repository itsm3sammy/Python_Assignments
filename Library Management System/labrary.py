class L:
    def __init__(self):
        self.__i = {}
        self.__m = {}

    def add(self, x):
        self.__i[x.id] = x

    def reg(self, x):
        self.__m[x.id] = x
