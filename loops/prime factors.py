value=int(input())
org_val=value
prime = [x for x in range(2, value) if all(x % y != 0 for y in range(2, x))]
for i in prime:
    if value%i==0:
        print(i,end="--> ")
        count=0
        while (value%i)==0:
            value=value/i
            count+=1
        print(count)
if org_val==value:
    print(1,value)
