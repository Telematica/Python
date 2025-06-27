def fn(a, b, c):
    return (a, b, c)


def fn2(a, b, c):
    return [a, b, c]


def fn3(a, b, c):
    return {a, b, c}


def fn4(a=1, b=2):
    return a-b

# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
# https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
# https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
def foo(name, /, **kwds):
    return 'name' in kwds


print(type(fn(1, 2, 3)))
print(type(fn2(1, 2, 3)))
print(type(fn3(1, 2, 3)))
print(fn4(b=2, a=1))
print(foo(1, **{'name': 2}))
