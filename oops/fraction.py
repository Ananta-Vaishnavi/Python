def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
class Fraction:
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den
    
    def printfrac(self):
        if self.num==0 or self.den==1:
            print(self.num)
        else:
            print(self.num,'/',self.den)
    def simplify(self):
        gcd=hcf(self.num,self.den)
        self.num=self.num//gcd
        self.den=self.den//gcd
f=Fraction(2,6)
f.simplify()
f.printfrac()
