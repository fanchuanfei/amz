
from amz_py.product_condition.SourceInput import getdate
# from test.TargetOutput import update_sheet


# 存放数据源的文件地址
fileaddress= r"C:\Users\Administrator\Desktop\小蜗牛"

productdict = getdate(fileaddress)

# update_sheet(productdict)

flag = 1

if flag == 1 and len(productdict.get("B0DHS2QMRS")) == 1:
    print("有,一个")


if flag == 1 and len(productdict.get("B0DHS2QMRS")) > 1:
    print("有多个")
