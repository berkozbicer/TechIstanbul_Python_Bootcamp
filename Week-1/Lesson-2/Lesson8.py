score = int(input("Enter a note: "))

if score < 0:
    print("The note is invalid")
elif score < 70:
    print("The note is insufficient certificate of appreciation")
elif score < 85:
    print("The note is sufficient certificate of appreciation")
elif score <= 100:
    print("The note is good certificate of appreciation")
else:
    print("The note is invalid")