# Read and write to file
def r(p):
    c = ""
    with open(p, "r") as f:
        for i in f:
            c += i
    return c

def w(p, c):
    with open(p, "w") as f:
        return f.write(c)

a = input("Enter path to file: ")
b = input("Enter content to enter: ")

w(a, b)
print(r(a))


# Find longest word in file
def lw(p):
    l = ""
    with open(p, "r") as f:
        for x in f:
            y = x.split()
            for z in y:
                if len(z) > len(l):
                    l = z
    return l

print("Longest word is", lw(a))


# Check if file is empty
def e(p):
    with open(p, "r") as f:
        return not f.read(1)

print(e(a))


# Reverse file content and write to new file
def rev(p):
    with open(p, "r") as f:
        c = f.read()[::-1]
    with open("reversed.txt", "w") as f:
        f.write(c)

rev(a)
print("Reversed content is in reversed.txt")


# Convert list of strings to uppercase
def up(l):
    return list(map(lambda x: x.upper(), l))

m = []
n = int(input("Enter number of elements to add in list: "))
for i in range(n):
    m.append(input(f"Enter word {i+1}: "))

print("Uppercase list:", up(m))


# Filter even length words
def fl(l):
    return list(filter(lambda x: len(x) % 2 == 0, l))

print("Words that have even length:", fl(m))


# Process file with lambda: uppercase each word
def proc(p):
    with open(p, "r") as f:
        l = f.readlines()

    u = []
    for line in l:
        u_line = " ".join(map(lambda x: x.upper(), line.split()))
        u.append(u_line)

    with open(p, "w") as f:
        for item in u:
            f.write(item + "\n")

proc(a)
print("The file has been processed and updated.")
