import os
import pandas as pd


def convert_csv_to_xlsx(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file = os.path.join(folder_path, filename)
            excel_file = os.path.splitext(csv_file)[0] + '.xlsx'
            df = pd.read_csv(csv_file)
            df.to_excel(excel_file, index=False)
            os.remove(csv_file)
            print(f'{filename} 已转换为 {os.path.basename(excel_file)} 并已删除原CSV文件')
        #



