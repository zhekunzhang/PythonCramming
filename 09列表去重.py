def getunie(lista):
    result=[]
    for item in lista:
        if item not in result:
            result.append(item)
    return result
aaaaa=[1,1,1,2,2,2,3,3,3,4,4]
print(f"source list {aaaaa} uniquelist:",getunie(aaaaa))
print(f"source list {aaaaa} uniquelist:",list(set(aaaaa)))