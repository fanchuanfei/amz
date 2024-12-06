import os
from datetime import datetime, timedelta
from openpyxl import load_workbook
from amz_py.file_conversion.conversion import convert_csv_to_xlsx
# 将下载下来的文件转换为xlsx文件
folder_path = r"C:\Users\Administrator\Desktop\小蜗牛\test"


#转换文件
convert_csv_to_xlsx(folder_path)

# 获取前一天的日期
yesterday = datetime.now() - timedelta(days=1)
formatted_yesterday = yesterday.strftime('%d-%m-%y')
new_file_name = f"BusinessReport-{formatted_yesterday}.xlsx"

# 拼接为文件
fileaddress = os.path.join(folder_path, new_file_name)




workbook = load_workbook(fileaddress)

worksheet = workbook.active

worksheet.cell(2,1,"test")

workbook.save(fileaddress)










