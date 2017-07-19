# list  tuple   set dictionary (=자바의 map과 같은 역할)
#   []  ()      {}      {}

a = {1,2,3,4,5};
print(a)
print(type(a))

#문제 list를 중복되지 않도록 표현해 봅니다.

r = {"name":"홍길동","age":20,"isMember":True,"height":185.7}
print(r)
print(r["name"])
r["age"] = 25;
print(r)

print("-"*50)

#dictionary의 key를 모아 뽑아올 수 있을까?
keys = r.keys()
print(keys)

#key의 목록만큼 반복 수행하여 value를 출력해 봅시다. 