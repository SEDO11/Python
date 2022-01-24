name = input("이름을 입력하세요.> ")

mon = ["유비쿼터스 컴퓨팅", "비주얼 프로그래밍"]
tue = ["소프트웨어 공학"]
wen = ["컴퓨터 네트워크", "데이터 베이스"]
thu = ["인간관계(교양)", "비주얼 프로그래밍"]
fri = ["공강"]


day = input("날짜를 입력하세요.> ")
if day == "월" or day == "월요일":
    print(name + "님의 월요일 과목은 이렇습니다.", mon)  
elif day == "화" or day == "화요일":
    print(name + "님의 화요일 과목은 이렇습니다.", tue)
elif day == "수" or day == "수요일":
    print(name + "님의 수요일 과목은 이렇습니다.", wen)
elif day == "목" or day ==  "목요일":
    print(name + "님의 목요일 과목은 이렇습니다.", thu)
else:
    print(name + "님의 금요일 과목은 이렇습니다.", fri)
