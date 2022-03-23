n=int(input("Enter the number upto which you want odd numbers "))
i=1
sum=0
while i<n:
  if i%2!=0:
   print(i)
   sum+=i
  i+=1
  sum+=i
print(sum)
