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
        self.assertTrue(0 <= m['otif_rate'] <= 1)




class TestBusinessRules(unittest.TestCase):
    def test_blocked_and_partial_orders_fail_otif(self):
        from run import enrich
        rows = [dict(order_id='A', warehouse='Germany', ordered_units=10, available_units=10, blocked=True, delivery_delay_days=-1, fulfilled_units=0), dict(order_id='B', warehouse='Germany', ordered_units=10, available_units=6, blocked=False, delivery_delay_days=-1, fulfilled_units=6)]
        m = metrics(rows)
        self.assertEqual(m['fill_rate'], 0.6)
        self.assertEqual(m['otif_rate'], 0)
        enriched = enrich(rows)
        self.assertEqual(enriched[0]['status'], 'Blocked')
        self.assertEqual(enriched[1]['shortage_units'], 4)
    def test_empty_metrics(self):
        self.assertEqual(metrics([])['fill_rate'], 0)
        self.assertEqual(metrics([])['otif_rate'], 0)
    def test_invalid_count(self):
        with self.assertRaises(ValueError):
            simulate(-1)
    def test_invariants(self):
        for row in simulate():
            self.assertLessEqual(row['fulfilled_units'], min(row['ordered_units'], row['available_units']))
            if row['blocked']:
                self.assertEqual(row['fulfilled_units'], 0)
    def test_build_is_reproducible(self):
        import tempfile
        import json
        import csv
        from run import build
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            result = build(output, 30)
            original = {p.name: p.read_bytes() for p in output.iterdir()}
            self.assertEqual(result, json.loads((output/'kpis.json').read_text()))
            with (output/'orders.csv').open() as f:
                self.assertEqual(len(list(csv.DictReader(f))), 30)
            build(output, 30)
            self.assertEqual(original, {p.name: p.read_bytes() for p in output.iterdir()})

if __name__ == '__main__':
    unittest.main()
