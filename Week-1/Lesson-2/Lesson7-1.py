food = input("Enter food name? ")
drink = input("Enter drink name? ")

if food == "pizza" and (drink == "cola" or drink == "ayran"):
    print("You ordered pizza and cola")
    print("Enjoy your meal!")
else:
    print(f"You did not order {food} and {drink}.")
    print("Please order again.")