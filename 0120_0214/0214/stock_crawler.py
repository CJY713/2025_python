import requests
from program_set import setting
from datetime import datetime, timedelta
import time  # 新增時間模組



class Crawler:
    def __init__(self, date_mode):
        self.session = None
        self.crawler_set = setting['Crawler']
        self.url = self.crawler_set['url']
        self.headers = self.crawler_set['headers']
        self.date_mode = date_mode
            
    def get_session(self):
        if self.session is None:
            self.session = requests.session()

    def close_session(self):
        if self.session:
            self.session.close()
            self.session = None

    def get_date(self):
        if self.date_mode == '1':
            return [str(datetime.now().date()).replace('-','')]
        elif self.date_mode == '2':
            year = int(input('西元年:'))
            month = int(input('月:'))
            day = int(input('日:'))
            return [str(datetime(year=year,month=month,day=day).date()).replace('-','')]
        elif self.date_mode == '3':
            return self.__range_date

    def __range_date(self):   # 加 __ 可以讓外部不會呼叫到此函數
        """
        %Y 西元年 (四位數)  2025
        %m 月 (兩位數)  01
        %d 日 (兩位數)  01
        """
        start_date = input('輸入起始日期(格式 EX:2025-01-01):')
        start_date = datetime.strptime(start_date,'%Y-%m-%d').date()      
        # strptime 的 p -> parse 把字串解析成 datetime 物件
        end_date = input('輸入結束日期(格式 EX:2025-01-01):')
        end_date = datetime.strptime(end_date,'%Y-%m-%d').date() 
        days_delta: int = (end_date -  start_date).days
        date_list = []
        for i in range(days_delta+1):
            date = end_date - timedelta(days=(days_delta-i))
            url_date = str(date).replace('-','')
            date_list.append(url_date)
        return date_list

    def stock_crawler(self):
        try:
            self.get_session()
            url_date_list = self.get_date()
            for url_date in url_date_list:
                json_data = self.session.get(
                    self.url.format(date = url_date), headers = self.headers).json()
                yield json_data, url_date
                if len(url_date_list) != 1:  # 新增延遲
                    time.sleep(5) # 傳送一筆資料暫停 5 秒 以免被證交所鎖IP
        except:
            self.close_session()





