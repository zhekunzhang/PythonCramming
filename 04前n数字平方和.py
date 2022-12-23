def pre_sumn(num):
    sum=0
    for idx in range(1,num+1):  
        print(idx)
    #     sum+=idx*idx
    #return sum  如果不屑返回值 默认有个None
        sum+=idx*idx
    return sum  

number=3
print(pre_sumn(number))