def load_students():
    students = []

    with open('test.txt', 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            student = {
                'name' : data[0],
                'score' : int(data[1])
            }
            students.append(student)
    return students

def print_students(students):
    for student in students:
        print(student['name'],':',student['score'])

def max_students(students):
    name = ''
    max_score = 0
    for student in students:
        if student['score'] >= max_score:
            max_score = student['score']
            name = student['name']
    return name

def average_students(students):
    try:
        total = 0
        for student in students:
            total = total + student['score']
        return total/len(students)
    except ZeroDivisionError:
        print('학생 수가 0명입니다.')
        return '없음'

def add_students(students):
    name = input('추가할 학생의 이름을 입력하세요: ')
    score = int(input('추가할 학생의 점수를 입력하세요: '))

    student = {
        'name' : name,
        'score' : score
    }
    students.append(student)
    
    with open('test.txt','a',encoding='utf-8') as file:
        file.write(name+','+str(score)+'\n')

try:
    students = load_students()
except FileNotFoundError:
    print('학생 정보가 없습니다.')
    number = int(input('학생수: '))
    
    students = []

    for i in range(number):
        name = input(str(i+1)+'번째 학생 이름: ')
        score = int(input(str(i+1)+'번째 학생 점수: '))

        student = {
            'name' : name,
            'score' : score
        }

        students.append(student)

        with open('test.txt', 'a', encoding='utf-8') as file:
            file.write(name+','+str(score)+'\n')

#1. 학생 목록 보기
#2. 학생 추가
#3. 최고점 학생 보기
#4. 평균 점수 보기
#5. 종료

while True:
    print('==== 성적 관리 프로그램 ====')

    answer = input('메뉴를 선택하세요: ')

    if answer == '1':
        print_students(students)
    elif answer == '2':
        add_students(students)
    elif answer == '3':
        print('최고점 학생:',max_students(students))
    elif answer == '4':
        print('평균 점수:',average_students(students))
    elif answer == '5':
        break
    else:
        print('잘못된 메뉴 입력입니다.')
