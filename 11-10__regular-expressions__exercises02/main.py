import re
fname = input("Enter file: ")
count = 0
total = 0
for line in open(fname):
    matches = re.findall(r"New Revision: ([0-9]+)", line)
    if len(matches) > 0:
        count = count + 1
        total = total + int(matches[0])
print(total // count)
