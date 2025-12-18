maths = float(input("the marks in maths are : "))

english = float(input("the marks in eng are : "))
bio = float(input("the marks in bio are : "))
pe = float(input("the marks in pe are : "))
comp = float(input("the marks in comp are : "))

total = maths+english+bio+pe+comp

per = total/500 * 100

print("the total marks are : ",total)
print("the percentage is",per)
