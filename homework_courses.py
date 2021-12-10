class Student:
    students_list = {}
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = {}
        self.overall_average_grade = 0           
         
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade(self):
        self.average_grades = {i: sum(j) / len(j)  for i, j in self.grades.items()}
        self.overall_average_grade = sum(self.average_grades.values()) / len(self.average_grades.values())
        return self.overall_average_grade   

    def rate_lecturers(self, lecturer, course, grade):
       if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
           lecturer.average_grade()
           Lecturer.lecturers_list[f'{lecturer.name} {lecturer.surname}'] = lecturer.average_grades
       else:
           return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\r\nФамилия: {self.surname}\r\nСредняя оценка за ДЗ: {self.overall_average_grade:.1f}\r\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\r\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.overall_average_grade < other.overall_average_grade

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.overall_average_grade == other.overall_average_grade

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.overall_average_grade >= other.overall_average_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer(Mentor):
    lecturers_list = {}
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = {}
        self.overall_average_grade = 0
        
    def average_grade(self):
        self.average_grades = {i: sum(j) / len(j)  for i, j in self.grades.items()}
        self.overall_average_grade = sum(self.average_grades.values()) / len(self.average_grades.values())
        return self.overall_average_grade

    def __str__(self):
        return f'Имя: {self.name}\r\nФамилия: {self.surname}\r\nСредняя оценка за лекции: {self.overall_average_grade:.1f}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.overall_average_grade < other.overall_average_grade

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.overall_average_grade == other.overall_average_grade

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.overall_average_grade >= other.overall_average_grade    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
       if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
           if course in student.grades:
               student.grades[course] += [grade]
           else:
               student.grades[course] = [grade]
           student.average_grade()
           Student.students_list[f'{student.name} {student.surname}'] = student.average_grades
       else:
           return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\r\nФамилия: {self.surname}'

def average_grade_students(list_students, course):
    count = 0
    val = 0
    for data in list_students.values():
        for course_id, grade_in in data.items():
            if course_id == course:
                count += 1
                val += grade_in
    if count == 0:
        print("Оценок по такому предмету нет")
        return -1
    return round(val/count, 2)

def average_grade_lecturers(list_lecturers, course):
    count = 0
    val = 0
    for data in list_lecturers.values():
        for course_id, grade_in in data.items():
            if course_id == course:
                count += 1
                val += grade_in
    if count == 0:
        print("Оценок по такому предмету нет")
        return -1
    return round(val/count, 2)

best_student = Student('Ruoy', 'Eman', 'your_gender')
mid_student = Student('Bob', 'Dilan', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java', 'Git']
mid_student.courses_in_progress += ['Python']
best_student.add_courses("Введение в программирование")
mid_student.add_courses("Введение в программирование")

cool_reviewer = Reviewer('Some', 'Buddy')
cool_lecturer = Lecturer('Michael', 'Doe')
bad_reviewer = Reviewer('Any', 'Buddy')
bad_lecturer = Lecturer('Jonh', 'Doe')
cool_reviewer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_lecturer.courses_attached += ['Git']
bad_reviewer.courses_attached += ['Git']
bad_lecturer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

bad_reviewer.rate_hw(best_student, 'Git', 9)
bad_reviewer.rate_hw(mid_student, 'Python', 8)
bad_reviewer.rate_hw(mid_student, 'Python', 7)

best_student.rate_lecturers(cool_lecturer, 'Python', 10)
mid_student.rate_lecturers(cool_lecturer, 'Python', 9)
best_student.rate_lecturers(bad_lecturer, 'Python', 5)
mid_student.rate_lecturers(bad_lecturer, 'Python', 3)
best_student.rate_lecturers(cool_lecturer, 'Git', 10)
mid_student.rate_lecturers(cool_lecturer, 'Git', 8)
best_student.rate_lecturers(bad_lecturer, 'Git', 5)
mid_student.rate_lecturers(bad_lecturer, 'Git', 6)


print(cool_lecturer)
print(bad_lecturer)
print(cool_reviewer)
print(bad_reviewer)
print(best_student)
print(mid_student)

# print(cool_lecturer < bad_reviewer)
print(cool_lecturer > bad_lecturer)
print(cool_lecturer == bad_lecturer)
print(cool_lecturer <= bad_lecturer)

print(best_student < bad_reviewer)
print(best_student != mid_student)
print(best_student >= mid_student)

print(Lecturer.lecturers_list)
print(mid_student.average_grades)
print(best_student.average_grades)
print(best_student.overall_average_grade)
print(Student.students_list)
print(Lecturer.lecturers_list)
print(average_grade_students(Student.students_list, 'Git'))
print(average_grade_students(Student.students_list, 'Python'))
print(average_grade_students(Student.students_list, 'It'))
print(average_grade_lecturers(Lecturer.lecturers_list, 'Git'))
print(average_grade_lecturers(Lecturer.lecturers_list, 'Python'))
print(average_grade_lecturers(Lecturer.lecturers_list, 'It'))

