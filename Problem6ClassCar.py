class car:

    def __init__(self, model, year, color, car_type, manufacturer):        
        self.model = model 
        self.year = year
        self.color = color
        self.car_type= car_type
        self.manufacturer = manufacturer

    def get_model(self): #<- method
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_car_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + str(self.car_type) + ' ' + str(self.manufacturer)

car1 = car("Sports", 2012, "Blue", "Corvette", "Chevrolet") #<- attributes for car
car2 = car("Sedan", 2020, "Black", "Civic", "Honda")

print(car1.get_color())
print(car1.get_model())
print(car1.get_car_type())
print(car1.get_manufacturer())
print(car2.get_color())
print(car2.get_car_type())
print(car2.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())


#Victor Moreno
#2/27/24

#Add two additional attributes and methods of ‘type’ and ‘manufacturer'
