from student import load_students,add_students,average_students,print_students,max_students

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

while True:
    print('==== 성적 관리 프로그램 ====')
    print('1. 학생 목록 보기')
    print('2. 학생 추가')
    print('3. 최고점 학생 보기')
    print('4. 평균 점수 보기')
    print('5. 종료')

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
