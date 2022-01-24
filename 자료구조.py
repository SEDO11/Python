'''
자료구조의 변경
'''

#처음에는 set 타입
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

#list 타입으로 변환시켜서 list타입으로 변함
menu = list(menu)
print(menu, type(menu))

#tuple 타입으로 변환시켜서 tuple타입으로 변함
menu = tuple(menu)
print(menu, type(menu))

#set 타입으로 변환시켜서 set타입으로 변함
menu = set(menu)
print(menu, type(menu))