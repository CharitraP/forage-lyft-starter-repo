from .tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        total_tire_wear=0
        for tire in self.tire_wear:
            total_tire_wear+=tire
            if total_tire_wear>=3.0:
                return True
        return False