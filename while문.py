# customer = "토르"
# index = 5
# while(index >= 1):
#     print("{0}님 커피가 준비 되었습니다, {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")


# 무한으로 실행되는 while문
# customer2 = "아이언맨"
# index2 = 1
# while True:
#     print("{0}, 커피가 준비되었습니다, 호출 {1}회".format(customer2, index2))
#     index2 += 1

customer3 = "토르"
person = "Unknown"

while person != customer3:
    print("{0}님 커피가 준비되었습니다. ".format(customer3))
    person = input("이름이 어떻게 되세요?> ")

    if person == customer3:
        print("{0}님 여기있습니다. 감사합니다.".format(customer3))
