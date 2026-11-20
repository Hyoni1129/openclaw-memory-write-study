"""Summarize the web-instruction memory-write experiment."""
import argparse
import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from memory_write_analysis import read_results, summarize


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Compare the calculated totals with the paper's results")
    args = parser.parse_args()
    summary = summarize(read_results(ROOT / "data/experiment_results.csv"))

    if args.check:
        with (ROOT / "results/model_results.csv").open(
                encoding="utf-8", newline="") as stream:
            reported = list(csv.DictReader(stream))
        calculated = [{key: str(value) for key, value in row.items()}
                      for row in summary]
        if calculated != reported:
            raise SystemExit("Reported totals do not match the experimental data")

    print(f"{'Model':<8}{'Exposed':>12}{'Memory write':>16}{'Malicious saved':>18}")
    for row in summary:
        total = row["total"]
        print(f"{row['model']:<8}{str(row['exposed'])+'/'+str(total):>12}"
              f"{str(row['memory_written'])+'/'+str(total):>16}"
              f"{str(row['malicious_instruction_stored'])+'/'+str(total):>18}")


if __name__ == "__main__":
    main()
