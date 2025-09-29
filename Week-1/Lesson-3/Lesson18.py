import random
# guess

kept_number = random.randint(1, 10)

while True:
    entered_number = int(input("Enter a number (1-10): "))
    if entered_number < 1 or entered_number > 10:
        print("Please enter a number between 1 and 10.")
        continue
    if entered_number < kept_number:
        print("Too low! Try again.")
    elif entered_number > kept_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break