# Tab spacing (4 blank spaces)

a = 1
n = 10
while(a<n):
    print("test")
    a += 1

# Python's built-in id() function returns the address where the object is stored.
print(
    id(a),
    id(1),
    id(2.345),
    id(False),
    id(True),
    id([]),
    id({}),
    id(()),
)

print(a)
del a
# print(a)

print(type(n))