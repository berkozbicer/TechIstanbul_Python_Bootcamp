birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year

if age >= 18:
    print("You can get a driver's license.")
else:
    print("You are too young to get a driver's license.")
    print(18-age, "years left until you can get a driver's license.")
    print(f"You will be able to get a driver's license in {birth_year + 18}.")