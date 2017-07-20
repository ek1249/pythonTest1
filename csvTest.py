import re
import random
#파일의 내용을 읽어 들여 보기 좋게 출력해봅니다.

f = open("data/kma.txt","r")
lines = f.readlines()
for i in lines:
    line = i.strip()
    print(i)

#도시명과 최고 온도만 출력해 봅니다.

#컴퓨터가 0-100사이의 난수를 발생하도록 하고 사용자가 이것을 알아 맞출때까지 반복 수행하도록 합니다.
n = random.randrange(100)
# print(n)
i = -1;
# print("n :",+n)
cnt=0
while i != n :
    cnt = cnt+1
    print("알아 맞춰 보세요 ",end="==> ")
    i = int(input())
    if i == n:
        break
    elif i>n:
        print("더 작은 수를 시도하세요.")
    else:
        print("더 큰 수를 시도하세요")

print(cnt,"번째에 성공 했습니다.")