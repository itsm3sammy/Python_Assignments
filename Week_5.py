# 1. Square all numbers
def s(l):
    for n in l:
        sq = n ** 2
        print(f"Square of {n} is: {sq}")

# 2. Print square only if the number is even
def se(l):
    for n in l:
        if n % 2 == 0:
            sq = n ** 2
            print(f"Square of even {n} is: {sq}")

# 3. Store even squares in a list
def sl(l):
    e = []
    for n in l:
        if n % 2 == 0:
            sq = n ** 2
            e.append(sq)
    return e

x = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Input list: {x}")
s(x)
se(x)
print(f"New list of even square is: {sl(x)}")
