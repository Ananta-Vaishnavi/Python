num=int(input("Enter number "))
per=1
for i in range(2,num-1):
  if (num%i==0):
    per+=i
if per==num:
  print("Perfect")
else:
  print("Not Perfect")
