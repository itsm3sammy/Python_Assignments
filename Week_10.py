class E:
    def __init__(self, i, s):
        self.i = i
        self.__s = s

    @property
    def s(self):
        return self.__s

    def info(self):
        print(f"Employee Name: {self.i}")
        print(f"Employee Salary: {self.s}")

class M(E):
    def __init__(self, i, s, d):
        super().__init__(i, s)
        self.d = d

    def info(self):
        print(f"Manager Name: {self.i}")
        print(f"Manager Salary: {self.s}")
        print(f"Manager department: {self.d}")

class D(E):
    def __init__(self, i, s, p):
        super().__init__(i, s)
        self.p = p

    def info(self):
        print(f"Developer Name: {self.i}")
        print(f"Developer Salary: {self.s}")
        print(f"Developer programming language: {self.p}")

    def get_s(self):
        return self.s

    def set_s(self, s):
        if s > 0:
            self._E__s = s
        else:
            print("Salary must be a positive number!")

    def get_p(self):
        return self.p

    def set_p(self, p):
        self.p = p

def m():
    e = E(101, 50000)
    mg = M(201, 90000, "HR")
    d = D(301, 150000, "Python")

    e.info()
    mg.info()
    d.info()

    print("\nUpdating Developer's salary...")
    d.set_s(160000)
    print(f"Updated Developer Salary: {d.get_s()}")

    print("\nUpdating Developer's programming language...")
    d.set_p("Java")
    print(f"Updated Developer Programming Language: {d.get_p()}")

m()
