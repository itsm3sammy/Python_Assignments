# Decimal to int and string conversion
x = float(input("Enter a number: "))
y = int(x)
z = str(x)

print("Original Input:", x)
print("Conversion to integer:", y)
print("Conversion to string:", '"' + z + '"')


# Display initials from name
n = input("Enter your full name: ")
p = n.split()
if len(p) >= 2:
    i = p[0][0].upper() + "." + p[1][0].upper()
    print("The initials are:", i)


# Reverse string
s = input("Enter a string: ")
r = s[::-1]
print("Reversed string is:", r)


# Substring from index
w = input("Enter a word: ")
i = int(input("Enter a starting index: "))

if i < len(w):
    print("Substring from", i, "is:", w[i:])
else:
    print("Invalid index, try again!")


# Extract domain from email
e = input("Enter an email: ")

if '@' in e:
    d = e.split("@")[-1]
    print("Domain:", d)
else:
    print("Invalid email, try again!")


# Swap first and last character
t = input("Enter a word: ")

if len(t) > 1:
    u = t[-1] + t[1:-1] + t[0]
    print("Swapped word:", u)
else:
    print("Word must have at least two characters!")