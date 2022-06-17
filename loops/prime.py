from math import sqrt
def PrimeNumber(n):
    if n==2 or n==3:
        return True
    
    if n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    else:
        return True
for i in range(1,10):
    print(i)    
    print(PrimeNumber(i))
