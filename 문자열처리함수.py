python = "Python is Amazing"
print(python.lower()) #모든 문자를 소문자로
print(python.upper()) # 모든 문자를 대문자로
print(python[0].isupper) #0번째 문자가 대문자가 맞는지 확인(불린, 참, 거짓)
print(len(python)) #총 길이 수를 나타냄
print(python.replace("Python", "Java")) #해당 문자를 다른 문자로 변경

index = python.index("n") #해당 문자가 몇 번째에 위치해 있는지 확인
print(index)
index = python.index("n", index + 1) #전에 찾은 위치 5 + 1을 해서 6번째 부터 n을 찾기 시작

print(python.find("Java")) #find은 값이 없으면 -1을 출력
#print(python.index("Java")) index는 값이 없으면 프로그램 종료

print(python.count("n")) #n이 총 몇 개 있는지 세줌
