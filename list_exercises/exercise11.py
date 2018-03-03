strings = ["Hello", "I", "am", "a", "IT", "builder", "am", "I", "cool", "?"]
newstrings = []
for string in strings:
    if string not in newstrings:
        newstrings.append(string)
print(newstrings)