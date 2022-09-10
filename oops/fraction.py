def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
        
def lcm(a,b):
    return (a*b)//hcf(a,b)
class Fraction:
    def __init__(self,num=0,den=1):
        self.num=num
        self.den=den
    
    def simplify(self):
        gcd=hcf(self.num,self.den)
        self.num=self.num//gcd
        self.den=self.den//gcd
        
    def printfrac(self):
        if self.num==0 or self.den==1:
            print(self.num)
        else:
            print(self.num,'/',self.den)
            
    def printdeci(self):
        print(self.num/self.den)
        
    def add(self,other):
       newNum=(self.num*other.den)+(self.den*other.num)
       newDen=self.den*other.den
       self.num=newNum
       self.den=newDen
       self.simplify()
       self.printfrac()
       
    def subtract(self,other):
       newNum=(self.num*other.den)-(self.den*other.num)
       newDen=self.den*other.den
       self.num=newNum
       self.den=newDen   
       self.simplify()
       self.printfrac()
       
    def multiply(self,other):
        newNum=self.num*other.num
        newDen=self.den*other.den
        self.num=newNum
        self.den=newDen   
        self.simplify()
        self.printfrac()
        
    def divide(self,other):
        newNum=self.num*other.den
        newDen=self.den*other.num
        self.num=newNum
        self.den=newDen   
        self.simplify()
        self.printfrac()
        
    def LCM(self,other):
        newNum=lcm(self.num,other.num)
        newDen=hcf(self.den,other.den)
        self.num=newNum
        self.den=newDen
        self.simplify()
        self.printfrac()
        
    def HCF(self,other):
        newNum=hcf(self.num,other.num)
        newDen=lcm(self.den,other.den)
        self.num=newNum
        self.den=newDen
        self.simplify()
        self.printfrac()
    
    
f=Fraction(2,5)
f2=Fraction(3,7)
f.LCM(f2)
f.HCF(f2)
