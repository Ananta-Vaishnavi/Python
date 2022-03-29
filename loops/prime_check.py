n=int(input("Enter a number  "))
c=2
for i in range(2,n-1):
  if n%i==0:
    break
  else:
   c+=1
if c==n-1:
  print("Prime")
else:
  print("Not Prime")
