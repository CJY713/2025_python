import yt_dlp
url = input('輸入網址')

ydl_opts = {
    'format':'best',
    'outtmp1':'%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
    