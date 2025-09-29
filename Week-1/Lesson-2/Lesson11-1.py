day = int(input("Enter day of week (1-7): "))

if day == 1 or day == 3 or day == 6:
    print("Python Bootcamp Day!")
elif day == 2 or day == 4 or day == 5 or day == 7:
    print("There is no Bootcamp today!")
else:
    print("Invalid input! Please enter a number between 1 and 7.")