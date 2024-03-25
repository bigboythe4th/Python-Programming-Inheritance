# Your code here...
class Vehicle:
    def __init__(self):
        self.price = 0
        self.category = ''
    
    def __repr__(self):
        return "category:" + self.category + ",price:" + str(self.price)
    
        
class Car(Vehicle):
    
    def __init__(self):
        Vehicle.__init__(self)
        self.category = 'car'

class boat(Vehicle):
    
    def __init__(self):
        Vehicle.__init__(self)
        self.category = 'boat'
        
        
class Truck(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 40000
        
class Pickup_Truck(Truck):
    
    def __init__(self):
        Truck.__init__(self) 
        self.price = 35000


class Nissan_Frontier(Pickup_Truck):
    
    def __init__(self):
        Pickup_Truck.__init__(self) 
        self.price = 28000


class Semi_Truck(Truck):
    
    def __init__(self):
        Truck.__init__(self) 
        self.price = 150000

class Kenworth_t880(Semi_Truck):
    
    def __init__(self):
        Semi_Truck.__init__(self) 
        self.price = 180000




class Sports_car(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 70000

class Exotic_Car(Sports_car):
    
    def __init__(self):
        Sports_car.__init__(self) 
        self.price = 500000

class mclaren_p1(Exotic_Car):
    
    def __init__(self):
        Exotic_Car.__init__(self) 
        self.price = 1500000

class  Ferrari_F8(Exotic_Car):
    
    def __init__(self):
        Exotic_Car.__init__(self) 
        self.price = 300000

class suv(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 32000
        

class Hatchback(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 23000


class sedan(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 23000

class coupe(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 24000

class van(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 32000
