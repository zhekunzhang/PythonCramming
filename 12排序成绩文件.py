#读取文件
#排序数据
#写出文件
import os
def read_file():
    res=[]
    with open("b站刷题\in.txt",'r',encoding="utf-8") as fin:
        for line in fin:
            line =line[0:-1]#将一行内容赋值给变量
            res.append(line.split(" "))#返回一个分割好的字符串
            print(line)
    res.remove(res[0])
    return res      

def sort_grades(datas):
    return sorted(datas,key=lambda x:int(x[3]),reverse=True)

def write_file(datas):
    with open("b站刷题\out.txt",'w',encoding="utf-8") as fout:
        for data in datas:
        #for data in fout: !!! 把传入的参数通过fout句柄柄  一行行写出
            fout.write("^_^".join(data)+'\n')#将列表元素用"^_^"连接
            
datas=read_file()
datas=sort_grades(datas)
print(datas)
write_file(datas)