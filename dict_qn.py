def get_dictionary_of_string(string1):
    string_character = {}
    for char in string1:
        string_character[char] = string_character.get(char, 0) + 1
    return string_character


def create_strings_from_characters(frequencies, string1, string2):
    if string1 == "" and string2 == "":
        return 2
    if frequencies == {}:
        return 0

    string1_dict = get_dictionary_of_string(string1)
    string2_dict = get_dictionary_of_string(string2)

    final = []
    output = []
    for key in frequencies:
        if key in string1_dict:

            if frequencies[key] - string1_dict[key] < 0:
                final.append(0)
            else:
                final.append(1)
    for key in frequencies:
        if key in string1_dict:
            if frequencies[key] - string1_dict[key] >= 0:
                frequencies[key] = frequencies[key] - string1_dict[key]

    for key in frequencies:
        if key in string2_dict:

            if frequencies[key] - string2_dict[key] < 0:
                output.append(0)
            else:
                output.append(1)

    up_final = [1]
    up_output = [1]
    for num in final:
        if num == 0:
            up_final = [0]

    for numb in output:
        if numb == 0:
            up_output = [0]
    return up_final[0] + up_output[0]
