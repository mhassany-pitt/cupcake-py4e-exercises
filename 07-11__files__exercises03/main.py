file_name = input("Enter the file name: ")
if file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(file_name) as file:
            subject_count = 0
            for line in file:
                if line.startswith("Subject:"):
                    subject_count += 1
        print("There were", subject_count, "subject lines in", file_name)
    except FileNotFoundError:
        print("File cannot be opened:", file_name)
