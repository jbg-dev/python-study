print('===== 성적 관리 프로그램 =====\n\n')

number = int(input('학생 수를 입력하세요: '))
print('\n')

numbers = []

for i in range(number):
    score = int(input(str(i+1)+'번째 학생 점수: '))
    numbers.append(score)
print('\n')

def get_total(scores):
    return sum(scores)

def get_average(scores):
    return sum(scores)/len(scores)

def get_max_score(scores):
    return max(scores)

def get_min_score(scores):
    return min(scores)

print('점수: ',numbers)
print('최고점수: ',get_max_score(numbers))
print('최저점수: ',get_min_score(numbers))
print('총점: ',get_total(numbers))
print('평균: ',get_average(numbers))
