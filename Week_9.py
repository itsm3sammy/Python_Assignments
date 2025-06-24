class E:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def info(self):
        print(f"Employee Name: {self.n}")
        print(f"Employee Salary: {self.s}")

class M(E):
    def __init__(self, n, s, t):
        super().__init__(n, s)
        self.t = t

    def info(self):
        print(f"Manager Name: {self.n}")
        print(f"Manager Salary: {self.s}")
        print(f"Manager team size: {self.t}")

    def b(self):
        return self.s + 0.10 * self.s

def m():
    e1 = E("Sajjan", 50000)
    e2 = E("Anush", 60000)
    m1 = M("Sujit", 90000, 10)

    e1.info()
    e2.info()
    m1.info()

    print(f"Bonus: {m1.b()}")

m()
