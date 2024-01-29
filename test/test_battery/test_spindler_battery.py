import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-01-28")
        last_service_date = date.fromisoformat("2020-01-27")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-01-28")
        last_service_date = date.fromisoformat("2022-01-31")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())