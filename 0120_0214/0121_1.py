import pandas as pd
import numpy as np

### 表格合併

#相同欄位沿著 axis=0 方向合併,並忽略原有index
df_1 = pd.DataFrame({'A':[1,2]})
df_2 = pd.DataFrame({'A':[3,4]})
df_12 = pd.concat([df_1,df_2],ignore_index=True)
print(df_12)

#不同欄位沿著 axis=1 方向合併
df_3 = pd.DataFrame({'B':[3,4,5]})
df_13 = pd.concat([df_1,df_3],axis=1)
print(df_13)


### 群組運算 groupby
data = {
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,35,19,28],
    'City':['New York','Los Angeles','New York','Chicago'],
    'Salary':[20000,30000,50000,60000]
}
df = pd.DataFrame(data)
groupby_name = df.groupby('Name')
#print(groupby_name)
#print(list(groupby_name))
group_dict = {}
for name, data in groupby_name:
    group_dict[name] = data
print(group_dict)


# 高效數據查詢與計算

# &:and,  |:or
print( df[ (df['Age']>=20) & (df['Age']<=30) ] )
#print( df[ (df['Age']>=20) | (df['Age']<=30) ] )
print(df[df['Name'].str.len()==5])   #名字字串長度為5的資料

#使用 .query(' ') 在字串裡寫python條件判斷的感覺
print(df.query('20<=Age<=30'))
print(df.query('Name=="Alice"'))

# 用原有的資料創建新欄位的資料
df['New_Age'] = df['Age']+5
df['New_Salary'] = np.sqrt(df['Salary'])*200
print(df)
