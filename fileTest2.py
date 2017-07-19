#kma의 전국의 중기예보를 파일로 저장하도록 합니다. (kma.txt)
import requests
import re

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
f = open("data/kma.txt","w")
response = requests.get(url);
text = response.text
loc = re.findall('<location (.+?)</location>',text,re.DOTALL); 
#print(len(loc))

#각각의 location에서 city를 출력
#각각의 location에서 data를 출력
for i in loc:
    city = str(re.findall("<city>(.+)</city>", i))
    data = re.findall("<data>(.+?)</data>",i,re.DOTALL)
    for d in data:
        tmEf = str(re.findall("<tmEf>(.+)</tmEf>",d))
        wf = str(re.findall("<wf>(.+)</wf>",d))
        tmn = str(re.findall("<tmn>(.+)<tmn>",d))
        tmx = str(re.findall("<tmx>(.+)</tmx>",d))
        f.write(city)
        f.write(tmEf)
        f.write(wf)
        f.write(tmn)
        f.write(tmx)
        f.write("\n")



