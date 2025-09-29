# Armstrong Number

# Way-1

""""
num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
"""

# Way-2

num = int(input("Enter a number: "))
strnum = str(num)
sum = 0

for i in strnum:
    digit = int(i)**len(strnum)
    sum += digit
    print(i, digit, sum)
    
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")