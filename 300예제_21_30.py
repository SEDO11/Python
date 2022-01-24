'''
# 21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python'
# 실행 예 p t
letters = 'python'
print(letters[0], letters[2])

# 22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"
# 실행 예: 2210
license_plate = "24가 2210"
print(license_plate[4: ])

# 23 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀
# hint [start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출
string = "홀짝홀짝홀짝"
print(string[::2])
# print(string[1::2]) 짝만 출력하는 방법

# 24 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
string = "PYTHON"
print(string[::-1])
'''
# #25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예 010 1111 2222
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

#26
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)

#27
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[1])

