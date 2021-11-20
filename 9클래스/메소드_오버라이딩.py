#다중 상속 -> 부모 클래스가 두 개 이상

#일반 유닛
class Unit: #부모 클래스
    def __init__(self, name, hp, speed): #필요한 값 정의
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도: {2}]".format(self.name, location, self.speed))
       
#공격 유닛 / 상속
class AttackUnit(Unit): #자녀 클래스 #공격 유닛은 일반 유닛을 상속 받아서 만듬
    def __init__(self, name, hp, speed, damage): #필요한 값 정의
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    #공격 할때
    def attack(self, location):
         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력] : {2}".format(self.name, location, self.damage))
    
    #공격 받을때
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기 , 공격 기능 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

    #오버라이딩, 재정의 
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)




#벌처 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")
#배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시", )