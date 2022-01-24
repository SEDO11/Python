
#리스트 []
# 리스트는 대괄호
# 지하철 칸별로 10, 20, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"] #대괄호
print(subway)
'''
#조세호씨가 몇 번째 칸에 타고 있는가?
#index는 해당 값의 위치 값을 출력해주는 코드이다. 0부터 시작
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
#append -> 뒤에 더하다
subway.append("하하")
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
# 1번째에 정형돈을 넣는다.
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
#유재석을 뒤에 넣어서 총 2명의 유재석이 나온다.
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
num_list = [5,2,3,4,1]
num_list.sort()
print(num_list)

#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)
'''
#다양한 자료형 함께 사용
num_list = [5,2,3,4,1]
mix_list = ["조세호", 20, True]
#print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)