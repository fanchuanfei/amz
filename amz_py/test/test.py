import os
from datetime import datetime, timedelta

from amz_py.dao.Logistics_table.restock import convert_txt_to_xlsx

folder_path = r"C:\Users\Administrator\Desktop\test\110881782419020101.txt"

output_path = r"C:\Users\Administrator\Desktop\test\20250113.xlsx"


convert_txt_to_xlsx(folder_path,output_path)