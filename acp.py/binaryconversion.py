num = int(input("Enter a decimal number: "))
binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

# nested loop just to print each digit
for i in binary:
    for j in i:
        print(j, end="")

print()
