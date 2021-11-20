#파이썬 11~20예제 변수
'''
#11 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
주식 = 10
print("평가금액: ", (삼성전자 * 주식))

#12 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = "298조"
현재가 = "50000원"
PER = 15.79

print("항목 \t 값")
print("시가총액", 시가총액)
print("현재가", 현재가)
print("PER", PER)

#13 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
#>> s = "hello"
#>> t = "python"
#실행 예: hello! python

s = "hello"
t = "python"
print(s+ "!", t) 

#16 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
num = int(num_str)
print(type(num))
'
#17 정수를 문자열 100으로 변환
num = 100
num_str = str(num)
print(type(num_str))

#18 문자열을 실수로 변환
num1 = "15.79"
num1f = float(num1)
print(num1f, type(num1f))

#19 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 
# 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
year_int = int(year)
print(year_int)
print(year_int+1)
print(year_int+2)
print(year_int+3)

#20 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

aircon = 48584
month = 36
total = aircon * month
print("총 금액", total)
'''