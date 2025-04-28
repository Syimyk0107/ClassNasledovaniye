#Class 
# class Dog:
#     def __init__(self, name, age, year):
#         self.name = name
#         self.age = age
#         self.year = year

#     def bark(self):
#         return f"name: {self.name}, age: {self.age} , {self.year} Woof!"

# my_dog = Dog("Buddy", 3, 2022) 
# print(my_dog.bark())   

#---------------------------------
#--------Nasledovaniye------------------
# class Cars:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def start_the_engine(self):
#         print(f"Двигатель автомобиля {self.brand} {self.model} запущен.")
#     def stop_the_engine(self):
#         print(f"Двигатель автомобиля {self.brand} {self.model} остановлен.")
    
# class ElectroCar(Cars):
#     def charge(self):
#         print(f"Электромобиль {self.brand} {self.model} заряжается.")

# ## Make object for the class Cars

# cars = Cars("Toyota", "Camry", 2025)
# cars.start_the_engine()
# cars.stop_the_engine()

# ## Make object for the class ElectroCars
# electro_car = ElectroCar("Tesla", "Model S", 2024)
# electro_car.start_the_engine()
# electro_car.stop_the_engine()
# electro_car.charge()
#--------------------------------------------------------------------------------------------------

class Laptops:
    def __init__(self, brand, model, color, year, weight, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.weight = weight
        self.year = year


    def start_the_made(self):
        print(f"Computer {self.brand} {self.model} {self.color}  {self.year} {self.weight} made.")
    def start_the_sale(self):
        print(f"Computer {self.brand} {self.model} {self.color}  {self.year} {self.weight} on sale.")
    
class Windows(Laptops):
    def ssd(self):
        print(f"Laptop {self.brand} {self.model} Color: {self.color}  Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Normal price")

class Ios(Laptops):
    def m3(self):
        print(f"Macbook {self.brand} {self.model} Color: {self.color}  Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Expensive price")

class Linux(Laptops):
    def ux(self):
        print(f"Computer {self.brand} {self.model} Color: {self.color}  Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Cheap price")

# ## Make object for the class Laptops

# lap_types = Laptops("Mi", "Re", "Red", 2025, "1.2kg", "1600$")
# lap_types.start_the_made()
# lap_types.start_the_sale()

## Make object for the class Windows
win_laptop = Windows("HP", "Pavilion", "Gray", 2025, "1.3kg", "1600$")
win_laptop.start_the_made()
win_laptop.start_the_sale()
win_laptop.ssd()

## Make object for the class Ios
ios_laptop = Ios("MacOs", "M3", "White", 2024, "900g", "2500$")
ios_laptop.start_the_made()
ios_laptop.start_the_sale()
ios_laptop.m3()

## Make object for the class Linux
win_laptop = Linux("Acer", "Aspire","Black", 2018,"1.5kg", "1200$")
win_laptop.start_the_made()
win_laptop.start_the_sale()
win_laptop.ux()
