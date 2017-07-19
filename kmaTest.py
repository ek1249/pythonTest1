import requests
import re

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

response = requests.get(url);
text = response.text
#print(response)
#print(response.text)

#pro = re.findall("<province>(.*)</province>",text);
#print(pro)

#Location을 모두 출력해 봅니다.
#Location에서 province,city,data를 찾아 출력해 봅니다.
#서울,mode,tmEf,wf,tmn,tmx
#.+ ==> 탐욕적(Greedy) : 전체를 한 덩어리로 봄
#.+? ==>  비탐욕적(nongreedy) : 각각의 요소로 처리됨
loc = re.findall('<location (.+?)</location>',text,re.DOTALL);
#print(len(loc))

#각각의 location에서 city를 출력
#각각의 location에서 data를 출력
for i in loc:
    city = re.findall("<city>(.+)</city>", i)
    data = re.findall("<data>(.+?)</data>",i,re.DOTALL)
    for d in data:
        tmEf = re.findall("<tmEf>(.+)</tmEf>",d)
        wf = re.findall("<wf>(.+)</wf>",d)
        tmn = re.findall("<tmn>(.+)<tmn>",d)
        tmx = re.findall("<tmx>(.+)</tmx>",d)
        print(city,tmEf,wf,tmn,tmx)
