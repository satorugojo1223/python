amt = int(input("enter the amount you wanna take out (-_*) "))

note100 = amt//100
note50 = (amt%100)//50
note10 = ((amt%100)%50)//10

print("the number of 100 dolla note is",note100)

print("the number of 50 dolla note is",note50)

print("the number of 10 dolla note is(bro too pooor ,homeless )",note10)