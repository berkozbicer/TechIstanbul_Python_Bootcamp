multiplier = 1
piece = 0
entered_numbers = ""

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        continue
    multiplier *= num
    piece += 1
    entered_numbers += str(num) + " x "

    if piece == 10:
        print("10 numbers have been entered.")
        print("Multiplier is:", multiplier)
        print("Numbers entered:", entered_numbers)
        break