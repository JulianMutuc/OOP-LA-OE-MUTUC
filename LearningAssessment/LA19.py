
class FriedRice:
    def __init__(self, rice, egg, meat,garlic ,salt, msg):
        self.__rice = rice
        self.egg = egg
        self.meat = meat
        self.garlic = garlic
        self.salt = salt
        self.__msg = msg
    def __str__(self):
        return f"Ang sinangag ko ay may {self.__rice}, {self.egg}, {self.meat}, {self.garlic}, {self.salt}, {self.__msg}"

GarlicFriedRice = FriedRice("Kanin", "", "", "Bawang", "Asin", "MSG")
EggFriedRice = FriedRice("Kanin", "Itlog", "", "Bawang", "Asin", "MSG")
EggFriedRice2 = FriedRice("Kanin", "Itlog", "Karne", "Bawang", "Asin", "MSG")

print(GarlicFriedRice.__msg)
print(EggFriedRice.__msg)
print(EggFriedRice2.__msg)