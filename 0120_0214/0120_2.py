"""
Pandas 是一個數據分析工具,提供高效能,易於操作的數據結構,
適用於資料處理與分析,
簡單來說,就是表格處理模組
pip install pandas
"""

import pandas as pd

# 主要物件

# pd 的 Series : 一維數據結構
s = pd.Series([10,20,30])
print(s)
s = pd.Series([10,20,30],index=['a','b','c'])
print(s)

# 取得Series的數據
print(s.values,type(s.values))
print(s['c'])

# 用字典創建 Series
dict1 = {'a':1,'b':2,'c':3}
s2 = pd.Series(dict1)
print(s2)
print(s+s2)


# DataFrame : 用二維數據結構,類似於Excel表格
# 往後可以使用 pd 編輯 excel檔案

# 方法1.使用字典轉成表格(df)
data = {'Name':['Alice','Bob'],
        'Age' :[25,30]}
df = pd.DataFrame(data)
print(df)

#方法2.先設定欄位名稱再塞入資料
columns_name = ['Name','Age']
data_list = [['Alice',25],['Bob',30],['Charlie',35]]
df2 = pd.DataFrame(data_list,columns=columns_name)
print(df2)

# 創建新欄位新資料
df['id'] = [1,2]
print(df)

# 轉換型態
#df['Age'] = df['Age'].astype(str)
#print(type(df['Age'][0]))

# 使用索引搜尋表格範圍 (.loc, .iloc)
print(df.loc[0,'Name'])     #使用標籤索引 (第一個參數:表格的index,第二個參數:欄位名稱)
print(df.iloc[1,0])         #使用整數索引 (第一個參數:表格的index,第二個參數:欄位所在的index)
print(df.loc[0])
print(df.iloc[0])

# 切片索引搜尋
print(df.loc[:,'Name'])
print(df.loc[0,:])
print(df.loc[:,'Age':'id'])


# 使用 Numpy 函數進行數值運算範例
import numpy as np

df['Age'] = np.log(df['Age'])   #底數預設e
# 要存新數值,要再賦值給原表格,類似修改後存檔的概念
print(df)


# 處理遺失資料

# 建立帶有缺失值的數據
data_nan = {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,np.nan,np.nan,28],
    'City':['New York','Los Angeles',np.nan,'Chicago'],
    'Salary':[50000,60000,70000,np.nan]
}

# 創建 DataFrame
df_nan = pd.DataFrame(data_nan)
print(df_nan)

#把有缺失值的資料都刪除
#df_nan = df_nan.dropna()                            # 預設刪除列資料,需回傳
#df_nan.dropna(inplace=True)                         # inplace=True 直接修改原資料,不需回傳
#df_nan = df_nan.dropna(axis='columns')              # 預設刪除有空值的欄資料
#df_nan = df_nan.dropna(axis='columns',how='all')    # 刪除所有資料都是空值的欄資料
#df_nan = df_nan.dropna(thresh=2).reset_index(drop=True)   # 列資料空值超過2個才會刪除該列,並重置index順序


### 判斷缺失值
print(df_nan.isnull())
print(df_nan.notnull())
print(df_nan.notnull().astype(int))    # 布林值轉換成 1 or 0

### 填補缺失數據

# 寫法1
# df_nan = df_nan.fillna(0)     #用0補空值
# 寫法2
# df_nan.fillna(0,inplace=True)   #inplace=True不用回傳
# print(df_nan)

# 使用平均值mean填補
#df_nan['Age'] = df_nan['Age'].fillna(df_nan['Age'].mean())
#print(df_nan)
# 使用眾數mode填補
#print(df_nan['City'].mode())   
#df_nan['City'] = df_nan['City'].fillna(df_nan['City'].mode()[0])
#print(df_nan)
# 使用中位數median填補
#df_nan['Salary'] = df_nan['Salary'].fillna(df_nan['Salary'].median())
#print(df_nan)

# 使用前一項數據補值
#df_nan = df_nan.ffill()
#print(df_nan)
#使用後項補值
#df_nan = df_nan.bfill()
#print(df_nan)

#設定不同欄位不同填充值
df_nan = df_nan.fillna(
    {
        'Age':df_nan['Age'].mean(),
        'City':df_nan['City'].mode()[0],
        'Salary':df_nan['Salary'].median(),

    }
)
print()
print(df_nan)