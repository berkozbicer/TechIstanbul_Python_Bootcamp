road = float(input("Enter the length of the road in km: "))
time = float(input("Enter the time in hours: "))
speed = road / time

if speed > 144:
    print(f"You are exceeding the speed limit! Your speed is {speed} km/h.")
else:
    print("You are within the speed limit.")