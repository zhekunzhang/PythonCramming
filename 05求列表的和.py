def listsum(ll):
    sum=0
    for item in ll:
        sum+=item
    return sum

lista=[1,2,3,4]
print(listsum(lista))

#py 也提供了sum 可以直接求list sum
print(sum(lista))