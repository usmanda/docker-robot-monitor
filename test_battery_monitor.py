import unittest

from battery_monitor import battery_status


class TestBatteryStatus(unittest.TestCase):
    def test_ready(self):
        self.assertEqual(
            battery_status(75),
            ("Ready for a mission", "green"),
        )

    def test_low(self):
        self.assertEqual(
            battery_status(30),
            ("Plan to recharge soon", "yellow"),
        )

    def test_critical(self):
        self.assertEqual(
            battery_status(10),
            ("Return to charging station", "red"),
        )

    def test_boundaries(self):
        cases = [
            (0, ("Return to charging station", "red")),
            (19.9, ("Return to charging station", "red")),
            (20, ("Plan to recharge soon", "yellow")),
            (49.9, ("Plan to recharge soon", "yellow")),
            (50, ("Ready for a mission", "green")),
            (100, ("Ready for a mission", "green")),
        ]

        for level, expected in cases:
            with self.subTest(level=level):
                self.assertEqual(battery_status(level), expected)

    def test_invalid_readings(self):
        for level in [-5, 110, float("nan"), float("inf")]:
            with self.subTest(level=level):
                with self.assertRaises(ValueError):
                    battery_status(level)


if __name__ == "__main__":
    unittest.main()