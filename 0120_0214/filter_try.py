"""
pip install opencv-python
"""
import numpy as np
import cv2

# 讀取自己的圖片(JPG/PNG)
img = cv2.imread(r"C:\Users\Student\Desktop\2025\cat.jpg")
#cv2.imshow('cat', img)     # 用OpenCV顯示圖片

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('cat_gray', gray_img)        #顯示灰階圖

# 若要改變圖片大小
#resized_image = cv2.resize(gray_img, (int(gray_img.shape[1] * 0.5), int(gray_img.shape[0] * 0.5)))
#cv2.imshow('cat_gray_resized', resized_image)  # 顯示縮小後的灰階圖片

# 自訂濾波器
kernel = np.array([[0,1,-1],
                   [0,1,-1],
                   [0,1,-1] ])
filter_img = cv2.filter2D(gray_img, -1, kernel)
#cv2.imshow('cat_gray_filter', filter_img)

#cv2.waitKey(0)      # 0代表按任意鍵後才執行下一步,若是1會變成1毫秒後關閉
#cv2.destroyAllWindows()     # 關閉所有視窗

#-----------------------------------------

"""
pip install matplotlib
pip install scipy
"""
# 用 matplotlib 跟 scipy 看圖跟慮波
import matplotlib.pyplot as plt
from scipy import signal

# matplotlib用的通道是RGB
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#plt.imshow(img_rgb)
#plt.show()

kernels = np.array([
    [[-1,-1,-1],
    [1,1,1],
    [0,0,0]],
    [[-1,1,0],
    [-1,1,0],
    [-1,1,0]],
    [[0,0,0],
    [1,1,1],
    [-1,-1,-1]],
    [[0,1,-1],
    [0,1,-1],
    [0,1,-1]]
    ])

# 設定圖片大小
plt.figure(figsize=(12,8))

# 設定圖片放置規則
plt.subplot(1,5,1)
"""
圖片排列方式及圖片位置:
座位有1列,5個位置,此image要放在第1張的位置 -> (1,5,1)
+------+------+------+------+------+
| img1 | img2 | img3 | img4 | img5 |
+------+------+------+------+------+
"""
plt.imshow(img_rgb)
plt.axis('off')         # 將圖形的座標軸隱藏
plt.title('Origin')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
for i in range(len(kernels)):
    plt.subplot(1,5,i+2)
    filter_img = signal.convolve2d(img_gray, kernels[i])     # 做濾波
    plt.imshow(filter_img, cmap='gray')
    plt.axis('off')
    plt.title(f'filter{i+1}')


plt.show()