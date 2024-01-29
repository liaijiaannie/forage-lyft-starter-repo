from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    def create_calliope(last_service_date, current_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_glissade(last_service_date, current_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_palindrome(last_service_date, current_date, warning_light_is_on):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(warning_light_is_on)
        return Car(engine, battery)
    
    def create_rorschach(last_service_date, current_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    
    def create_thovex(last_service_date, current_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(engine, battery)
    

