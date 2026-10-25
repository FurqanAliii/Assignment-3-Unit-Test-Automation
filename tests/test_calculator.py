import math
import pytest
from Calculator import SafeEvaluator


def test_basic_arithmetic():
    ev = SafeEvaluator()
    assert ev.evaluate("2+3*4") == 14
    assert ev.evaluate("(1+2)*3") == 9


def test_power_and_mod():
    ev = SafeEvaluator()
    assert ev.evaluate("2^3") == 8
    assert ev.evaluate("10%3") == 1


def test_trig_degrees():
    ev = SafeEvaluator()
    assert math.isclose(ev.evaluate("sin(30)"), 0.5, rel_tol=1e-9)
    assert math.isclose(ev.evaluate("cos(60)"), 0.5, rel_tol=1e-9)
    assert math.isclose(ev.evaluate("tan(45)"), 1.0, rel_tol=1e-9)


def test_constants_and_functions():
    ev = SafeEvaluator()
    assert math.isclose(ev.evaluate("pi"), math.pi, rel_tol=1e-12)
    assert math.isclose(ev.evaluate("sqrt(9)"), 3.0, rel_tol=1e-12)
    assert math.isclose(ev.evaluate("log(e)"), 1.0, rel_tol=1e-9)


def test_invalid_identifier_raises():
    ev = SafeEvaluator()
    with pytest.raises(ValueError):
        ev.evaluate("unknown_name")

@pytest.mark.parametrize("expression, expected", [
    ("2+3", 5),
    ("10-4", 6),
    ("3*4", 12),
    ("10/2", 5),
    ("2^3", 8),
    ("10%3", 1),
    ("-5+2", -3),
    ("sqrt(0)", 0),
    ("sqrt(1)", 1),
])
def test_valid_expression_partitions(expression, expected):
    evaluator = SafeEvaluator()
    assert evaluator.evaluate(expression) == expected

@pytest.mark.parametrize("expression", [
    "unknown_name",
    "2 > 1",
    "'hello'",
])
def test_invalid_expression_partitions(expression):
    evaluator = SafeEvaluator()
    with pytest.raises((ValueError, TypeError)):
        evaluator.evaluate(expression)