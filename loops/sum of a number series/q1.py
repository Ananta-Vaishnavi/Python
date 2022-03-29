#1+1/2+1/3+.......+1/n
n=int(input("Enter a number "))
i=1
s=0
while i<=n:
  s+=1/i
  i+=1
print(s)
