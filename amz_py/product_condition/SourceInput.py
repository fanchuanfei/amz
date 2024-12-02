from test.myclass.SourceProductClass import Product

from openpyxl import load_workbook
from typing import Set

# 打开资源表 装入字典

def getdate(fileaddress):
    sourceworkboook = load_workbook(fileaddress)

    sourceworksheet = sourceworkboook.active

    # key：父Asin  ， values:集合类型的子Sku，子Asin
    productdict: dict[str, Set[Product]] = {}
    # 把数据加入到字典中
    for i in range(1, sourceworksheet.max_row+1):
        parensasin = sourceworksheet.cell(i, 1).value


        if parensasin is None:       #数据读完直接退出
            break

        # 存储数据到定义的的变量

        childasin = sourceworksheet.cell(i, 2).value
        session = sourceworksheet.cell(i, 4).value
        titlestr = sourceworksheet.cell(i, 3).value
        titlestr.split(",")
        title = titlestr[0]
        pageviews = sourceworksheet.cell(i, 8).value
        orders = sourceworksheet.cell(i, 20).value
        product = Product(parensasin, childasin,title, session,pageviews,orders)


        #把创建好的类放入字典的值中
        productchildset = {product}

        #判断是否为多Sku，如果是不用创建新集合，追加到对应父Asin下
        if parensasin == childasin:

            productdict.update({parensasin: productchildset})

        elif productdict.get(parensasin) is not None:

            productchildset = productdict.get(parensasin)

            productchildset.add(product)

        else:
            productdict.update({parensasin: productchildset})


    return productdict









