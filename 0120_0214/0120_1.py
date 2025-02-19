import numpy as np

### 矩陣
a = [1,2,3,4]
matrix_a = np.array(a)
print(a,type(a),matrix_a,type(matrix_a))
b = [
    [1,2],
    [3,4],
]
matrix_b = np.array(b)
print(matrix_b)

# 1. 全零矩陣
zeros_matrix = np.zeros((2,3))      #(2,3)是2*3的矩陣
print(zeros_matrix)

# 2. 全一矩陣
ones_matrix = np.zeros((3,3)) 
print(ones_matrix)

muti_ones_matrix = np.zeros((3,2,2))     #有三層2*2的矩陣   #若(4,3,2,2)代表四組三層2*2的矩陣
print(muti_ones_matrix)

# 3. 指定範圍的矩陣
range_matrix = np.arange(0,10,2)     #寫法類似for迴圈中常見的range()
print(range_matrix)



### 隨機數
# 1. 均於分布的隨機數矩陣(0到1):
random_matrix = np.random.rand(3,2)
print(random_matrix)

random_int_matrix = np.random.randint(1,10,size=(3,2))
print(random_int_matrix)

# 2. 模擬丟硬幣 正面是1 反面是0
def coin_random(count):
    coin_random = np.random.randint(0,2,size=(count,))
    print(coin_random)
    front = 10 - np.sum(coin_random)
    back = 10 - front
    print(f'正面有{front}次,反面有{back}次')
coin_random(10)



"""
基本操作
"""

# 1. 訪問
matrix = np.array([10,20,30,40,50])
print(matrix[0])     #獲取第一個元素
print(matrix[-1])    #獲取最後一個元素
matrix2 = np.array([[10,20],[30,40]])
print(matrix2[0][1])
print(matrix2[-1][-1])

# 2. 切片操作
matrix3 = np.array([10,20,30,40,50])
print(matrix3[1:4])
print(matrix3[ : :-1])   #[50 40 30 20 10] 倒著數

# 3. 矩陣間的加減乘除
matrix = np.array([10,20,30,40])
matrix1 = np.array([1,2,3,4])
print(matrix + matrix1)
print(matrix - matrix1)
print(matrix * matrix1)
print(matrix / matrix1)
print(matrix % matrix1)        #餘數
print(matrix ** matrix1)       #指數

matrix = np.array([[10,20],[30,40]])
matrix1 = np.array([[1,2],[3,4]])
print(matrix * matrix1)      #是直接相乘,跟線代中的矩陣乘法不同

"""
在Numpy中,矩陣乘法可以分為兩種方式:
元素逐項乘法 和 線性代數的矩陣乘法。
"""
result = np.dot(matrix1,matrix2)
print(result)
result2 = matrix1 @ matrix2
print(result2)



"""
矩陣的屬性指令
"""
# 1. 形狀(shape)
matrix_2x3 = np.array([[1,2,3],[4,5,6]])
print(matrix_2x3.shape)

##改變矩陣形狀(非常重要以及實用)
matrix_1x6 = matrix_2x3.reshape(6)
print(matrix_1x6)

x,y = matrix_2x3.shape     #把(2,3)拆包給x,y
matrix_1x6 = matrix_2x3.reshape(x*y)
print(matrix_1x6)

matrix_1x6 = matrix_2x3.reshape(-1)
print(matrix_1x6)



"""
合併與分割矩陣
"""

# 1.合併矩陣
## 使用 np.concatenate
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6]])
combined_matrix = np.concatenate((matrix1,matrix2),axis=0)     #沿著行去拼接
print(combined_matrix)
combined_matrix = np.concatenate((matrix1,matrix2.T),axis=1)     #沿著列去拼接   #.T是轉置矩陣
print(combined_matrix)

# 2.分割矩陣
##使用 np.split
matrix = np.array([1,2,3,4,5,6])
split_matrix = np.split(matrix,3)
print(split_matrix,type(split_matrix))

##使用 np.vsplit 和 np.hsplit
# 垂直分割 : 行方向分割,看起來像"水平線分割"
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
v_split = np.vsplit(matrix,3)
print(v_split)
# 水平分割 : 列方向分割,看起來像"垂直線分割"
h_split = np.hsplit(matrix,3)
print(h_split)

word = 'ajpcjpvjspfaavjvoicddkiwk'
print(word.split('j'))


