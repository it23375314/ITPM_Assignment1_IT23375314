import openpyxl
wb = openpyxl.load_workbook("Assignment 1 - Test cases.xlsx")
ws = wb[" Test cases"]
print(f"Merged cells: {ws.merged_cells.ranges}")
for row in range(1, 10):
    for col in range(1, 7):
        cell = ws.cell(row=row, column=col)
        print(f"Row {row}, Col {col}: {cell.value}")
