# def ifdouble(num):
#     if num%2==0:
#         return num
#     else:
#         pass

def list_dobule(begin,end):
    res=[]
    for num in range(begin,end+1):
            if num%2==0:
                res.append(num)
    return res


begin=4
end=15
print(list_dobule(begin,end))

#列表推导式
list2=[item for item in range(begin,end+1) if item%2==0]
print(list2)
