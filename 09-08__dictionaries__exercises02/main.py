filename = input("Enter file name: ")
fhandle = open(filename)
email_counts = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_counts[email] = email_counts.get(email, 0) + 1
print(email_counts)
