import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import unittest
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [1, 2, 3, 4]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [2, 2, 2.9, 2]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())