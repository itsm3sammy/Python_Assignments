import random

# Student class with average grade
class S:
    def __init__(self, n, a):
        self.n = n
        self.a = a
        self.g = []

    def avg(self):
        if not self.g:
            print(f"{self.n}'s grades have not been entered!")
            return 0
        t = 0
        for i in self.g:
            t += i
        return t / len(self.g)

s1 = S("Sujit", 20)
s2 = S("Sajjan", 23)
s3 = S("Swojan", 21)

s1.g = [88, 89, 93]
s2.g = [74, 61, 83]
s3.g = [85, 96, 75]

print(f"{s1.n}'s average grade is {s1.avg()}")
print(f"{s2.n}'s average grade is {s2.avg()}")
print(f"{s3.n}'s average grade is {s3.avg()}")


# Book class with short title method
class B:
    def __init__(self, t, a):
        self.t = t
        self.a = a

    def short(self):
        return self.t[:10] if self.t else "No title"

b1 = B("Harry Potter and the Sorcerers Stone", "J.K. Rowling")
b2 = B("One P", "Eiichiro Oda")
b3 = B("Goosebumps: Haunted Halloween", "R.L. Stine")

print(f"{b1.t}'s shortened version is {b1.short()}")
print(f"{b2.t}'s shortened version is {b2.short()}")
print(f"{b3.t}'s shortened version is {b3.short()}")


# StudentResult class with pass check
class R:
    def __init__(self, n, a, g):
        self.n = n
        self.a = a
        self.g = g

    def pass_status(self):
        if 50 <= self.g <= 100:
            return True
        elif 0 < self.g < 50:
            return False
        else:
            print(f"{self.n}'s grades are invalid!")

r1 = R("Sujit", 20, 95)
r2 = R("Sajjan", 23, 101)
r3 = R("Swojan", 21, 21)

print(f"{r1.n}'s pass status: {r1.pass_status()}")
print(f"{r2.n}'s pass status: {r2.pass_status()}")
print(f"{r3.n}'s pass status: {r3.pass_status()}")


# ShoppingCart class with total price
class C:
    def __init__(self):
        self.i = []

    def add(self, n, p):
        if p < 0:
            print(f"Invalid price for {n}")
        else:
            self.i.append({"n": n, "p": p})

    def total(self):
        return sum(x["p"] for x in self.i)

c = C()
c.add("Milk", 100)
c.add("KitKat", 120)
c.add("Airpods", 5500)
c.add("Chips", 200)

print(f"The grand total of items in the shop is Rs.{c.total()}")


# TextAnalyzer with word count
class T:
    def __init__(self):
        self.s = ""

    def add(self, w):
        self.s += (" " + w) if self.s else w

    def count(self):
        return len(self.s.split())

t = T()
t.add("Hello I am")
t.add("I am testing")
t.add("this method")

print("The count of words in the string is", t.count())


# Playlist with shuffle and display
class P:
    def __init__(self):
        self.s = []

    def add(self, t, a):
        self.s.append({"t": t, "a": a})

    def shuf(self):
        random.shuffle(self.s)

    def show(self):
        for i in self.s:
            print(f"Title: {i['t']}, Artist: {i['a']}")

p = P()
p.add("Great Gig in the Sky", "Pink Floyd")
p.add("Kashmir", "Led Zeppelin")
p.add("Nutshell", "Alice in Chains")
p.add("Lovers Rock", "TV Girl")
p.add("Save Your Tears", "The Weeknd")

p.shuf()
p.show()
