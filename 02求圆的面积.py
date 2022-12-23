import math
# print(math.pi)
def compute_are_circle(r):
    #return math.pi*r*r
    return round(math.pi*r*r,2)
    #但是只保留两位小数
print("area of 3 is :",compute_are_circle(3))
print("area of 4 is :",compute_are_circle(4))
print("area of 5 is :",compute_are_circle(5))