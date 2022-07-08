
def flatten_lists(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.extend(arg)
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, str) and arg.isdigit():
                new_args.append(int(arg))
            else:
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []
        for arg in args:
            if isinstance(arg, int):
                new_args.append(arg)

        result = func(*new_args)
        return result

    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)