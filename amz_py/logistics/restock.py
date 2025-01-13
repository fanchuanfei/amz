import pandas as pd
from datetime import datetime

from amz_py.logistics.dao.Salesandinventory import SalesInventory


# 将 txt文件转换为 xlsx文件
def convert_txt_to_xlsx(txt_file_path, xlsx_file_path):
    """
    将指定的.txt文件转换为.xlsx文件

    :param txt_file_path: .txt文件的路径
    :param xlsx_file_path: 输出的.xlsx文件的路径
    """
    # 获取的文件为当前时间的前七天数据
    current_day = datetime.now().day

    try:
        # 读取.txt文件，指定制表符为分隔符
        df = pd.read_csv(txt_file_path, delimiter='\t')

        # 将数据写入.xlsx文件
        df.to_excel(xlsx_file_path, index=False)
        print(f"成功将 {txt_file_path} 转换为 {xlsx_file_path}")
    except Exception as e:
        print(f"转换过程中出现错误: {e}")


# 读取前七天的销量  读取为字典， 使用SKu作为key
def read_Sales(fileaddress):
    sales_dict: dict = {}
    sourceworkboook = load_workbook(datailpage_fileaddress)
    sourceworksheet = sourceworkboook.active

    for i in range(2, sourceworksheet.max_row+1):
        product_name = sourceworksheet.cell(2,11).value
        sku = sourceworksheet.cell(2,12).value
        asin = sourceworksheet.cell(2,13).value
        quality = sourceworksheet.cell(2,15).value

        #里面有Sku
        if sku in sales_dict:
            salesinventory = sales_dict.get(sku)
            salesinventory.add_quality(quality)
        else:
            salesinventory = SalesInventory(asin,sku,product_name,quality)
            sales_dict.update({sku:salesinventory})



def read_inventory(sales_dict):
    pass


