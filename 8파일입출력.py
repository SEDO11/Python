# w 쓰기 용도로 연다
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file= score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# a 이미 존재하는 파일에 이어서 쓴다.
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# r 파일에 있는 내용을 읽어온다.
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# 줄 별로 읽기, 한 줄 읽고 커서는 다음으로 이동
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#반복문을 통해 출력
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
