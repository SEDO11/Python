'''
Quiz 1
변수명: station

변수값 : 사당, 신도림, 인천공항 순서대로 입력

  출력 문장 : xx 행 열차가 들어오고 있습니다.
  '''

# station = ["사당", "신도림", "인천공항"]
# print("{0}행 열차가 들어오고 있습니다.".format(station[0]))
# print("{0}행 열차가 들어오고 있습니다.".format(station[1]))
# print("{0}행 열차가 들어오고 있습니다.".format(station[2]))

'''
Quiz 2
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1: 랜덤으로 날짜를 뽑아야 함
조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3: 매월 1~3일은 스터디를 준비를 해야 하므로 제외

출력문 예제:
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

# from random import 
# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 {0} 일로 선정되었습니다.".format(day))

'''
Quiz 3
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예시) http://naver.com
규칙1 : http:// 부분은 제외 -> naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 (nav + 5 + 1 + !)

예) 생성된 비밀번호 : nav51!
'''

# site = "http://naver.com"
# site1 = site[7:-4]
# password = site1[:3] + str(len(site1)) + str(site1.count("e")) + "!"
# print("생성된 비밀번호: "+ password)

'''
Quiz 4
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하고 아이디는 1~20이라고 가정
조건2 : 댓글 내용 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
 -- 당첨자 발표 --
 치킨 당첨자 : 1
 커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
 '''

# from random import *

# human = list(range(1, 21))
# s = sample(human, 4)
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}".format(s[0]))
# print("커피 당첨자 : {}".format(s[1:4]))
# print("-- 축하 합니다 --")

'''
퀴즈5 당신은 코코아 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건2: 당신은 소요시간 5분 15분 사이의 승객만 매칭해야 합니다.

출력문 예제
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
'''
# from random import *
# total = 0

# for customer in range(1, 51):
#         timer = randint(5, 50)
#         if timer >= 5 and timer <= 15:
#             print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, timer))
#             total += 1

#         else:
#             print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, timer))

# print("총 탑승 승객: {} 분".format(total))

'''
Quiz 6
표준 체중을 구하는 프로그램을 작성하시오.

* 표준 체중 = 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자: 키(m) x 키(m) x 22
여자: 키(m) x 키(m) x 21

조건1: 표준 체중은 별도의 함수 내에서 계산
*함수명: std_weight
*전달값: 키(height), 성별(gender)
조건2: 표준 체중은 소수점 둘째자리까지 표시

출력예: 키 175cm 남자의 표준 체중은 67.38kg입니다.
'''
# height = 175
# gender = "여성"
# weight = 0

# def std_weight(height, gender):
#     if gender == "남자" or gender == "남성":
#         weight = float((height / 100) * (height / 100) * 22)
#         return weight

#     elif gender == "여자" or gender == "여성":
#         weight = float((height / 100) * (height / 100) * 21)
#         return weight

#     else:
#         print("성별이 옳바르지 않습니다.")

# weight = std_weight(height, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round(weight,2)))