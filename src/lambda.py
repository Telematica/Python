annonFn = lambda a,b,c : (a + b + c) * 10
IIFE = (lambda a,b,c: a+b+c)(1,2,3)

print(
    annonFn(1,2,3), 
    IIFE,
    (lambda a,b,c: a*b*c)(4,5,6)
)