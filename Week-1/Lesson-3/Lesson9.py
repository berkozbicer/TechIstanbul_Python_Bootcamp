multiplier = 1

while True:
    num = int(input("Enter a number: "))
    if not(num == 0):
        multiplier *= num
    else:
        print("Multiplier is:", multiplier)
        break