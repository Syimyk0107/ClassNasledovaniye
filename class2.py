# class Laptops:
#     def __init__(self, brand, model, color, year, weight, price, inch):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.price = price
#         self.weight = weight
#         self.year = year
#         self.inch = inch

#     def start_the_made(self):
#         print(f"Computer {self.brand} {self.model} {self.color} {self.year} {self.weight} made.")

#     def start_the_sale(self):
#         print(f"Computer {self.brand} {self.model} {self.color} {self.year} {self.weight} on sale.")


# class Windows(Laptops):
#     def ssd(self):
#         print(f"Laptop {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Normal price inch {self.inch}")

#     def inch_info(self):
#         # print(f"The screen size of this Windows laptop is {self.inch} inches.")
#           return f"The screen size of this Linux laptop is {self.inch} inches."


# class Ios(Laptops):
#     def m3(self):
#         print(f"Macbook {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Expensive price inch {self.inch}")

#     def inch_info(self):
#         # print(f"The screen size of this Macbook is {self.inch} inches.")
#         return f"The screen size of this Linux laptop is {self.inch} inches."

# class Linux(Laptops):
#     def ux(self):
#         print(f"Computer {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Cheap price inch {self.inch}")

#     def inch_info(self):
#         # print(f"The screen size of this Linux laptop is {self.inch} inches.")
#         return f"The screen size of this Linux laptop is {self.inch} inches."


# # Создание объектов и вызов методов
# win_laptop = Windows("HP", "Pavilion", "Gray", 2025, "1.3kg", "1600$", "16.5")
# win_laptop.start_the_made()
# win_laptop.start_the_sale()
# win_laptop.ssd()
# win_laptop.inch_info()

# ios_laptop = Ios("MacOs", "M3", "White", 2024, "900g", "2500$", "13.5")
# ios_laptop.start_the_made()
# ios_laptop.start_the_sale()
# ios_laptop.m3()
# ios_laptop.inch_info()

# linux_laptop = Linux("Acer", "Aspire", "Black", 2018, "1.5kg", "1200$", "14")
# linux_laptop.start_the_made()
# linux_laptop.start_the_sale()
# linux_laptop.ux()
# linux_laptop.inch_info()

class Laptops:
    def __init__(self, brand, model, color, year, weight, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.weight = weight
        self.year = year

    def start_the_made(self):
        print(f"Computer {self.brand} {self.model} {self.color} {self.year} {self.weight} made.")

    def start_the_sale(self):
        print(f"Computer {self.brand} {self.model} {self.color} {self.year} {self.weight} on sale.")


class Windows(Laptops):
    def __init__(self, brand, model, color, year, weight, price, inch):
        super().__init__(brand, model, color, year, weight, price)
        self.inch = inch

    def ssd(self):
        print(f"Laptop {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Normal price inch {self.inch}")

    def inch_info(self):
        return f"The screen size of this Windows laptop is {self.inch} inches."


class Ios(Laptops):
    def __init__(self, brand, model, color, year, weight, price, inch):
        super().__init__(brand, model, color, year, weight, price)
        self.inch = inch

    def m3(self):
        print(f"Macbook {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Expensive price inch {self.inch}")

    def inch_info(self):
        return f"The screen size of this Macbook is {self.inch} inches."


class Linux(Laptops):
    def __init__(self, brand, model, color, year, weight, price, inch):
        super().__init__(brand, model, color, year, weight, price)
        self.inch = inch

    def ux(self):
        print(f"Computer {self.brand} {self.model} Color: {self.color} Year: {self.year} Weight: {self.weight} made. Price: {self.price}--Cheap price inch {self.inch}")

    def inch_info(self):
        return f"The screen size of this Linux laptop is {self.inch} inches."


# Создание объектов и вызов методов
win_laptop = Windows("HP", "Pavilion", "Gray", 2025, "1.3kg", "1600$", "16.5")
win_laptop.start_the_made()
win_laptop.start_the_sale()
win_laptop.ssd()
# print(win_laptop.inch_info())

ios_laptop = Ios("MacOs", "M3", "White", 2024, "900g", "2500$", "13.5")
ios_laptop.start_the_made()
ios_laptop.start_the_sale()
ios_laptop.m3()
# print(ios_laptop.inch_info())

linux_laptop = Linux("Acer", "Aspire", "Black", 2018, "1.5kg", "1200$", "14")
linux_laptop.start_the_made()
linux_laptop.start_the_sale()
linux_laptop.ux()
# print(linux_laptop.inch_info())
