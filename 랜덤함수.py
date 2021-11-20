from random import *

print(random()) #0.0~1.0 난수 발생
print(random() * 10) #0.0~10.0 난수 발생
print(int(random() * 10)) #0~10 난수 발생
print(int(random() * 10) + 1) #1~10 난수 발생

#로또번호 출력
''' 1번
print(int(random()*45)+1) #1~45 난수 발생
print(int(random()*45)+1) #1~45 난수 발생
print(int(random()*45)+1) #1~45 난수 발생
print(int(random()*45)+1) #1~45 난수 발생
print(int(random()*45)+1) #1~45 난수 발생
print(int(random()*45)+1) #1~45 난수 발생
'''

#2번
'''
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
print(randrange(1, 46)) #1부터 46미만 까지의 난수 발생
'''

#3번
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생
print(randint(1, 45)) #1부터 45까지의 난수 발생