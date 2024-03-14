# Your code here...
class Vehicle:
    def __init__(self):
        self.price = 0
        self.category = ''
    
    def __repr__(self):
        return "category:" + self.category + ",price:" + str(self.price)
    
        
class Car(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.category = 'car'

class boat(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.category = 'boat'
        
        
class Truck(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 40000
        
class pickup_truck(Truck):
    
    def __init__(self):
        super().__init__() 
        self.price = 35000


class Nissan_Frontier(pickup_truck):
    
    def __init__(self):
        super().__init__() 
        self.price = 28000


class semi_truck(Truck):
    
    def __init__(self):
        super().__init__() 
        self.price = 150000

class kenworth_t880(semi_truck):
    
    def __init__(self):
        super().__init__() 
        self.price = 180000




class sports_car(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 70000

class suv(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 32000
        

class sedan(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 23000


class sedan(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 23000

class coupe(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 24000

class van(Car):
    
    def __init__(self):
        super().__init__() 
        self.price = 32000
