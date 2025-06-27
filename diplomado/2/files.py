import random as r

fh = open("3numeros.txt", "wt")
for k in range(3):
    fh.write(str(r.random())+"\n")

fh.close()

l = []

with open("3numeros.txt") as fh:
    for line in fh:
        n = line.strip()
        n = float(n)
        l.append(n)

print(l)