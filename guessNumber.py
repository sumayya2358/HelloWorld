# Press the green button in the gutter to run the script.
import random

INVALID_NUMBER_MESSAGE = "Please enter a valid number."
INVALID_NUMBER = "INVALID_NUMBER"
GUESS_A_NUMBER = "Guess a number: "
START_RANGE_MESSAGE = "Enter the start of the range: "
END_RANGE_MESSAGE = "Enter the end of the range: "


def get_integer(message):
    while True:
        try:
            start = int(input(message))
            return start
        except:
            print(INVALID_NUMBER_MESSAGE)


def validate_range(start, stop):
    while start >= stop:
        print(INVALID_NUMBER_MESSAGE)
        stop = get_integer(END_RANGE_MESSAGE)
    return stop


def generate_range(start, stop):
    random_number = random.randint(start, stop)
    return random_number


def guess_a_number(random_number):
    guessed_number = INVALID_NUMBER
    no_of_attempts = 0
    while guessed_number != random_number:
        guessed_number = get_integer(GUESS_A_NUMBER)
        no_of_attempts = no_of_attempts + 1

    if no_of_attempts > 1:
        print(f"You guessed the number in {no_of_attempts} attempts")
    else:
        print(f"You guessed the number in {no_of_attempts} attempt")


def execute():
    start = get_integer(START_RANGE_MESSAGE)
    stop = get_integer(END_RANGE_MESSAGE)
    stop = validate_range(start, stop)
    generated_number = generate_range(start, stop)
    guess_a_number(generated_number)


execute()
