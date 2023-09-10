import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestEngine(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.3,0.4,0.5,0.9]
        tire = CarriganTires(tire_wear)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_true(self):
        tire_wear = [0.9,0.8,0.5,0.9]
        tire = OctoprimeTires(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3,0.4,0.5,0.5]
        tire = CarriganTires(tire_wear)
        self.assertFalse(tire.needs_service())
    
    def test_needs_service_false(self):
        tire_wear = [0.4,0.4,0.5,0.3]
        tire = OctoprimeTires(tire_wear)
        self.assertFalse(tire.needs_service())