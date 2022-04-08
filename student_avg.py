class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if not 0 < new_grade < 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = new_grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        sum_of_grade = 0
        print("==============================")
        for student in students:
            print(student.grade)
            sum_of_grade += student.grade
            # print(student.name+"=>"+student.grade)
        print("==============================")
        return sum_of_grade / len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        best_student = None
        max_grade = 0
        for student in cls.all_students:
            if student.grade > max_grade:
                max_grade = student.grade
                print(max_grade)
                best_student = Student(student.name, max_grade)
                print(best_student)
        return best_student

    # Write your code here.
