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
