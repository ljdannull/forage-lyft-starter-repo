from abc import ABC, abstractmethod
from car.serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()