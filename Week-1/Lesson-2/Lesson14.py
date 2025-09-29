name1, name2, name3 = "Alice", "Bob", "Charlie"

print(name1 + name2 + name3)  # Concatenation without spaces
print(name1, name2, name3)     # Print with spaces
print(f"{name1} {name2} {name3}")  # Using f-string for formatted output
print("{} {} {}".format(name1, name2, name3))  # Using str.format method
print("{0} {1} {2}".format(name1, name2, name3))  # Using indexed placeholders
print("{name1} {name2} {name3}".format(name1=name1, name2=name2, name3=name3))  # Using named placeholders

text = "Hello Mr/Ms {}. Welcome to the platform."
print(text.format(name1))  # Formatting with a single placeholder
print(text.format(name2))  # Formatting with a single placeholder
print(text.format(name3))  # Formatting with a single placeholder

text1 = "Firsth place {} Second place {} Third place {}"
print(text1.format(name1, name2, name3))  # Formatting with multiple placeholders
print(text1.format(name3, name1, name2))  # Changing the order of placeholders
print(text1.format(name2, name3, name1))  # Changing the order of placeholders

print(text.count("l"))  # Counting occurrences of 'l'
print(text.count("o"))  # Counting occurrences of 'o'