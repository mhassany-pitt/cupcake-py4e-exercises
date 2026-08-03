filename = input("Enter a file name: ")
fhandle = open(filename)
day_counts = {}
for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        day = words[2]
        day_counts[day] = day_counts.get(day, 0) + 1
print(day_counts)
