name = "JohnDoe"

length = len(name)
print("Length of the name:", length)

print(name[0])  # First character
print(name[-1]) # Last character
print(name[1:4]) # Characters from index 1 to 3
print(name[:3])  # First three characters
print(name[3:])  # Characters from index 3 to the end
print(name[-4:]) # Last four characters
print(name[::2]) # Every second character
print(name[::-1]) # Reversed string
print(name.upper()) # Uppercase
print(name.lower()) # Lowercase
print(name.replace("o", "a")) # Replace 'o' with 'a'
print(name.split("D")) # Split at 'D'
print("John" in name) # Check if 'John' is in the name
print(name.startswith("John")) # Check if name starts with 'John'
print(name.endswith("Doe")) # Check if name ends with 'Doe'
print(name.find("D")) # Find index of 'D'
print(name.count("o")) # Count occurrences of 'o'
print(name.isalpha()) # Check if all characters are alphabetic
print(name.isdigit()) # Check if all characters are digits
print(name.isalnum()) # Check if all characters are alphanumeric
print(name.strip()) # Remove leading/trailing whitespace    
print(name.center(20)) # Center the string in a field of width 20
print(name.ljust(20)) # Left justify in a field of width 20
print(name.rjust(20)) # Right justify in a field of width 20
print(name.zfill(20)) # Pad with zeros to a width of 20
print(name.encode()) # Encode the string to bytes
print(name.title()) # Title case
print(name.swapcase()) # Swap case
print(name.partition("D")) # Partition at 'D'
print(name.rpartition("D")) # Reverse partition at 'D'
print(name.format()) # Format the string (no placeholders here)
print(f"Name is: {name}") # f-string formatting
print("Name is: {}".format(name)) # str.format() method 
print("Name is: %s" % name) # Old-style formatting
print(name.translate(str.maketrans("o", "a"))) # Translate 'o' to 'a'
print(name.removeprefix("John")) # Remove prefix 'John'
print(name.removesuffix("Doe")) # Remove suffix 'Doe'
print(name.islower()) # Check if all characters are lowercase
print(name.isupper()) # Check if all characters are uppercase
print(name.isspace()) # Check if all characters are whitespace
print(name.expandtabs()) # Expand tabs to spaces (no tabs here)
print(name.casefold()) # Casefold for caseless matching
print(name.removeprefix("John")) # Remove prefix 'John'
print(name.removesuffix("Doe")) # Remove suffix 'Doe'
print(name.islower()) # Check if all characters are lowercase
print(name.isupper()) # Check if all characters are uppercase
print(name.isspace()) # Check if all characters are whitespace
print(name.expandtabs()) # Expand tabs to spaces (no tabs here)
print(name.casefold()) # Casefold for caseless matching

print("o" in name) # Check if 'o' is in the name
print("x" not in name) # Check if 'x' is not in the name
print(name.index("D")) # Find index of 'D' (raises error if not found