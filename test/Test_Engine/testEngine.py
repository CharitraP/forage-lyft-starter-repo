import unittest

from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine


class TestEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 98767
        last_service_mileage = 544
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
    
    def test_needs_service_true(self):
        current_mileage = 77676
        last_service_mileage = 766
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 24576
        last_service_mileage = 34
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
        
    def test_needs_service_false(self):
        current_mileage = 55564
        last_service_mileage = 667
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())