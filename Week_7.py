class S:
    def __init__(self, n, i):
        self.n = n
        self.i = i
        self.c = []

    def add(self, x):
        if x in self.c:
            print(f"{x} is already enrolled")
        else:
            self.c.append(x)
            print(f"{x} has been added successfully!")

    def rem(self, x):
        if x in self.c:
            self.c.remove(x)
            print(f"{x} removed successfully!")
        else:
            print(f"{x} doesn't exist in the list")

    def show(self):
        if not self.c:
            print(f"{self.n} is not enrolled in any courses")
        else:
            print(self.n, "is enrolled in:", ", ".join(self.c))

s = S("Sujit", 999)
s.add("Computer")
s.add("Physics")
s.show()

s.rem("Physics")
s.show()

s.add("Python")
s.show()
