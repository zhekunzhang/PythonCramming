def get_jiecheng1(number):
    pass
def get_jiecheng(number):
    res=1
    while number>0:
        res*=number
        number-=1
    return res



print("jiecheng 6= ",get_jiecheng(6))
print("jiecheng 6= ",get_jiecheng(3))
print("jiecheng 6= ",get_jiecheng(100))


