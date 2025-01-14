import os

import openpyxl.utils
from openpyxl.reader.excel import load_workbook

from amz_py.logistics.restock import remove_colume

folder_path = r"E:\desktop\test\1.xlsx"

# sourceworkboook = load_workbook(folder_path)
# sourceworksheet = sourceworkboook.active
#
# remove_colume(sourceworksheet, 4)

start_index = openpyxl.utils.cell.column_index_from_string('L')
end_index = openpyxl.utils.cell.column_index_from_string('P')
for col in range(start_index,end_index+1):
    print(col)




