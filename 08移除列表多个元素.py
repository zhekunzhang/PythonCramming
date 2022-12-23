list_or=[2,5,6,7,9,11,13]
list_todel=[2,9,11]


def removelist(orilist,dellist):
    for item in dellist:
        orilist.remove(item)

removelist(list_or,list_todel)
print(list_or)