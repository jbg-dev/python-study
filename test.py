answer = 37
number = int(input('숫자를 입력하세요: '))
while answer != number:
    if answer > number:
        print('더 큰 숫자입니다.')
        number = int(input('숫자를 입력하세요: '))
    elif answer < number:
        print('더 작은 숫자입니다.')
        number = int(input('숫자를 입력하세요: '))
print('정답입니다!')