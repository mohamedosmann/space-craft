
class Rocket:
    def __init__(self, name, fuel):
        self.name = name
        self._fuel = fuel

class Drone:
    def __init__(self, name, fuel):
        self.name = name

    def launch(self):
        print(f"{self.name} is launching off vertically")
    
def start_launch(vehicle):
        vehicle.launch()
    

    
falcon = Rocket("Falcon ", 100)
drone  = Drone("Startlink Drone")

start_launch(falcon)
start_launch(drone)