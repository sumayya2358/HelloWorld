import random

start_message = "Enter the start of the range: "
stop_message = "Enter the end of the range: "
invalid_message = "Please enter a valid number."
guess_message = "Guess a number: "


def get_number(message):
    number = input(message)
    while not number.isdigit():
        print(invalid_message)
        number = input(message)
    else:
        return int(number)


def validate_range(start, stop):
    while stop < start:
        print(invalid_message)
        stop = get_number(stop_message)
    return stop


def generate_random(start, stop):
    random_number = random.randint(start, stop)
    return random_number


def get_attempt(random_number):
    attempts = 0
    while True:
        try:
            guessed_number = int(input(guess_message))
            attempts += 1
            if guessed_number == random_number:
                return attempts
                break
        except:
            print(invalid_message)


def print_result(attempts):
    if attempts > 1:
        print(f"You guessed the number in {attempts} attempts")
    else:
        print(f"You guessed the number in {attempts} attempt")


def execute():
    start = get_number(start_message)
    stop = get_number(stop_message)
    stop = validate_range(start, stop)
    random_number = generate_random(start, stop)
    attempts = get_attempt(random_number)
    print_result(attempts)


execute()
