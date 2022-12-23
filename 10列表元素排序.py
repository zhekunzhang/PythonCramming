#源列表  拷贝列表 升序降序
lista=[2,5425,12,44,123,4,5,1212]
print(id(lista))
lista.sort()
print(lista)
print(id(lista))


#返回一个新的列表 不改变源列表
listb=sorted(lista)
print(listb)
print(id(listb))


#python 反序排列
listb.sort(reverse=True)
print(listb)
print(id(listb))