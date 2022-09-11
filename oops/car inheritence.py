class Vehicle:
    def __init__(self,color,max_speed):
        self.color=color
        self.__max_speed=max_speed  #private members
        
    def get_max_speed(self):
        return self.__max_speed
        
    def set_max_speed(self):
        self.__max_speed = max_speed
        
class Car(Vehicle):    
    def __init__(self,color,max_speed,num_gears,isconvertible):
        super().__init__(color,max_speed)
        self.num_gears=num_gears
        self.isconvertible=isconvertible
        
    def printCar(self):
        print(self.color)
        print(self.get_max_speed())
        print(self.num_gears)
        print(self.isconvertible)
        
        
c=Car("blue",260,4,False)
c.printCar()
