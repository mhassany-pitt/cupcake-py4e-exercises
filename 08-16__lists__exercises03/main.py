numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    numbers.append(float(user_input))

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
