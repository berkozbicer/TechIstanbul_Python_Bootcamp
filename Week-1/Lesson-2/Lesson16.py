import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
else:
    print(f"Sorry, the correct number was {number}. Better luck next time!")