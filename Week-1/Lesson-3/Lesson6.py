piece = int(input("How many slice of pizza would you like: "))
slice = piece
a = 1

while a <= piece:
    print("This is slice number", a)
    a += 1

while slice > 0:
    print("Enjoy your slice of pizza")
    slice -= 1