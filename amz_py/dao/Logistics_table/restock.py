import pandas as pd
from datetime import datetime

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