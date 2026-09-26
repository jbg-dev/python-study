import random

print('==== 숫자 맞히기 게임 ====')
answer = random.randint(1,100)
number = int(input('1~100 사이의 숫자를 입력하세요: '))
count = 1
while answer != number:
    if answer > number:
        print('더 큰 숫자입니다.')
        number = int(input('1~100 사이의 숫자를 입력하세요: '))
    elif answer < number:
        print('더 작은 숫자입니다.')
        number = int(input('1~100 사이의 숫자를 입력하세요: '))
    count = count + 1

print('정답입니다!')
print('총 횟수: ',count)