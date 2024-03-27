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
        self.category = 'Car'

class Boat(Vehicle):
    
    def __init__(self):
        Vehicle.__init__(self)
        self.category = 'Boat'
        
class Fishing_Vessel(Boat):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 200000

class Motor_Yacht(Boat):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 10000000

class Sailboat(Boat):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 700000

class Barge(Boat):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 50000

class m3_Self_Propelled_Split_Hopper_Barge(Barge):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 3200000

class Cargo_Ship(Boat):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 1200000

class MSC_Irina(Cargo_Ship):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 15000000

class Truck(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 40000

class Truck_SUV(Truck):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 80000

class Ford_Bronco_Raptor(Truck_SUV):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 80000
        
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

class  Mclaren_f1(Exotic_Car):
    
    def __init__(self):
        Exotic_Car.__init__(self) 
        self.price = 20000000

class SUV(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 32000
        
class Hyundai_Kona(SUV):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 25625

class Hatchback(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 23000

class Mazda_3(Hatchback):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 25335

class Sedan(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 23000

class Honda_Civic(Sedan):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 23000

class Honda_Civic_2024(Honda_Civic):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 25000

class Coupe(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 24000
        
class Audi_A5(Coupe):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 40000

class van(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 32000

class Luxury_Car(Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 60000

class Rolls_Royce_Phantom_2024(Luxury_Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 505750

class Bentley_Flying_Spur(Luxury_Car):
    
    def __init__(self):
        Car.__init__(self) 
        self.price = 217625
