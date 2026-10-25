# Test Design – PyCalculator

## Project
Original open-source project: PyCalculator
Main class: SafeEvaluator
Test framework: pytest

## 1. Equivalence Class Partitioning (ECP)

| Partition | Example input | Expected result |
|---|---|---|
| Valid arithmetic | 2+3 | 5 |
| Valid division | 10/2 | 5 |
| Valid power | 2^3 | 8 |
| Valid scientific function | sqrt(9) | 3 |
| Valid constant | pi | Mathematical pi |
| Unknown identifier | unknown_name | ValueError |
| Unsupported expression | 2 > 1 | ValueError |
| Invalid string constant | 'hello' | ValueError |

## 2. Boundary Value Analysis (BVA)

| Boundary case | Input | Expected result |
|---|---|---|
| Square root at zero | sqrt(0) | 0 |
| Square root at lower valid boundary | sqrt(1) | 1 |
| Negative square root | sqrt(-1) | ValueError |
| Division by zero | 10/0 | ZeroDivisionError |
| Zero numerator | 0/5 | 0 |
| Small positive value | 1/1000 | 0.001 |

## 3. Notes

- ECP groups inputs into valid and invalid categories.
- BVA checks values at or near meaningful boundaries.
- Division by zero is tested as an exception.
- The current evaluator does not explicitly validate expression length or numeric ranges.
