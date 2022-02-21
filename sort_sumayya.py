NAME = 0
AGE = 1
SALARY = 2


def sort_by_name(elements):
    return elements[NAME]


def sort_by_age(elements):
    return elements[AGE]


def sort_by_salary(elements):
    return elements[SALARY]


def sort_employees(employees, sort_by):
    if not employees:
        return employees
    elements = employees[1]
    if sort_by == "name":
        sorted_empl = sorted(employees, key=sort_by_name)
        return sorted_empl
    if sort_by == "age":
        sorted_empl = sorted(employees, key=sort_by_age)
        return sorted_empl
    if sort_by == "salary":
        sorted_empl = sorted(employees, key=sort_by_salary)
        return sorted_empl
