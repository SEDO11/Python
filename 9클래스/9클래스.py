#클래스 = 붕어빵 틀 -> 무한정으로 만들 수 있게 만드는 것
#스타 유닛 만들기

# #마린
# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# #공격 함수
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력] : {2}".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", damage)

# 유닛 클래스 생성
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
