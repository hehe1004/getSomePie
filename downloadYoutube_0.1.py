import os
import pytube

print("다운받을 동영상 주소 입력하세요")
MRUrl = input()

yt = pytube.YouTube(MRUrl)

parent_dir = r"C:\Users\Public\Videos"

yt.streams \
    .filter(progressive=True, file_extension='mp4') \
    .order_by('resolution')\
    .desc()\
    .first()\
    .download(parent_dir)






