'''
당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출려되어야 합니다.

- x 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건: 파일명은 1주차.txt, 2주차.txt, ... 와 같이 만듭니다.
'''
#시도한 코딩 / 안됨
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file= score_file)
# print("영어 : 50", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# num = 1
# score_file = open(num+"주차.txt", "w", encoding="utf8")
#     print("- "+num+ "주차 주간보고 -", file=score_file)
#     print("부서 : ", file=score_file)
#     print("이름 : ", file=score_file)
#     print("업무요약 : ", file=score_file)
#     score_file.close()

#해보니까 with만 되는 듯
#50개는 너무 많아서 10개만 만들었음 for문의 뒷 숫자만 바꾸면 50개 만드는거 쌉가능
for num in range(1, 2):
    with open("{0}주차.txt".format(num), "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(num))
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : \n")