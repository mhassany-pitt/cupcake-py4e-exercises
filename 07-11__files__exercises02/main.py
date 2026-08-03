file_name = input("Enter the file name: ")
fhand = open(file_name)
total = 0.0
count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        total = total + float(line.split(":")[1])
        count = count + 1
print("Average spam confidence:", total / count)
