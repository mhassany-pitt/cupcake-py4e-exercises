filename = input("Enter a file name: ")
fhandle = open(filename)
email_counts = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_counts[email] = email_counts.get(email, 0) + 1

bigcount = None
bigemail = None
for email, count in email_counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
print(bigemail, bigcount)
