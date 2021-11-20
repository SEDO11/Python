# __init__ 은 파이썬에서 사용하는 생성자

class Unit:
    def __init__(self, name, hp, damage): #필요한 값 정의
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# __init__에서 self를 제외한 나머지 갯수만큼 정의를 해줘야함
#marine3 = Unit("마린") - > 이렇게 되면 hp, damage가 없으므로 에러뜸
 