# Scientific Calculator

<div align="right">

[![CI](https://github.com/SagarBiswas-MultiHAT/PyCalculator/actions/workflows/python-ci.yml/badge.svg)](https://github.com/SagarBiswas-MultiHAT/PyCalculator/actions)
&nbsp;
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
&nbsp;
[![Tests](https://github.com/SagarBiswas-MultiHAT/PyCalculator/actions/workflows/python-ci.yml/badge.svg)](https://github.com/SagarBiswas-MultiHAT/PyCalculator/actions)
&nbsp;
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---
<br>

</div>



<div align=center>

![](https://imgur.com/KjvwdvN.png)

---
<br>

</div>

A modern, safe scientific calculator written in Python using Tkinter. The project includes a secure expression evaluator (trigonometric functions operate in degrees), a responsive GUI, unit tests, and a GitHub Actions CI workflow so tests run automatically on push and pull requests.

This repository is intentionally small and designed for learning, experimenting, and easy contribution.

## Key Features

- Safe expression evaluation using Python's AST (no raw `eval`).
- Trigonometric functions (`sin`, `cos`, `tan`) that work in degrees.
- Common math functions: `sqrt`, `log`, power (`^` -> `**`), modulo.
- Clean, responsive Tkinter GUI with keyboard support.
- Automated tests with `pytest` and a GitHub Actions workflow for CI.

## Built With

- Python 3.10+ (works on 3.10 and 3.11 in CI)
- Tkinter (standard library GUI toolkit)
- pytest (for running unit tests)

## Quick Start

Prerequisites

- Python 3.10 or newer installed.
- (Optional) Create and activate a virtual environment.

Run the GUI
```bash
python Calculator.py
```

### Dev

Install (optional development deps)

```bash
python -m pip install -r requirements-dev.txt
```

Run the GUI

```bash
python Calculator.py
```

The calculator window will open. Use the buttons or your keyboard to enter expressions. Trigonometric input expects degrees (e.g., `sin(30)` → 0.5).

Run tests

```bash
python -m pytest -q
```

## Tests Included

There are unit tests in `tests/test.py` that validate arithmetic, power/modulo, trigonometric conversions (degrees), constants, and function behavior. The test suite runs on GitHub Actions for every push and pull request.

## Project Structure

The project layout is simple and easy to navigate:

- `Calculator.py` — Main application source: GUI and `SafeEvaluator` class.
- `README.md` — This file: explanation, usage, and project structure.
- `requirements.txt` — Runtime dependencies (empty for stdlib-only project).
- `requirements-dev.txt` — Development dependencies (`pytest`).
- `tests/` — Automated tests (pytest).
- `.github/workflows/python-ci.yml` — GitHub Actions CI configuration.

Directory tree (top-level):

```
Scientific_Calculator/
├─ Calculator.py
├─ README.md
├─ requirements.txt
├─ requirements-dev.txt
├─ tests/
│  └─ test.py
└─ .github/
   └─ workflows/
      └─ python-ci.yml
```

## Design Notes & Safety

- The expression evaluator uses Python's `ast` module to parse and evaluate expressions with a whitelist of allowed operations, functions, and constants. This prevents arbitrary code execution.
- Trigonometric functions convert degrees to radians internally to match typical calculator UX.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feat/your-feature`).
3. Add tests for new behavior.
4. Open a pull request describing the change.

Please keep changes focused and add tests for new functionality.

## License

This project is provided under the MIT License. See `LICENSE` for details if present.

## Contact

If you have questions or suggestions, open an issue in the repository.

---

Thank you for trying out this small scientific calculator — it is designed to be easy to read, modify, and extend.

### README:

```markdown
# Scientific Calculator

This Python application is a scientific calculator built using Tkinter. It supports various mathematical operations, including basic arithmetic (addition, subtraction, multiplication, division), trigonometric functions (sin, cos, tan), square root, exponentiation, and more.

## Features:

- Basic arithmetic operations (+, -, \*, /)
- Trigonometric functions (sin, cos, tan) in radians
- Square root and exponentiation (^)
- Clear display (C) and backspace (⌫)
- Responsive grid layout

## Requirements:

- Python 3.x
- Tkinter (included with Python)

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

### Running the Script

To run the script, follow these steps:

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the following command:

   python3 scientific_calculator.py
```

### Example Usage:

1. **Basic Operations**: Enter the numbers and operations, and click "=" to evaluate.
2. **Trigonometric Functions**: Enter the angle in degrees, then click "sin", "cos", or "tan" to get the result.
3. **Square Root**: Click "sqrt" to compute the square root of the displayed number.
4. **Exponentiation**: Use "^" to compute powers.

### Example Output:

![](https://scontent.fdac178-1.fna.fbcdn.net/v/t39.30808-6/473619514_122136009782552158_767090033486993121_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=RvnAq2LPOw8Q7kNvgFVbaBm&_nc_zt=23&_nc_ht=scontent.fdac178-1.fna&_nc_gid=AcBfKUTTM7Cm2xx33xdoqKq&oh=00_AYALlDqMGtk3Atq1cFFqQ9OEvP1qpyQThr0KwH-r6n4iTw&oe=678EA0E4)

## Code Explanation

### Main Script

- **GUI Layout**: The calculator uses a responsive grid layout. Each button is assigned to a grid cell, and the buttons are dynamically created using a loop.
- **Operations**: The calculator supports basic arithmetic, trigonometric functions, square root, and exponentiation. The user input is evaluated dynamically using Python's `eval()` function.
- **Error Handling**: When an invalid operation is performed (e.g., dividing by zero or invalid input), the calculator displays "Error".

### Error Handling

- **Invalid Operations**: If the input is invalid (e.g., dividing by zero or using invalid characters), the calculator displays "Error".
- **Trigonometric Functions**: If the user enters an invalid value for trigonometric functions, the calculator catches the error and displays "Error".

## Contributing

Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. This license permits anyone to use, modify, and distribute the software with minimal restrictions, ensuring flexibility for open-source development. See the [LICENSE](LICENSE) file for details.

---

**Note**: This script is designed for educational purposes and personal use.
