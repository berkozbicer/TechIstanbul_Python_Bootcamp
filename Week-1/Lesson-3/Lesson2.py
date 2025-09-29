name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

# for loop_variable in range(age):
#     print("{} times {}".format(loop_variable + 1, name))

for lc in range(len(name)):
        print("{} - {} - {}".format(lc + 1, name, name[lc]))