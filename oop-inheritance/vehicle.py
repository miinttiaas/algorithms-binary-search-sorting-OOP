class Vehicle:
    def __init__(self,make,model,year,weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def start_engine(self):
        print("The engine is started")

class Car(Vehicle):
    def __init__(self,make,model,year,weight,num_doors,num_passengers):
        super().__init__(make,model,year,weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def start_engine(self):
        print("The car`s engine is started")
    def drive(self):
        print(f"{self.model} is being driven")

class Truck(Vehicle):
    def __init__(self,make,model,year,weight,cargo_capacity,towing_capacity):
        super().__init__(make,model,year,weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def start_engine(self):
        print( "The truck's engine is starting")

    def haul(self):
        print("The truck is hauling cargo.")

class Motorcycle(Vehicle):
    def __init__(self,make,model,year,weight,num_wheels,has_sidecar="no"):
        super().__init__(make,model,year,weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def start_engine(self):
        print( "The motorcycle's engine is starting")
    def ride(self):
        print("The motorcycle is riding.")

# vehicle1 = Vehicle("Ferrari","Roma","1945","100kg")
# car1 = Car("Toyota", "Camry", 2020, 1500, 4, 5)
# truck1 = Truck("Ford", "F-150", 2022, 2500, 2000, 10000)
# motorcycle1 = Motorcycle("Honda", "CBR500R", 2021, 200, 2)
# vehicle1.start_engine()
# car1.start_engine()
# car1.drive()
# truck1.start_engine()
# truck1.haul()
# motorcycle1.start_engine()
# motorcycle1.ride()
