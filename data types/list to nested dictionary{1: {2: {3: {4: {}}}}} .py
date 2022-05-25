# def list_nd(l):
#   d1= d=dict()
#   for i in l:
#     d[i]=dict()
#     d=d[i]
#   return d1
# print(list_nd([1,2,3,4]))
def key(list):
    if len(list) == 1:
        return {list[0]: {}}
    else:
        return {list[0]: key(list[1:])}


print(key([1, 2, 3, 4]))
    
