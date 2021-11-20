gun = 10

def checkpoint(soldier): # 경계근무
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldier
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldier):
    gun = gun - soldier
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총 수: {0}".format(gun))
# checkpoint(2) # 두명이 경계 근무를 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 수: {0}".format(gun))
