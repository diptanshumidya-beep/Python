class Vhicle:

    def __init__(self, company, engine_type):
        self.company = company
        self.engine_type = engine_type

    def prrrint(self):
        print("Company:", self.company)
        print("Engine type:", self.engine_type)


class Kid(Vhicle):

    def __init__(self, mileage, speed, colour, company, engine_type):
       

       
        self.mileage = mileage
        self.speed = speed
        self.colour = colour
        super().__init__(company, engine_type)

    def print_details(self):
        print("Mileage:", self.mileage)
        print("Speed:", self.speed)
        print("Colour:", self.colour)
        print("ENGINE TYPE", self.engine_type)
        print("company", self.company)
        
       
        super().prrrint()


parent = Vhicle("Volkswagen", "V12")
parent.prrrint()

print()

child = Kid(
    150,
    300,
    "Orange",
    "Volkswagen",
    "V12")
    

child.print_details()

print()
print("Is Kid a subclass of Vehicle?", issubclass(Kid, Vhicle))