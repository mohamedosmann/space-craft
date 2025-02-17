class Rocket:
    def __init__(self, name, fuel):
        self.name = name
        self._fuel = fuel
    def get_fuel(self):
        return self._fuel
    
    def set_fuel(self, amount):
        if amount >=0:
            self._fuel = amount
        else:
            print("Fuel canont be negative ")
    
rocket = Rocket("Saturn V", 500)
print(rocket.get_fuel())
rocket.set_fuel(-40)