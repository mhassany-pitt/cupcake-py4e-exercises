filename = input("Enter file: ")
fhandle = open(filename)
unique_words = []
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
print(unique_words)
