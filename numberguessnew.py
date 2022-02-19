import random

while True:
    try:
        start = -1
        start = int(input("Enter the start of the range: "))
        stop = int(input("Enter the end of the range: "))
        random_num = random.randint(start, stop)
        break
    except:
        print("Please enter a valid number.")

lst = []
while True:
    try:
        number = int(input("Guess a number: "))
        lst.append(number)
        if number == random_num:
            break

    except Exception:

        print("Please enter a valid number.")

attempts = len(lst)
if attempts <= 1:

    print(f"You guessed the number in {attempts} attempt")
else:
    print(f"You guessed the number in {attempts} attempts")

# Write your code here.
# Make sure to use `random.randint` to pick your random number.
