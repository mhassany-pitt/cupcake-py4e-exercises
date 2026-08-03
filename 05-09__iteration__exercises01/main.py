total = 0
count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input")

print(total, count, total / count)
