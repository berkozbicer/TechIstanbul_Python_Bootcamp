oven_degree = 0
"""
while oven_degree <= 200:
    oven_degree += 50
    if oven_degree == 100:
        print("Oven is at 100 degrees, waiting to reach 200 degrees.")
        continue
    elif oven_degree == 200:
        print(f"Setting oven to {oven_degree} degrees.")
        break
print("Oven is preheated.")
"""

while oven_degree <= 200:
    oven_degree += 50
    match oven_degree:
        case 100:
            print("Oven is at 100 degrees, waiting to reach 200 degrees.")
            continue
        case 200:
            print(f"Setting oven to {oven_degree} degrees.")
            break
print("Oven is preheated.")