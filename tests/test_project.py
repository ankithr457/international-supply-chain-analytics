import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from run import simulate, metrics

class TestSupplyChain(unittest.TestCase):
    def test_reproducible(self):
        self.assertEqual(simulate(20), simulate(20))
    def test_valid_metrics(self):
        m = metrics(simulate())
        self.assertEqual(m['orders'], 1200)
        self.assertTrue(0 <= m['fill_rate'] <= 1)
        self.assertTrue(0 <= m['on_time_rate'] <= 1)

if __name__ == '__main__': unittest.main()
