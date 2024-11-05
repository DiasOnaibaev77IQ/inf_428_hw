import unittest

def time_difference(hour1: int, hour2: int) -> int:
    if hour2 - hour1 < 0:
        return 24 + (hour2 - hour1)
    return hour2 - hour1

class TestTimeDifference(unittest.TestCase):

    def test_same_time(self):
        self.assertEqual(time_difference(16, 16), 0)

    def test_adjacent_hours(self):
        self.assertEqual(time_difference(10, 11), 1)

    def test_wraparound_difference(self):
        self.assertEqual(time_difference(23, 1), 2)

    def test_half_day_difference(self):
        self.assertEqual(time_difference(0, 12), 12)

    def test_near_wraparound_difference(self):
        self.assertEqual(time_difference(22, 2), 4)

    def test_noon_to_midnight(self):
        self.assertEqual(time_difference(12, 0), 12)

    def test_minute_precision(self):
        self.assertAlmostEqual(time_difference(23.5, 0.5), 1)

if __name__ == '__main__':
    unittest.main()