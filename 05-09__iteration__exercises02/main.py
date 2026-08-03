maximum = None
minimum = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input")
        continue
    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number
print("Maximum:", maximum)
print("Minimum:", minimum)
