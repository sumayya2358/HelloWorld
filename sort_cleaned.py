NAME_IDX = 0
AGE_IDX = 1
SALARY_IDX = 2

NAME = "name"
AGE = "age"
SALARY = "salary"


def sort_by_name(elements):
    return elements[NAME_IDX]


def sort_by_age(elements):
    return elements[AGE_IDX]


def sort_by_salary(elements):
    return elements[SALARY_IDX]


sort_function_map = {NAME: sort_by_name, AGE: sort_by_age, SALARY: sort_by_salary}


def sort_employees(employees, sort_by):
    if not employees:
        return employees
    print(sort_by)
    print(sort_function_map[sort_by])
    return sorted(employees[1], sort_function_map[sort_by])


sort_by = "salary"
employees = [
    ["Jason", 26, 55000],
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Connor", 25, 110000]
]

sort_employees(employees, sort_by)
