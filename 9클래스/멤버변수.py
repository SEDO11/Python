#멤버변수 -> 클래스내에 정의된 변수

class Unit:
    def __init__(self, name, hp, damage): #필요한 값 정의
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스
wraith = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}\n".format(wraith.name, wraith.damage)) #멤버 변수를 외부에서 사용 .name, .damage

# 마인드 컨트롤
# 상대방의 유닛을 뺏었다고 가정
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking =True #외부에서 추가적으로 추가사항 작성 가능

if wraith2.clocking == True: #wraith1은 클로킹이 없기 때문에 오류뜸
    print("{0} 는 현재 클로킹 상태입니다.\n".format(wraith2.name))
