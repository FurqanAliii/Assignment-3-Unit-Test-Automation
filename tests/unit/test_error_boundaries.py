import pytest
from Calculator import SafeEvaluator


@pytest.mark.order(1)
@pytest.mark.invalid
def test_negative_square_root():
    evaluator = SafeEvaluator()
    with pytest.raises(ValueError):
        evaluator.evaluate("sqrt(-1)")


@pytest.mark.order(2)
@pytest.mark.invalid
def test_division_by_zero():
    evaluator = SafeEvaluator()
    with pytest.raises(ZeroDivisionError):
        evaluator.evaluate("10/0")


@pytest.mark.order(3)
@pytest.mark.smoke
def test_zero_numerator():
    evaluator = SafeEvaluator()
    assert evaluator.evaluate("0/5") == 0


@pytest.mark.order(4)
@pytest.mark.smoke
def test_small_positive_result():
    evaluator = SafeEvaluator()
    assert evaluator.evaluate("1/1000") == 0.001