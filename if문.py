
# weather = input("오늘은 날씨가 어떤가요?> ")

# if weather == "비":
#     print("우산을 챙기세요.")

# elif weather == "미세먼지":
#     print("마스크를 잘 챙기세요.")

# else:
#     print("오늘은 준비물이 필요 없어요.")

temp = int(input("기온은 어때요?: "))

if temp >= 30:
    print("너무 더워요 밖에 나가지 마세요.") 
elif temp >= 10 and temp < 30:
    print("괜찮은 날씨에요.")
elif temp >=0 and temp < 10:
    print("날씨가 추워요, 외투를 챙기세요.")
else:
    print("너무 추워요 나가지 마세요.")
