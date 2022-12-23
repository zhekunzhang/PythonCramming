studentinfo =[
    {"num":1101,"name":"张三","score":98},
    {"num":1102,"name":"李四","score":91},
    {"num":1103,"name":"王五","score":92},
    {"num":1104,"name":"五六","score":93},
]

studentinfo_sort=sorted(studentinfo,key=lambda  x:x["score"] )
print(studentinfo)
print(studentinfo_sort)