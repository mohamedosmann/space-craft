#OOP practice 

#basic class 
class rocket:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
    def launch(self):
        if self.fuel>0:
            print(f"{self.name} has been launched remaining fuel is {self.fuel}")
            self.fuel -=10
        else:
            print("out of fuel ")
        
class falcon9(rocket):
    def __init__(self, name, fuel, reusable_booster):
        super().__init__(name, fuel)
        self.reusable_booster = reusable_booster
    

    def land_booster(self):
        if self.reusable_booster:
            print("Booster is landing........")
        else:
            print("Booster cannot be reused.......")

falcon_heavy = falcon9("starship heavy", 1000, True)

falcon_heavy.launch()
falcon_heavy.land_booster