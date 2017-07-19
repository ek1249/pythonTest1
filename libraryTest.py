import requests
import re

url = "http://211.251.214.169:8080/SeatMate_sj/SeatMate.php?classInfo=1"
str = requests.get(url)
print(str)
print(str.text)
text = bytes(str.text,"iso-8859-1").decode("euc-kr");
#print(text)
title = re.findall("<title>(.*)</title>",text)
print(title)


#빈좌석을 모두 출력해봅시다.
#>172</div></TD>
print("-"*50)
seats = re.findall(">(.+)</div></TD>",text) #중요한 건 괄호표시 한다. .+ 뜻은 이 안에 포함된 문자가 한글자 이상이라는거
print(seats)

print()
cnt = 0
for i in seats:
    if i != "배정":
        print(i,end=" ")
        cnt = cnt +1
print()
print("빈좌석수: ",cnt)