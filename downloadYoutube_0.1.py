import os
import pytube

print("다운받을 동영상 주소 입력하세요")
MRUrl = input()

yt = pytube.YouTube(MRUrl)

parent_dir = os.getcwd() # 현재 디렉토리 반환
parent_dir += '/Video' # Video 폴더가 없으면 자동으로 만들어줍니다.
# 만약 ssl 에러가 난다면 python 응용프로그램 폴더에 들어가서
# installCertification 을 실행 
yt.streams \
    .filter(progressive=True, file_extension='mp4') \
    .order_by('resolution')\
    .desc()\
    .first()\
    .download(parent_dir)

#수정 테스트 깃허브






