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
    if employees == []:
        return employees
    return sorted(employees[1], sort_function_map[sort_by])
