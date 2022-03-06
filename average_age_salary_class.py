class Employee:
    average_age = 0
    average_salary = 0
    number_of_employees = 0
    sum_age = 0
    sum_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.number_of_employees += 1
        Employee.sum_age += age
        Employee.sum_salary += salary
        print(Employee.sum_age)
        print(Employee.sum_salary)

        @classmethod
        def number_of_employees(cls):
            cls.number_of_employees += 1

        @classmethod
        def sum_age(cls, age):
            cls.sum_age += age

        @classmethod
        def sum_salary(cls, salary):
            cls.sum_salary += salary

        @classmethod
        def average_age(cls):
            return cls.sum_age(age) / cls.number_of_employees

        @classmethod
        def average_salary(cls):
            return cls.sum_salary(salary) / cls.number_of_employees

