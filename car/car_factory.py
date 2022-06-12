from car.car import Car
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory:
    
    def _get_car(self, last_service_date):
        return Car(last_service_date)
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, wear):
        car = self._get_car(last_service_date)
        car.engine = CapuletEngine(current_mileage, last_service_mileage)
        car.battery = SpindlerBattery(current_date, last_service_date)
        car.tires = CarriganTire(wear)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, wear):
        car = self._get_car(last_service_date)
        car.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car.battery = SpindlerBattery(current_date, last_service_date)
        car.tires = OctoprimeTire(wear)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on, wear):
        car = self._get_car(last_service_date)
        car.engine = SternmanEngine(warning_light_on)
        car.battery = SpindlerBattery(current_date, last_service_date)
        car.tires = OctoprimeTire(wear)
        return car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, wear):
        car = self._get_car(last_service_date)
        car.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car.battery = NubbinBattery(current_date, last_service_date)
        car.tires = OctoprimeTire(wear)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, wear):
        car = self._get_car(last_service_date)
        car.engine = CapuletEngine(current_mileage, last_service_mileage)
        car.battery = NubbinBattery(current_date, last_service_date)
        car.tires = OctoprimeTire(wear)
        return car