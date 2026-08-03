filename = input("Enter a file name: ")
fhandle = open(filename)
domain_counts = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        domain = email.split("@")[1]
        domain_counts[domain] = domain_counts.get(domain, 0) + 1
print(domain_counts)
