#사전(키, 값)

#3은 유재석, 100은 김태호
캐비냇 = {3:"유재석", 100:"김태호"}
print(캐비냇[3])
print(캐비냇[100])
print(캐비냇.get(3))

'''
print(캐비냇[5])
print(캐비냇.get(5))
#get은 값이 없어도 사용 가능하지만, []은 값이 없으면 사용 불가능하다.
'''
print("hi")

'''
print(3 in 캐비냇) #True
print(5 in 캐비냇) #False
boolean 함수
'''

#문자형도 가능
캐비냇 = {"A-3":"유재석", "B-100":"김태호"}
print(캐비냇["A-3"])
print(캐비냇["B-100"])
print(캐비냇.get("A-3"))

#새 손님
print(캐비냇)
캐비냇["A-3"] = "김종국"
캐비냇["C-20"] = "조세호"
print(캐비냇)

#간 손님, del(딜리트), 키 삭제
del 캐비냇["A-3"]
print(캐비냇)

#key 들만 출력
print(캐비냇.keys())

#value 들만 출력
print(캐비냇.values())

# key, value 쌍으로 출력
print(캐비냇.items())

# 목욕탕 폐점, 모든 값 삭제
캐비냇.clear()
print(캐비냇)