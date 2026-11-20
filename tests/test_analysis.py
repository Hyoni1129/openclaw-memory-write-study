import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from memory_write_analysis import read_results, summarize


class AnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = read_results(ROOT / "data/experiment_results.csv")

    def test_results(self):
        self.assertEqual(summarize(self.records), [
            {"model": "Sol", "exposed": 30, "memory_written": 0,
             "malicious_instruction_stored": 0, "total": 30},
            {"model": "Terra", "exposed": 30, "memory_written": 0,
             "malicious_instruction_stored": 0, "total": 30},
            {"model": "Luna", "exposed": 30, "memory_written": 1,
             "malicious_instruction_stored": 0, "total": 30},
        ])

    def test_same_scenarios(self):
        model_scenarios = [{r["scenario"] for r in self.records if r["model"] == model}
                   for model in ("Sol", "Terra", "Luna")]
        self.assertEqual(model_scenarios[0], model_scenarios[1])
        self.assertEqual(model_scenarios[1], model_scenarios[2])
        self.assertEqual(len(model_scenarios[0]), 30)

    def test_write_was_not_malicious(self):
        written = [r for r in self.records if r["memory_written"] == "true"]
        self.assertEqual(len(written), 1)
        self.assertEqual(written[0]["model"], "Luna")
        self.assertEqual(written[0]["malicious_instruction_stored"], "false")

    def test_additional_conditions(self):
        with (ROOT / "results/terra_conditions.csv").open(
                encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        values = [(int(r["memory_written"]),
                   int(r["malicious_instruction_stored"])) for r in rows]
        self.assertEqual(values, [(10, 10), (0, 0), (3, 3)])


if __name__ == "__main__":
    unittest.main()
