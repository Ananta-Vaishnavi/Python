num=input("Enter number ")
dig=len(num)
i=0
j=1
st=0
f=1
while i!=dig:
  a=int(num[i])
  while j<=a:
    f=f*j
    j+=1
  st+=f
  i+=1
if st==int(num):
  print("Strong")
else:
  print("Not Strong")
