#함수의 매개변수의 기본값을 가질 수 있다.
def pro(a,b,c=500):
    print("a:",a)
    print("b:",b)
    print("c:",c)

pro(5,6)

#함수의 가변인자
def pro(**n): #dictionary로 묶어서 처리됨
    print(n)

pro(a=5)
pro(a=5,b=6)


