def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = computepay(hours, rate)
print("Pay:", pay)
