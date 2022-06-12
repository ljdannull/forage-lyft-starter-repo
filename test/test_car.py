import unittest
from datetime import datetime

from car.car_factory import CarFactory

fac = CarFactory()
current_date = datetime.today().date()
wear = [0,0,0,0]

class TestCalliope(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        warning_light_is_on = False

        car = fac.create_palindrome(current_date, last_service_date, warning_light_is_on, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        print(today, last_service_date)
        warning_light_is_on = False

        car = fac.create_palindrome(current_date, last_service_date, warning_light_is_on, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = fac.create_palindrome(current_date, last_service_date, warning_light_is_on, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = fac.create_palindrome(current_date, last_service_date, warning_light_is_on, wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = fac.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = fac.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = fac.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = fac.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = fac.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wear)
        self.assertFalse(car.needs_service())

class TestTires(unittest.TestCase):
    
    def test_octo_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        new_wear = [0.5, 0.5, 0.5, 0.5]
        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, new_wear)
        self.assertFalse(car.needs_service())
    
    def test_octo_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        new_wear = [1, 1, 0.5, 0.5]
        car = fac.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, new_wear)
        self.assertTrue(car.needs_service())
    
    def test_carrigan_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        new_wear = [0.2, 0.2, 0.2, 0.2]
        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, new_wear)
        self.assertFalse(car.needs_service())

    def test_carrigan_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        new_wear = [0.2, 0.2, 0.2, 0.9]
        car = fac.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, new_wear)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()
