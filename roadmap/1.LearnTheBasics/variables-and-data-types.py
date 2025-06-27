n:int = 1

num = 2

float_num:float = 4.5

str:str = ""
str2 = ''

str3 = """ hello
world
"""


def returnfloat(a:int, b:float, c):
    return a,b,c

returnfloat(1,1.1,"aaa")

print(float_num)

# Python Multi-Line Statements

item_one = 1

total = item_one + \
    2 + \
    3

print(total,str3)