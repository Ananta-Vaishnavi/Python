n=int(input("Enter the number of digits "))
num=[None]*n
i=0
e=0
o=0
osum=0
esum=0
while i<n:
  num[i]=int(input())
  i+=1
i=0
while i<n:
  if(num[i]%2)==0 :
   esum+=num[i]
   e+=1
  else:
    osum+=num[i]
    o+=1
  i+=1
print("count of even= ",e)
print("count of odd= ",o)
print("sum of even number ",esum)
print("sum of odd number ",osum)
    
