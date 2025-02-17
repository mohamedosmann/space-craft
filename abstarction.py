from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read_data(self):
        pass

class TempratureSensor(Sensor):
    def read_data(self):
        return " 25*C"

temp_sensor = TempratureSensor()
print(f"the temprature is {temp_sensor.read_data()}")