# if True: 
#     pass
# print("Hello, World!")

"""
for loop in range(10):
    name = input("Enter your name: ")
    if name == "Alice":
        print("ALice is found")
        break
    print(loop+1 , "times asked.")
"""

for loop in range(10):
    name = input("Enter your name: ").upper()
    if name == "ALICE":
        print(f"{name} is registered")
        continue
    surname = input("Enter your surname: ")
    print(f"{name} {surname} Welcome to the platform")