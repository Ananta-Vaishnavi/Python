# from collections import Counter
# l=[3, 3, 3, 4, 6, 6, 6, 7, 7, 8, 8]
# a=dict(Counter(l))
# for i,j in a.items():
#     if j%2!=0:
#         print(i)
l=[6,7,3,6,8,7,6,8,3,3]
l.sort()
for i in range(len(l)):
    if l[i]==l[i-1]:
        continue
    if l.count(l[i])%2!=0:
        print(l[i],end='')
