rom pytube import YouTube
import os
link = input('enter the link for the video you want to download: ')

yt = YouTube(link)

videos = yt.streams.all()

i = 0

for stream in videos:
    print(f'{i}::{stream}')
    i+= 1

download = int(input('enter the video number you want to download'))
cwd = os.getcwd()
vid = videos[download-1]
print('downloading...')
vid.download(cwd)
print('downloaded in: ')
print(cwd)