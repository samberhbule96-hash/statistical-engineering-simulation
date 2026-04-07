import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    def test_central_tendency(self):
        engine = StatEngine([10, 20, 30, 40])
        self.assertEqual(engine.get_mean(), 25.0)
        self.assertEqual(engine.get_median(), 25.0)

    def test_bessel_correction(self):
        # For [10, 20], Pop Var = 25, Sample Var = 50
        engine = StatEngine([10, 20])
        self.assertEqual(engine.get_variance(is_sample=False), 25.0)
        self.assertEqual(engine.get_variance(is_sample=True), 50.0)

    def test_cleaning(self):
        engine = StatEngine([1, "2", None, 3])
        self.assertEqual(len(engine.data), 3)

if __name__ == "__main__":
    unittest.main()
