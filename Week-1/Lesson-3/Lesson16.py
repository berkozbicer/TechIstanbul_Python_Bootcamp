# Find

sentences = input("Enter a sentence: ")
counter = 0

for i in sentences:
    if i == 'u' or i == 'U':
        counter += 1
print("Number of 'u' or 'U':", counter)

# print(sentences.upper().count("U")) 