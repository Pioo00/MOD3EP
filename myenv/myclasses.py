import datetime

class Supplier:
    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country
        self.createdAt = datetime.datetime.now()
        #https://www.geeksforgeeks.org/python/python-datetime-module/

    def getName(self):
        return self.name
    
    def __str__(self):
        format = str(self.name) + " - " + str(self.city) + ", " + str(self.country) + " created at: " + str(self.createdAt)
        print(format)

class WaterBottle:
    def __init__(self, sku, brand, cost, size, mouthSize, color, suppliedBy, qty):
        self.sku = sku
        self.brand = brand
        self.cost = f"{cost:.2f}" #string na sha
        self.size = size
        self.mouthSize = mouthSize
        self.color = color
        self.suppliedBy = suppliedBy
        self.qty = qty
        