data = "ABCD"
# We want to get data printed out as A,B,C,D or
# A
# B
# C
# D

for i in data:
    print(i)

x = []
for i in data:
    x.append(i)

print(*x, sep=', ', end= '.')

# -----------------------------------
print(" ")
# -----------------------------------

print(any([c.islower() for c in data]))
data = "ABCd"
print(any([c.islower() for c in data]))

# -----------------------------------

print(any([i.isalpha() for i in data]))
print(any([i.isalnum() for i in data]))
print(any([i.isdigit() for i in data]))
print(any([i.islower() for i in data]))
print(any([i.isupper() for i in data]))

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(pow(a, b)+pow(c, d))