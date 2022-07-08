def expansion_of_list(listA, listB=[]):
    for elements in listA:
        if isinstance(elements, list):
            expansion_of_list(elements, listB)
        else:
            listB.append(elements)

    return listB


list1 = [[1, [[2]]], [1, 2], 3]
result = expansion_of_list(list1)
print(result)
