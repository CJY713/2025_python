'''
pip install pytube
'''

from pytube import YouTube

def yt_dl(url):
    try:
        # 實例化物件
        yt = YouTube(url)
        print(f'正在下載{yt.title}')

        # 取得最高畫質的影片
        stream = yt.streams.get_highest_resolution()

        # 下載
        stream.download()
        print(f'{yt.title}下載完成')
    except Exception as e:
        print(f'錯誤原因:{e}')

if __name__ == '__main__':
    ur1 = input('輸入網址:')
    yt_dl(ur1)
    

