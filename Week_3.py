# Count vowels in a string
def v(t):
    t = t.lower()
    v_set = "aeiou"
    f = []
    c = 0
    for ch in t:
        if ch in v_set:
            c += 1
            f.append(ch)
    return c, f

x = input("Enter a word: ")
a, b = v(x)
print("Vowel count:", a)
print("Vowels:", ",".join(b))


# Find max in a list without max()
def m(l):
    if not l:
        return None
    k = l[0]
    for i in l:
        if i > k:
            k = i
    return k

y = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum number:", m(y))


# Multiplication table
def t(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

z = int(input("Enter a number: "))
t(z)


# Longest word in sentence
def lw(s):
    w = s.split()
    if not w:
        return None
    l = w[0]
    for i in w:
        if len(i) > len(l):
            l = i
    return l

s = input("Enter a sentence separated by spaces: ")
print("Largest word:", lw(s))


# Sum of list elements
def s(l):
    if not l:
        return None
    r = 0
    for i in l:
        r += i
    return r

q = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sum of all elements in list:", s(q))


# Convert to title case
def tc(s):
    w = s.split()
    if not w:
        return None
    nw = [i.capitalize() for i in w]
    return " ".join(nw)

j = input("Enter a sentence: ")
print("New sentence:", tc(j))


# Check palindrome
def p(w):
    return w == w[::-1]

u = input("Enter a word: ")
print(p(u))


# Character frequency count
def f(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

r = input("Enter a string: ")
print(f(r))