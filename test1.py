'''
문제3 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요.

예) http://naver.com
규칙1 : http:// 부분은 제외 -> naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
'''

#비교를 위한 초기값 모두 출력
start = 'http://kakao.com'
print(start)
#http:// 자르기
print(start[7:])

#http:// 자르기, .com 자르기, 역수는 뒤에서 부터 자른다.
pw1 = start[7:-4]
print(pw1)

#출력
print(pw1[0:3] + str(len(pw1)) + str(start.count('e')) + str('!'))
'''
출력해석
http://와 .com을 자르고
그 부분에서 처음 부터 세 번째 까지의 문자를 뽑아서 넣어준다
다 자른 부분의 글자의 갯수를 넣고
e의 갯수를 넣고
!를 넣어준다

그렇게 비밀번호가 완성된다.

알게 된 것 숫자(정수,실수)형은 문자형과 합해서 출력을 할 때 str을 통해서 문자형으로 바꿔준다.
'''