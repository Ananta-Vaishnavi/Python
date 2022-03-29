# 1+x+x^2+x^3.......x^n
n=int(input("Enter a n up to which the series should continue "))
x=int(input("Enter a number"))
i=1
s=1
while i<n:
  s+=x**i
  i+=1
print(s)
