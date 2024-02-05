#Create superclass vehicle
class Vehicle:
    def __init__(self, vehicletype):
        self.vehicletype = vehicletype
#create subclass automobile
class Automobile(Vehicle):
    def __init__(self, vehicletype, year, make, model, doors, roof):
        super().__init__(vehicletype)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#make function to print all the info
def printinfo():
    print(f"Vehicle Type: {vehicletype}\nYear: {year}\nMake: {make}\nModel: {model}\nNumber of doors: {doors}\nRoof Type: {roof}")
#inputting the  info
vehicletype = input("What is your type of transportation? ")
year = input("What year was it made? ")
make = input("Who made it? ")
model = input("And the model? ")
doors = input("How many doors does it have? ")
roof = input("Regular Roof, Sun-roof, or none..?" )
#run function
printinfo()