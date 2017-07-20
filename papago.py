import os
import sys
import requests
import re
import urllib.request
client_id = "xN7gmrW0UrPz03_4_VX9"
client_secret = "nildfM39yq"
encText = urllib.parse.quote("안녕 파파고")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
text=""
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    text = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)


#응답한 텍스트만 출력하기
trans = re.findall('translatedText":"(.+)"',text)
print(trans)