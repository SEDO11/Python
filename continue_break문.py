absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음

for student in range(1, 11):
    if student in absent:
        continue

    elif student in no_book:
        print("오늘 수업은 여기까지 {0}번 따라와".format(no_book))
        break

    print("{0}번 학생 책 읽어봐".format(student))