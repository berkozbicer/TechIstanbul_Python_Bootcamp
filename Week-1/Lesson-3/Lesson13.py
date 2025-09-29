password = "s3cr3t"
remaining_attempts = 3

while remaining_attempts > 0:
    entered_password = input("Enter your password: ")   
    if entered_password == password:
        print("Access granted")
        break
    else:
        print("Access denied")
        remaining_attempts -= 1
        print(f"Remaining attempts: {remaining_attempts}")
        if remaining_attempts == 0:
            print("No attempts left. Access permanently denied.")
            break