def food(n):
    import requests
    import re

    url = "http://www.songkok.es.kr/lunch.list"
    text = requests.get(url).text
    # print(text)
    month = re.findall('date=+n+">(.+)</a>', text)
    print(month)

food(20170720)
