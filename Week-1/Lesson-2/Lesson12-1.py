day = int(input("What day of the week is it (1-7): "))

match day:
    case 1 | 3 | 6:
        print("Python Bootcamp Day!")
    case 2 | 4 | 5 | 7:
        print("Self Study Day!")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")