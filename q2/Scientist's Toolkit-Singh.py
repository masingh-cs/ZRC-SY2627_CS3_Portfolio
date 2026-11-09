from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return 7.2

class TempSensor(Sensor):
    def get_reading(self):
        return 24.5

print("--- Lab Inventory System ---")
print(f"[pH Sensor] Sensor Reading: {PHSensor().get_reading()}")
print(f"[temperature] Sensor Reading: {TempSensor().get_reading()}°C")
print("----------------------------")
#my_sensor = Sensor()