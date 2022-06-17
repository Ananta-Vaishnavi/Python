from collections import Counter
l=[3, 3, 3, 4, 6, 6, 6, 7, 7, 8, 8]
dupl=[]
a=dict(Counter(l))
for i,j in a.items():
    if j>1:
        dupl.append(i)
print(dupl)
