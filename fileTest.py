#
# #line = f.readline()
# lines = f.readlines()
# for line in lines:
#     line = line.strip() #개행 문자 제거
#     print(line)
# f.close()


#문제 파일명을 매개변수로 전달받아 해당 파일을 출력하는 함수를 만들고 호출해 봅니다.
# def readFile(fname) :
#     f = open(fname, "r")
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()  # 개행 문자 제거
#         print(line)
#     f.close()
#
# readFile("data/poem.txt")

#문제 자신의 이름과 나이를 파일로 출력해 봅니다. (파일명은 임의로 합니다.)
f = open("data/my.txt","w")
f.write("권지혜\n")
f.write("25")
f.close()
