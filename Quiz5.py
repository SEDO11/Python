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
'''
from random import *
count = 0

for customer in range(1, 51):
        timer = randint(5, 51)
        if timer <= 15 and timer >= 5:
            print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, timer))
            count += 1

        else:
            print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, timer))

print("총 탑승 승객: {0}분".format(count))
'''