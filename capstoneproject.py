#propulsion system 
class propultion:
    def __init__(self, fuel:float, thrust:float, engine_type:str):
        self._fuel = fuel
        self.thrust = thrust
        self.engine_type = engine_type
    def consumed_fuel(self, amount:float):
        if self._fuel >= amount:
            self._fuel -= amount
            print(f"Remaining fuel is {self._fuel}in Kg")
        else:
            print("fuel depletted")
    def get_fuel(self) ->float:
        return self._fuel
    
    #navigation system

class navigation:
    def __init__(self):
        self.coordinates = (0.0,0.0,0.0)
        self.trajectory = []
    def update_position(self, velocity:tuple, time:float):
        dx = [0]*time
        dy = [1]*time
        dz = [2]*time
        self.coordinates = (
            self.coordinates [0] + dy,
            self.coordinates [1]+ dx,
            self.coordinates [2] + dx

        )
        self.trajectory.append(self.coordinates)
    
#communication system:

class communication:
    def __init__(self):
        self.messages = []
    def send_messages(self, message : str, destination :str):
        self.messages.append(f" sent to {destination}: '{message}'") 
        print(f"message sent to {destination}")
    def receive_message(self,message:str):
        self.messages.append(f"Received '{message}'")
        print(f"New message{message}")

class engine:
    def __init__(self, efficiecy:float):
        self.efficiecy = efficiecy
    def ignite(self):
        raise NotImplementedError("Subclasses must ignite ()")
    
class chemical_engine:
    def ignite(self):
        print("chemical engine ignited ")
class Ion_engine:
    def ignite(self):
        print("Ion engine activated ")

class space_craft:
    def __init__(self, name:str, fuel: float, thrust:float, engine_type:str):
        self.name = name
        self.propulsion = propultion(fuel,thrust,engine_type)
        self.navigation  = navigation()
        self.communication  = communication()
        self.engine = chemical_engine() if engine_type == "chemical" else Ion_engine(0.95)
    def launch(self):
        self.engine.ignite()
        print(f"{self.name} is launching.....")
    def simulate_movement(self, velocty:tuple, time:float):
        fuel_needed = time * self.propulsion.thrust
        if self.propulsion.get_fuel() >= fuel_needed:
            self.propulsion.consumed_fuel(fuel_needed)
            self.navigation.update_position(velocty, time)
            print(f"New position : {self.navigation.coordinates}")
        else:
            print("not enough fuel for maunevor")
falcon = space_craft("Falcon X", fuel=1000, thrust=500, engine_type="chemical")
falcon.launch()
falcon.simulate_movement((10,0,5),5)

falcon.communication.send_messages("Earth we are stable", "Earth")
falcon.communication.receive_message("Roger!, Falcon X Proecced",)

print("Trajectory:", falcon.navigation.trajectory)