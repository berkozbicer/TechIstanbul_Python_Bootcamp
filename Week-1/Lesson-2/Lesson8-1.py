classe = int(input("Enter your class (0-12): "))

if classe == 0:
    print("You are in Kindergarten.")
elif 1 <= classe <= 4:
    print("You are in Elementary School.")
elif 5 <= classe <= 8:
    print("You are in Middle School.")
elif 9 <= classe <= 12:
    print("You are in High School.")
else:
    print("Invalid class entered.")