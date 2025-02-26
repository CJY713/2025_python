#老師程式碼:https://github.com/ChungyiBossi/2024_winter_HFU_python

import pandas as pd
from pprint import pprint
import requests
from bs4 import BeautifulSoup


# Step1 : requests
url = "https://www.twking.cc/"
r = requests.get(url)
r.encoding = 'utf8'       # 避免亂碼
#print(len(r.text))


# Step2 : 找訊息
soup = BeautifulSoup(r.text, 'html.parser')
#soup.find_all('div', class_='booktop')     # 下面寫法會更好,使用attrs={}
booktops = soup.find_all('div', attrs={"class":"booktop"})
for booktop in booktops:
    #print(booktop.p)

    # 在 booktop 內查找帶有 class="booktop_red" 的 <a> 標籤
    #booknames = booktop.find_all('p')
    #for bookname in booknames:  # 如果找到了對應的 <p> 標籤
    #    print(bookname.text.strip())  # 打印書名並去除多餘的空格

    # 老師方法1
    #tops = booktop.find_all('p')
    #top_type = tops[0].text     # top10的種類
    #print(top_type)
    #for top in tops[1:]:
    #    print('\t', top.a.text, ":", top.a.get('href'))

    # 老師方法2
    top_type = booktop.p.text
    tops = booktop.css.select('p a')
    print(top_type)
    for top in tops:
        print('\t', top.text, ":", top.get('href'))


## Step3 : collection
booktop_summarize = dict()
booktops = soup.find_all('div', attrs={"class":"booktop"})
for booktop in booktops:
    tops = booktop.find_all('p')
    for top in tops[1:]:
        top_book_name = top.a.text.strip()    # 小說名稱,並清除前後空白
        top_book_url = top.a.get("href")    # 小說的連結
        
        if top_book_name in booktop_summarize:
            booktop_summarize[top_book_name]['count'] += 1    # 已存在在紀錄中
        else:
            booktop_summarize[top_book_name] = {
                'count':1,
                'href':top_book_url
            }

#pprint(booktop_summarize)
#pprint(sorted(booktop_summarize.items(), reverse=True, key=lambda x:x[1]['count']))


sorted_booktop_summarize = sorted(
    booktop_summarize.items(), 
    reverse=True, 
    key=lambda x: x[1]['count'])

## Step4 : 格式
#[
#    {'name':'ABC', 'count':1, 'url':'http...'},
#    {'name':'DEF', 'count':2, 'url':'http...'},
#    {'name':'XYZ', 'count':1, 'url':'http...'}
#]

book_rows = list()
for book in sorted_booktop_summarize:
    book_name = book[0]
    book_count = book[1]['count']
    book_page_url = book[1]['href']
    book_row = {
        'novel_name': book_name,
        'top_count': book_count,
        'novel_page_url': book_page_url
    }
    book_rows.append(book_row)

booktop_summarize_df = pd.DataFrame(book_rows)
booktop_summarize_df.to_csv('booktop.csv')

