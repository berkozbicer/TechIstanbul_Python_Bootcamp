#method 1

"""
answer = input("Would you like to pizza? (yes/no): ")

while answer.lower() == "yes":
    print("Here is your pizza! Enjoy!")
    answer = input("Would you like another pizza? (yes/no): ")
"""

#method 2

cevap = bool(input("Would you like to pizza? (True/False): "))

while cevap:
    print("Here is your pizza! Enjoy!")
    cevap = bool(input("Would you like another pizza? (True/False): "))