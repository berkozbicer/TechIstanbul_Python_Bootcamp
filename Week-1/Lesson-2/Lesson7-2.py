food = input("Enter food name? ")
drink = input("Enter drink name? ")

if food == "pizza":
    print("You ordered right food.")
    if drink == "cola" or drink == "ayran":
        print("You ordered right drink.")
        print("Enjoy your meal!")
    else:
        print(f"You did not order {drink} rightly.")    
else:
    print(f"You did not order {food} rightly.")
    print("Please order again.")