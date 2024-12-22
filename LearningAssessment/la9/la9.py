class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):  
        return f"{self.brand} is a car object"

car = Car("Ferrari")
print(car) 
del car

try:
    print(car)
except NameError:
    print("The car object has been deleted and no longer exists.")
