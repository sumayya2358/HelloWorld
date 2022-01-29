def do_some_action(sumayya, adeeb):
    love = sumayya + adeeb
    return love;


sasi = do_some_action(1, 2)
print(sasi)


def substract(input_1, input_2):
    output = input_1 - input_2
    return output


numbers = substract(45, 34)
print(numbers)


def range2(limit):
    list = []
    i = 0
    while i < limit:
        list.insert(i, i)
        i = i + 1
    return list


print(range2(3))


def range2(lower_limit, upper_limit):
    list = []
    i = lower_limit
    while i < upper_limit:
        list.insert(i, i)
        i += 1;
    return list


print(range2(3, 5))


def range2(lower_limit, upper_limit, step):
    list = []
    i = lower_limit
    while i < upper_limit:
        list.insert(i, i)
        i += step
    return list


print(range2(2, 10, 3))


def find2(list_of_fruits, target_fruit):
    for i in range(len(list_of_fruits)):
        if list_of_fruits[i] == target_fruit:
            return i


fruits = ["banana", "cherry", "apple", "orange"]
position = find2(fruits, "apple")
print(position)

