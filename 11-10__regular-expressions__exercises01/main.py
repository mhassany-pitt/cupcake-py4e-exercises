import re
regex = input("Enter a regular expression: ")
count = 0
for line in open("mbox.txt"):
    if re.search(regex, line):
        count = count + 1
print("mbox.txt had", count, "lines that matched", regex)
