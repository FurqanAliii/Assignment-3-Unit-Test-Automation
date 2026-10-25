
# PyCalculator - Automated Testing Guide

## 1. Project Overview
PyCalculator is an existing Python scientific calculator project.
Automated tests focus on the SafeEvaluator functionality in Calculator.py.

## 2. Environment Setup
Use Python 3 and a virtual environment.

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install pytest-xdist pytest-order openpyxl