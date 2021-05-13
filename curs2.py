import sys

print("aaa")

name = "Ana"

if name:
    print(name)
else:
    print("nu avem definit nici un nume")

x = 1.2
y = 1.2

if x is y:
    print("eq")


print(hex(id(x)))
print(hex(id(y)))

fp = {"name": "Jhon"}
fs = {"name": "Jhon"}

print(hex(id(fp)))
print(hex(id(fs)))
print(id(fs) - id(fp))

print(sys.getsizeof(fs))


