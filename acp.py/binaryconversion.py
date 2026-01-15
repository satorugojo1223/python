num1 = float(input("Enter a decimal number: "))
binary = ""

while num1 > 0:
    rem = num1 % 2
    binary = str(rem) + binary
    num1 = num1 // 2

# nested loop just to print each digit
for i in binary:
    for j in i:
        print(j, end="")

print()
