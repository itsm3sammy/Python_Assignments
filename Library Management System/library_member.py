class M:
    def __init__(self, i, n):
        self.__i = i
        self.__n = n
        self.__b = []

    @property
    def id(self):
        return self.__i

    @property
    def n(self):
        return self.__n

    @property
    def b(self):
        return self.__b

    def br(self, x):
        self.__b.append(x)

    def rt(self, x):
        self.__b.remove(x)

    def d(self):
        return [i.t for i in self.__b]
