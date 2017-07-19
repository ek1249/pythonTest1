#naver 최신뉴스를 긁어 파일로 출력합니다.
#제목,href만 출력합니다.

import requests
import re

url = "http://news.naver.com/"

response = requests.get(url);
text = response.text
# print(text);
title = re.findall('<ul id="text_today_main_news_801001" class="newsnow_txarea">(.+?)</ul>',text,re.DOTALL)
f = open("data/news.txt","w")

for i in title:

    a = re.findall('<a href="(.+?)"  class',i,re.DOTALL) #'+'는 찾으려는 장소 안에 있는 내용이 1글자 이상/?를 하는 이유는 예를들어 기상청의 <location>이 전체 소스에서 여러건이 있다는거/
    # re.DOTALL을 쓰는 이유는 내가 찾을 데이터가 한줄에 있을때는 안써도되는데 찾을 데이터가 여러줄에 걸쳐 있는 경우 사용한다!
    ti = re.findall("<strong>(.+?)</strong>",i,re.DOTALL)
    for j in range(len(a)):
        print(a[j]+" : "+ti[j])
        #f.write(ti[j]+":"+a[j]+"\n")




#print(title);
