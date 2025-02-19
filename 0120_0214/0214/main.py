from stock_crawler import Crawler
from data_process import DataProcess



def main():
    date_mode = input('輸入 1:今日資料, 2:指定日期資料, 3.指定範圍資料 :')
    crawler = Crawler(date_mode)
    data_process = DataProcess()
    crawler_data = crawler.stock_crawler()
    for json_data, url_date in crawler_data:
        data_process.data_to_csv(json_data, url_date)


if __name__ == '__main__':
    main()