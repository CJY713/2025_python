from datetime import datetime, timedelta

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
print(date_list)
