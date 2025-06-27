import math

# 2) Radius of Circle Inscribed in a Triangle of Sides a,b,c
# r = √s(s-a)(s-b)(s-c)/2
# where s = 1/2(a+b+c) = semiperimeter
def radiusOfCircleInscribedInATriangleOfSidesABC(a,b,c):
    s = 0.5*(a+b+c)
    r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    return r

# 3) Radius of Circle Circumscribing a Triangle of Sides a,b,c
# R = abc/4√s(s-a)(s-b)(s-c)
# where s = 1/2(a+b+c) = semiperimeter
def radiusOfCircleCircumscribingATriangleOfSidesABC(a,b,c):
    s = 0.5*(a+b+c)
    R = a*b*c/(4*math.sqrt(s*(s-a)*(s-b)*(s-c)))
    return R


a = 5
b = 7
c = 11

print(radiusOfCircleInscribedInATriangleOfSidesABC(a,b,c))
print(radiusOfCircleCircumscribingATriangleOfSidesABC(a,b,c))

# output: 1.1277141173341685
# output: 7.421708293566749