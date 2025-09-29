words = input("Enter a words: ")

# print(words[::-1])

# for i in range(len(words)-1, -1, -1):
#     print(words[i], end="")

reverse = ""
for char in words:
    reverse = char + reverse
print("Reverse of", words, reverse)