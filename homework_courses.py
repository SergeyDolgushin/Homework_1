class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   

    def rate_lecturers(self, lecturer, course, grade):
       if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
       else:
           return 'Ошибка'



     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
       if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
           if course in student.grades:
               student.grades[course] += [grade]
           else:
               student.grades[course] = [grade]
       else:
           return 'Ошибка'




best_student = Student('Ruoy', 'Eman', 'your_gender')
mid_student = Student('Bob', 'Dilan', 'your_gender')
best_student.courses_in_progress += ['Python']
mid_student.courses_in_progress += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_lecturer = Lecturer('Michael', 'Doe')
cool_reviewer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Python']

cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
best_student.rate_lecturers(cool_lecturer, 'Python', 10)
mid_student.rate_lecturers(cool_lecturer, 'Python', 9)
 
print(best_student.grades)
print(cool_lecturer.name, cool_lecturer.courses_attached)
print(cool_lecturer.grades)
