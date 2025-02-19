
from program_set import setting
import pandas as pd

class DataProcess:
    def __init__(self):
        self.process_set = setting['Process']

    # 資料處理完存入csv
    def data_to_csv(self, json_data, url_date):
        print(json_data)
        stock_data = json_data['tables'][8]
        column_name = stock_data['fields']
        stock_df = pd.DataFrame(stock_data['data'],columns=column_name)
        stock_df = stock_df.drop(self.process_set['drop_columns'],axis=1)
        stock_df = stock_df[stock_df['證券代號'].apply(lambda x:x.isdigit())].reset_index(drop=True)
        stock_df.to_csv(f'{url_date}.csv')
        print('儲存成功')
