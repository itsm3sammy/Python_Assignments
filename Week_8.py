class A:
    def calc(self):
        return 0

class C(A):
    def __init__(self, r):
        self.r = r

    def calc(self):
        return 3.14 * self.r ** 2

class R(A):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calc(self):
        return self.l * self.b

def m():
    x = C(5)
    y = R(10, 5)
    print(f"Area of circle: {x.calc()}")
    print(f"Area of rectangle: {y.calc()}")

m()
