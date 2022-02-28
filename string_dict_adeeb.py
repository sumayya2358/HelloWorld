def remove_frequency(frequencies, string):
    for char in set(string):
        if char in frequencies:
            frequencies[char] -= string.count(char)


def can_create_string(frequencies, string):
    for char in set(string):
        if char in frequencies:
            if (string.count(char) > frequencies[char]):
                return 0
        else:
            return 0
    remove_frequency(frequencies, string)
    return 1


def create_strings_from_characters(frequencies, string1, string2):
    return can_create_string(frequencies, string1) + can_create_string(frequencies, string2)
