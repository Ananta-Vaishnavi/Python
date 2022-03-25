num=[None]*10
i=0
sum=0
while i<10:
  num[i]=int(input())
  i+=1
i=0
while i<10:
  sum+=num[i]
  i+=1
print("sum= ",sum)
print("average= ",sum/10)
