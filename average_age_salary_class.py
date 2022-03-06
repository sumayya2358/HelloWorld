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
        Employee.calculate_average(age, salary)

    @classmethod
    def calculate_average(cls, age, salary):
        cls.number_of_employees()
        cls.sum_of_age(age)
        cls.sum_of_salary(salary)
        cls.average_age()
        cls.average_salary()

    @classmethod
    def number_of_employees(cls):
        cls.number_of_employees += 1

    @classmethod
    def sum_of_age(cls, age):
        cls.sum_of_age += age

    @classmethod
    def sum_of_salary(cls, salary):
        cls.sum_of_salary += salary

    @classmethod
    def average_age(cls):
        cls.average_age = cls.sum_of_age / cls.number_of_employees

    @classmethod
    def average_salary(cls):
        cls.average_salary = cls.sum_of_salary / cls.number_of_employees
