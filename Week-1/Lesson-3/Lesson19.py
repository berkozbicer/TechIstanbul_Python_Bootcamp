compound = ""

while True:
    sentence = input("Enter a sentence (or 'exit' to quit): ")
    if sentence.lower() == 'exit':
        print(compound)
        break
    else:
        compound += sentence + " "
        print("Current compound sentence:", compound)
        