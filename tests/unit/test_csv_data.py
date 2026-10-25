import csv
from pathlib import Path

import pytest
from Calculator import SafeEvaluator


CSV_FILE = (
    Path(__file__).resolve().parents[2]
    / "test_data"
    / "calculator_cases.csv"
)


def load_test_cases():
    with CSV_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize("case", load_test_cases())
def test_calculator_from_csv(case):
    evaluator = SafeEvaluator()

    expression = case["expression"]
    expected = float(case["expected"])
    actual = evaluator.evaluate(expression)

    assert actual == expected
