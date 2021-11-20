# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" " )
#     print(lang1,lang2,lang3,lang4,lang5)
# profile("유재석", "20", "파이썬", "자바", "C", "C++", "C#")
# profile("김태호", "21", "파이썬", "코틀린", "스위프트", "", "")

# 가변인자를 사용할 때
def profile(name, age, *languege): # *languege가 가변인자이다.
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" " )
    for lang in languege:
            print(lang, end=" ")
            
    print()

profile("유재석", "20", "파이썬", "자바", "C", "C++", "C#", "코틀린", "아두이노")
profile("김태호", "21", "파이썬", "코틀린", "스위프트")

