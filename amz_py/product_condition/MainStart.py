from openpyxl import load_workbook
from amz_py.product_condition.SourceInput import getdate
# from test.TargetOutput import update_sheet

# 遍历字典

fileaddress= r"C:\Users\Administrator\Desktop\小蜗牛\BusinessReport-14-11-24(1).xlsx"

productdict = getdate(fileaddress)

# update_sheet(productdict)

flag = 1

if flag == 1 and len(productdict.get("B0DHS2QMRS")) == 1:
    print("有,一个")


if flag == 1 and len(productdict.get("B0DHS2QMRS")) > 1:
    print("有多个")
