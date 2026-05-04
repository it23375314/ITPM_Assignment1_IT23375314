import openpyxl
wb = openpyxl.load_workbook("Assignment 1 - Test cases.xlsx")
ws = wb[" Test cases"]
for row in ws.rows:
    print([cell.value for cell in row])
