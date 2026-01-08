n = int(input("enter the numbeer asap : "))

sum = 0
num = n

while num !=0:
    rem = num%10
    sum = sum+rem ** 3
    num = num//10

if sum == n:
    print(n,"is an armstrong number")
else:
    print("dissapointment")