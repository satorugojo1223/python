num = int(input("Enter a number: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * num

print("Result =", result)
