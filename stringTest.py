import re
import requests

str1 = '안녕하시렵니까.'
print(str1)
print(str1[0:4])
print(str1[6:])
print(str1[:6])

str2 = "홍길동\n강감찬"
print(str2)

str3 = "홍길동\t강감찬"
print(str3)

str = "aPple"
print(str.upper())
print(str.lower())

str4 = "아 기다리 고 기다리 던 방학이닷~!"
print(str4.count("기",0))

print("-"*50)
email = "tiger@nate.com"
print(email[:email.index("@")])

print("-"*50)
cut = re.findall("(.+)@",email)
print(cut[0])

