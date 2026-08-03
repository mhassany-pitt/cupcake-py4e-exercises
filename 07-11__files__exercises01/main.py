file_name = input("Enter a file name: ")
fhand = open(file_name)
for line in fhand:
    print(line.rstrip().upper())
