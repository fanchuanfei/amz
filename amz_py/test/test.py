import os
from openpyxl.reader.excel import load_workbook

folder_path = r"C:\Users\Administrator\Desktop\test\工作簿1.xlsx"

sourceworkboook = load_workbook(folder_path)
sourceworksheet = sourceworkboook.active

date = sourceworksheet.cell(1,3).value
date1 = sourceworksheet.cell(1,4).value
print(date)
print(date1)


