#sep= -> 값 사이에 넣어줌, end= -> 끝에 이렇게 한다. 이거 쓰면 줄바꿈 안됨
# print("pytion", "java", "javaScript", sep=" vs ", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout) #표준출력
# print("python", "java", file=sys.stderr) #에러처리?

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #8칸의 공간을 확보하고 왼쪽정렬
#     #4칸의 공간을 확보하고 오른쪽 정렬
#     print(subject.ljust(8), str(score).rjust(4), sep= ":")

# 은행 대기 순번표
# 001 002 003 ...
# for num in range(1, 21):
#     #3칸의 공간을 확보하고 값이 없는 부분은 0을 채움
#     print("대기번호: "+str(num).zfill(3))

#입력은 무조건 str형태로 저장됨
answer = input("아무 값이나 입력하세요. : ")
print(type(answer))
# print("입력하신 값은"+answer+"입니다.")