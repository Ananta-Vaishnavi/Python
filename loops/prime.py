from math import sqrt
def PrimeNumber(n):
    if n==1:
        print('Neithe Prime nor a Composite number')
        return
    elif n%2==0:
        print('Not a Prime Number')
        return
    a=0
    for i in range(3,int(sqrt(n))+1,2):
        a=i
        if n%i==0:
            break
    if int(sqrt(n))%2==0 and a==int(sqrt(n))+1:
        print('Prime Number')
        return
    elif int(sqrt(n))%2!=0 and a==int(sqrt(n)):
        print('Prime Number')
        return
    else:
        print('Not a Prime Number')
        return
PrimeNumber(i)
