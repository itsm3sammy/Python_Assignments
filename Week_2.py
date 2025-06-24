# Skip numbers divisible by 5, stop at >50
a = []
for b in range(1, 11):
    c = int(input("Enter an integer: "))
    a.append(c)

for d in a:
    if d > 50:
        break
    elif d % 5 == 0:
        continue
    print(d)


# Password strength checker
s = "@#$%&"
x = False
y = False
z = False

p = input("Enter your password: ")
for ch in p:
    if ("a" <= ch <= "z" or "A" <= ch <= "Z"):
        x = True
    elif ("0" <= ch <= "9"):
        y = True
    elif ch in s:
        z = True

if len(p) < 6 or (not y and x and not z):
    print("Weak")
elif len(p) >= 6 and y and x and not z:
    print("Moderate")
elif len(p) >= 8 and y and x and z:
    print("Strong")
else:
    print("Invalid password!")


# Alternate word reverse
t = input("Enter a sentence: ")
u = t.split()
for i in range(0, len(u), 2):
    u[i] = u[i][::-1]
print("Output:", " ".join(u))


# Count duplicate words
v = ["apple", "banana", "grapes", "apple", "apple", "mango", "banana", "apple", "banana", "mango"]
w = {}

for x in v:
    if x in w:
        w[x] += 1
    else:
        w[x] = 1

r = {k: v for k, v in w.items() if v > 1}
print("Output:", r)


# Book stock checker
b = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 2,
    'Book4': 7,
    'Book5': 4,
}

n = input("Enter name of book you want: ")
if n in b:
    while True:
        q = input("Enter number of copies you want to buy: ")
        if q.isdigit() and int(q) > 0:
            q = int(q)
            break
        else:
            print("Invalid entry! enter a valid number")

    if q <= b[n]:
        print("Available")
    elif q > b[n]:
        print("Partially Available")
else:
    print("Unavailable")


# Word frequency count
s = input("Enter a sentence: ").split()
d = {}

for w in s:
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

print("Output:", d)
