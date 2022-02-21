import random
start_message = "Enter the start of the range: "
stop_message = "Enter the end of the range: "
invalid_message = "Please enter a valid number: "
guess_message = "Guess a number: "
def get_number(message):
    while True:
        try:
            number = int(input(message))
            if number.isdigit():
                return number
                break
        except:
            print(invalid_message)
"""

def validate_range(start,stop):
    if start > stop:
        get_number(stop_message)
    else:
        random_number = random.randint(start,stop)
        return random_number

def get_attempt(random_number):
    attempts = 0
    while True:
        try:
            guessed_number = int(input(guess_message))
            attempts+=1
            if guessed_number == random_number:
                return attempts
                break
        except:
            print(invalid_message)

def print_result(times):
    times = get_attempt()
    if times > 1:
        print(f"You guessed the number in {times} attempts")
    else:
        print(f"You guessed the number in {times} attempt")
def execute():
    start = get_number(start_message)
    stop = get_number(stop_message)
    random_numb = validate_range()
    attempted_number = get_attempt(random_numb)
    final_output = print_result(attempted_number)

execute()
"""
get_number(start_message)



# Write your code here.
# Make sure to use `random.randint` to pick your random number.
