class complexNumbers:
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary
    
    def printcomplex(self):
        if self.imaginary==0 and self.real==0:
            print(0)
            
        elif self.imaginary==0:
            print(self.real)
            
        elif self.real==0:
            print(self.imaginary,'i')
            
        else:
            print(self.real,'+',self.imaginary,'i')
    
    def conjugate(self):
        self.imaginary=-(self.imaginary)
        self.printcomplex()
        
    def add(self,other):
        newReal=self.real+other.real
        newImaginary=self.imaginary+other.imaginary
        self.real=newReal
        self.imaginary=newImaginary
        self.printcomplex()
        
    def multiply(self,other):
        newReal=(self.real*other.real)-(self.imaginary*other.imaginary)
        newImaginary=(self.real*other.imaginary)+(self.imaginary*other.real)
        self.real=newReal
        self.imaginary=newImaginary
        self.printcomplex()
        
c1=complexNumbers(3,2)
c1.conjugate()
c2=complexNumbers(5,-4)
c1.multiply(c2)
