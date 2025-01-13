import os
from datetime import timedelta


# 数据源文件转换 并将文件名称修改为前一天
# folder_path：存放数据源文件夹的地址
def convert_csv_to_xlsx(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file = os.path.join(folder_path, filename)
            excel_file = os.path.splitext(csv_file)[0] + '.xlsx'
            df = pd.read_csv(csv_file)
            df.to_excel(excel_file, index=False)
            os.remove(csv_file)
            print(f'{filename} 已转换为 {os.path.basename(excel_file)} 并已删除原CSV文件')


# 开始读取数据表
def start_read_excel(folder_path):
    # 产品基础表的表格名称为  BusinessReport-20-12-24
    yesterday = datetime.now() - timedelta(days=1)
    formatted_yesterday = yesterday.strftime('%d-%m-%y')

    # 拼接产品基础表文件名 并读取文件
    datailpage_file_name = f"BusinessReport-{formatted_yesterday}.xlsx"
    datailpage_fileaddress = os.path.join(folder_path, datailpage_file_name)
    read_datailpage(datailpage_fileaddress)

    # 品牌表现表第二个下载 名称为 BusinessReport-20-12-24 (1)
    # 拼接品牌表现表并读取
    brandpf_file_name = f'BusinessReport-{formatted_yesterday}+" (1)".xlsx'
    brandpf_fileaddress = os.path.join(folder_path, brandpf_file_name)
    read_brandpf(brandpf_fileaddress)



    # 广告关键词  商品推广 搜索词 报告
    brandpf_file_name = "商品推广 搜索词 报告.xlsx"
    Ad_fileaddress = os.path.join(folder_path,brandpf_file_name)
    read_ad(Ad_fileaddress)


# 判断表格是否读完
def is_finished_reading(sourceworksheet,row,column):
     parentain = sourceworksheet.cell(row,column).value

     if parentain is None:
         return True
     else:
         return false


# 打开详情页面销售和流量 装入字典
def read_datailpage(datailpage_fileaddress):
    sourceworkboook = load_workbook(datailpage_fileaddress)
    sourceworksheet = sourceworkboook.active

    # key：父Asin  ， values:集合类型的子Sku，子Asin
    detailproductdict_result: dict = {}

    # 把数据加入到字典中
    for i in range(1, sourceworksheet.max_row+1):

        #1. 判断数据是否读完  N行 1列
        if is_finished_reading(sourceworksheet,i,1):
            break

        # 2.获取类的数据
        parentasin = sourceworksheet.cell(i, 1).value
        childasin = sourceworksheet.cell(i, 2).value
        titlestr = sourceworksheet.cell(i, 3).value
        titlestr.split(",")
        title = titlestr[0]
        sku = sourceworksheet.cell(i, 4).value
        total_sessions = sourceworksheet.cell(i, 5).value
        total_sessions_b2b = sourceworksheet.cell(i, 6).value
        page_views_total = sourceworksheet.cell(i, 7).value
        page_views_total_b2b = sourceworksheet.cell(i, 8).value
        recommended_offer_percentage = sourceworksheet.cell(i, 9).value
        recommended_offer_percentage_b2b = sourceworksheet.cell(i, 10).value
        ordered_items = sourceworksheet.cell(i, 11).value  # 已订购的商品数量
        ordered_items_b2b = sourceworksheet.cell(i, 12).value
        product_session_percentage = sourceworksheet.cell(i, 13).value  # 转化率
        product_session_percentage_b2b = sourceworksheet.cell(i, 14).value
        ordered_items_sales = sourceworksheet.cell(i, 15).value
        ordered_items_sales_b2b = sourceworksheet.cell(i, 16).value
        total_ordered_products = sourceworksheet.cell(i, 17).value
        total_ordered_products_b2b = sourceworksheet.cell(i, 18).value

        # 3.获取父类SKu
        parent_sku = sourceworksheet.cell(i, 4).value.rsplit("-", 1)[0]

        # 4.组合为字典key
        dict_key = parentasin+","+parent_sku

        # 5.创建子类
        childprodrct = ChildProduct(childasin, title, sku, total_sessions, total_sessions_b2b, page_views_total,
                                    page_views_total_b2b,
                                    recommended_offer_percentage, recommended_offer_percentage_b2b, ordered_items,
                                    ordered_items_b2b,
                                    product_session_percentage, product_session_percentage_b2b, ordered_items_sales,
                                    ordered_items_sales_b2b,
                                    total_ordered_products, total_ordered_products_b2b)

        # 6.进行判断
        # 字典有父类，直接添加子类到父类中
        if dict_key in detailproductdict_result:
            # 获取父类
            parentproduct = detailproductdict_result.get(dict_key)

            # 向父类里面添加子类
            parentproduct.add_child(childprodrct)
        else:  #字典中没有父类 ， 需要创建父类，和子类并将父类加入字典
            # 创建父类
            parentproduct = ParentProduct(parentasin,parent_sku)

            # 加入子类
            parentproduct.add_child(childprodrct)

            #将父类放入字典
            detailproductdict_result.update({dict_key,parentproduct})


        return detailproductdict_result


# 品牌绩效表装入字典
def read_brandpf(brandpf_fileaddress):
    sourceworkboook = load_workbook(brandpf_fileaddress)
    sourceworksheet = sourceworkboook.active

    # key：父Asin  ， values:集合类型的子Sku，子Asin
    brandproductdict_result: dict = {}

    # 把数据加入到字典中
    for i in range(1, sourceworksheet.max_row+1):

        if is_finished_reading(sourceworksheet, i, 1):
            break

        childasin = sourceworksheet.cell(i, 1).value
        title = sourceworksheet.cell(i, 2).value
        brandname = sourceworksheet.cell(i, 3).value
        avg_customer_review = sourceworksheet.cell(i, 4).value
        customer_reviews_count = sourceworksheet.cell(i, 5).value
        sales_rank = sourceworksheet.cell(i, 6).value

        bradproduct = ProductPerformance(childasin,title,brandname,avg_customer_review,customer_reviews_count,sales_rank)

        brandproductdict_result.update({childasin,bradproduct})

    return brandproductdict_result


# 广告表装入字典
def read_ad(Ad_fileaddress):
    pass