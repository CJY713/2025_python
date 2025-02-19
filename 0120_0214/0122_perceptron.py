import numpy as np

class Perceptron:
    def __init__(self, weight=None, bias=0):
        if weight is None:
            self.weight = np.array([1,1])
        else:
            self.weight = weight

        self.bias = bias

    def activate_function(self,x):
        if x > 0:
            return 1
        return 0
    
    def output(self, input_data):
        WX = np.dot(self.weight, input_data)
        WX_b_sum = WX + self.bias
        return self.activate_function(WX_b_sum)
    

# 設置權重跟偏差值
weight = np.array([1,1])
bias = -1

# 實例化感知器
and_perceptron = Perceptron(weight,bias)

# 建立數組
input_data = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ])

# 資料代入AND感知器計算
for data in input_data:
    result = and_perceptron.output(data)
    print(f'{data} -> {result}')


# 嘗試做出 or 感知器
weight2 = np.array([1,1])
bias2 = 0
or_perceptron = Perceptron(weight2,bias2)
input_data = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ])
for data in input_data:
    result = or_perceptron.output(data)
    print(f'{data} -> {result}')
