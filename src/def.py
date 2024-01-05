def fn(a, b, c):
    return (a, b, c)


def fn2(a, b, c):
    return [a, b, c]


def fn3(a, b, c):
    return {a, b, c}


def fn4(a=1, b=2):
    return a-b


print(type(fn(1, 2, 3)))
print(type(fn2(1, 2, 3)))
print(type(fn3(1, 2, 3)))
print(fn4(b=2, a=1))
