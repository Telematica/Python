import random as r

[print(x*3) for x in range(15)]

lr = [r.randint(10,23) for x in range(15)]
print(lr)
lr.reverse()
print(lr)