fname = input("Enter a file name: ")
fhandle = open(fname)
counts = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
lst = []
for email, count in counts.items():
    lst.append((count, email))
lst.sort(reverse=True)
count, email = lst[0]
print(email, count)
