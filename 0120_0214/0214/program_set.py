
setting = {
    'Crawler':{
        'url':'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date}&type=ALLBUT0999&response=json&_=1739498178222',
        'headers':{
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
            }
    },
    'Process':{
        'drop_columns':['漲跌(+/-)','漲跌價差','最後揭示買價','最後揭示買量','最後揭示賣價','最後揭示賣量']
    },
}