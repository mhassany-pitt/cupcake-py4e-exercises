import string
fname = input("Enter a file name: ")
fhandle = open(fname)
counts = {}
for line in fhandle:
    line = line.lower()
    for ch in line:
        if ch in string.ascii_lowercase:
            counts[ch] = counts.get(ch, 0) + 1
lst = []
for letter, count in counts.items():
    lst.append((count, letter))
lst.sort(reverse=True)
for count, letter in lst:
    print(letter, count)
