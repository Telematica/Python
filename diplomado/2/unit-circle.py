import math

# r = √xˆ2+yxˆ2
def isWithinUnitCircle(x,y):
    radius = math.sqrt(math.pow(x,2) + math.pow(y,2))
    if radius == 1:
        print("Radius: ",radius, "is on the Unit Circle")
    elif radius < 1:
        print("Radius: ",radius, "is within the Unit Circle")
    elif radius > 1:
        print("Radius: ",radius, "is outside the Unit Circle")
    return radius

isWithinUnitCircle(0.7071067811865476,0.7071067811865476)
isWithinUnitCircle(0,0)
isWithinUnitCircle(0.1,0.1)
isWithinUnitCircle(1,1)

print(math.sqrt(0.5))
'''
r=1 sobre
r<1 dentro
r>1 fuera
'''