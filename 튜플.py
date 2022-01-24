#리스트와는 다르게 내용 변경, 수정 불가능 대신 속도가 빠름
#튜플은 소괄호
menu = ("돈까스", "치즈돈까스") #소괄호
print(menu[0])
print(menu[1])
#print(menu[])

#menu.add("생선까스") 이런 리스트 처럼 추가는 불가능

'''
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
'''

#튜플은 이런식으로 사용가능 / 위에 있는 코딩이랑 같음
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)