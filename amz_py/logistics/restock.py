import os
import pandas as pd
from datetime import datetime
from openpyxl.reader.excel import load_workbook
from amz_py.logistics.dao.Salesandinventory import SalesInventory


# 将 txt文件转换为 xlsx文件
def convert_cvstxt_to_xlsx(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Process .txt files
            if filename.endswith('.txt'):
                try:
                    data = pd.read_csv(file_path, sep='\t', engine='python')  # Assuming tab-delimited text files
                    output_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.xlsx")
                    data.to_excel(output_file, index=False)
                    print(f"Converted: {filename} -> {os.path.basename(output_file)}")
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")

            # Process .csv files
            elif filename.endswith('.csv'):
                try:
                    data = pd.read_csv(file_path)
                    output_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.xlsx")
                    data.to_excel(output_file, index=False)
                    print(f"Converted: {filename} -> {os.path.basename(output_file)}")
                except Exception as e:
                    print(f"Failed to convert {filename}: {e}")






# 读取库存数据
def read_inventory(folder_path):
    inventory_dict: dict = {}
    inventory_fileaddress = os.path.join(folder_path,"库存.xlsx")
    sourceworkboook = load_workbook(inventory_fileaddress)
    sourceworksheet = sourceworkboook.active

    for i in range(2, sourceworksheet.max_row+1):
        # 通过SKu判断是不是我的产品 ，不是直接下一个
        if sourceworksheet.cell(i,1).value.split("-")[0] != 3:
            continue


        asin = sourceworksheet.cell(i,3).value
        sku = sourceworksheet.cell(i,1).value
        product_name = sourceworksheet.cell(i,4).value
        fulfillable_quantity = sourceworksheet.cell(i,11).value   # 可售数量
        reserved_quantity = sourceworksheet.cell(i,13).value # 预留数量
        currentAndReserve_inventory = fulfillable_quantity +  reserved_quantity

        inbound_working_quantity = sourceworksheet.cell(i,16).value  #已发货，但在处理 。 例如没填追踪码
        inbound_shipped_quantity = sourceworksheet.cell(i,17).value #已发货，在途数量

        Inbound_inventory = inbound_working_quantity + inbound_shipped_quantity

        salesinventory = SalesInventory(asin, sku, product_name, currentAndReserve_inventory,Inbound_inventory)

        inventory_dict.update({sku:salesinventory})




    return inventory_dict


# 读取前七天的销量
def read_Sales(folder_path,inventory_dict):
    inventory_fileaddress = os.path.join(folder_path,"销量.xlsx")
    sourceworkboook = load_workbook(inventory_fileaddress)
    sourceworksheet = sourceworkboook.active

    for i in range(2, sourceworksheet.max_row+1):
        # 通过SKu判断是不是我的产品 ，不是直接下一个
        if sourceworksheet.cell(i, 1).value.split("-")[0] != 3:
            continue

        sku = sourceworksheet.cell(i,12).value

        quality = sourceworksheet.cell(i,15).value

        salesinventory = inventory_dict.get(sku)

        salesinventory.add_quality(quality)

    return inventory_dict


#开始读取
def read_inventoryAndSales(folder_path):
    inventory_dict = read_inventory(folder_path)

    inventoryAndSales_dict = read_Sales(folder_path,inventory_dict)

    return inventoryAndSales_dict




# 写入销量和库存
def write_Salesandinventory(restocking_address,inventoryAndSales_dict):

    # 判断












