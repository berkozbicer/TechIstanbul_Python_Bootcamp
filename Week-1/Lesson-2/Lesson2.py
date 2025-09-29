answer = int(input("Did you join course? 1/0:"))

result = bool(answer)
print("result:", result)

if result == True:
    print("You have joined the course. You can take the certificate.")