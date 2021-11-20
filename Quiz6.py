'''
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

''' 
ver.1

height = 175
gender = "여자"
gram = 0

def std_weight(height, gender, gram):
    
    if gender == "남자":
        gram = float((height/100) * (height/100) * 22)
        return gram

    elif gender == "여자":
        gram = float((height/100) * (height/100) * 21)
        return gram

    else:
        print("잘 못 입력 했습니다.")

gram = std_weight(height, gender, gram)
print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, round(gram, 2)))
'''

'''
#ver.2
height = height = int(input("키를 입력하세요. cm: "))
gender = input("성별을 입력하세요. 남자 or 여자: ")
gram = 0

def std_weight(height, gender, gram):
    
    if gender == "남자":
        gram = float((height/100) * (height/100) * 22)
        return gram

    elif gender == "여자":
        gram = float((height/100) * (height/100) * 21)
        return gram

    else:
        print("잘 못 입력 했습니다.")

gram = std_weight(height, gender, gram)
print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, round(gram, 2)))
'''