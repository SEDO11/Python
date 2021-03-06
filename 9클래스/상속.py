#상속 -> 물려받는 것

#일반 유닛
class Unit:
    def __init__(self, name, hp): #필요한 값 정의
        self.name = name
        self.hp = hp
       
#공격 유닛 / 상속
class AttackUnit(Unit): #공격 유닛은 일반 유닛을 상속 받아서 만듬
    def __init__(self, name, hp, damage): #필요한 값 정의
        Unit.__init__(self, name, hp)
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

#메딕 / 공격력이 없는 의무병 유닛


#파이어뱃
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격을 두 번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

