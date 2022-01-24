'''
세트
집합 (set)
중복 안됨, 순서 없음, 수정가능
세트는 중괄호
'''
my_set = {1,2,3,3,3}
print(my_set)

javaA = {"유재석", "김태호", "양세형"} #중괄호
pythonA = set(["유재석", "박명수"])

#교집합 (java 와 python 을 모두 할 수 있는 개발자 찾기)
print(javaA & pythonA)
print(javaA.intersection(pythonA))

#합집합 j와 p 둘다 사용 가능한 개발자
print(javaA | pythonA)
print(javaA.union(pythonA))

#차집합 / j는 할 수 있지만 p는 할 줄 모르는 개발자
print(javaA - pythonA)
print(javaA.difference(pythonA))
#p는 할 수 있지만 j는 할 줄 모르는 개발자
print(pythonA - javaA)
print(pythonA.difference(javaA))

#p를 할 줄 아는 사람이 늘어남 / 값을 넣어준다
pythonA.add("김태호")
print(pythonA)

#java를 잊었어요 / 값을 뺀다
javaA.remove("김태호")
print(javaA)
