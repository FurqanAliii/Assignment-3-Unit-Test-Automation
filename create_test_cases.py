from openpyxl import Workbook
from pathlib import Path

output = Path("docs/test_cases.xlsx")
output.parent.mkdir(parents=True, exist_ok=True)

rows = [
    ["TC ID", "Technique", "Input", "Expected Result", "Purpose"],
    ["TC01", "ECP", "2+3", "5", "Valid arithmetic"],
    ["TC02", "ECP", "10/2", "5", "Valid division"],
    ["TC03", "ECP", "sqrt(9)", "3", "Valid function"],
    ["TC04", "ECP", "unknown_name", "ValueError", "Invalid identifier"],
    ["TC05", "ECP", "2 > 1", "ValueError", "Unsupported expression"],
    ["TC06", "BVA", "sqrt(0)", "0", "Square root boundary"],
    ["TC07", "BVA", "sqrt(1)", "1", "Positive boundary"],
    ["TC08", "BVA", "sqrt(-1)", "ValueError", "Negative square root"],
    ["TC09", "BVA", "10/0", "ZeroDivisionError", "Division by zero"],
    ["TC10", "BVA", "0/5", "0", "Zero numerator"],
    ["TC11", "BVA", "1/1000", "0.001", "Small positive result"],
]

wb = Workbook()
ws = wb.active
ws.title = "Test Cases"

for row in rows:
    ws.append(row)

ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions

for column in ws.columns:
    width = max(len(str(cell.value or "")) for cell in column) + 3
    ws.column_dimensions[column[0].column_letter].width = width

wb.save(output)
print(f"Excel file created: {output.resolve()}")
