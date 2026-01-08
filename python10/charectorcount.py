str1 = input("enter a phrase : ")
ch = input("enter a charecter : ")

count = 0
for i in str1:
    if ch == i:
        count+1

print(f"the number of {ch} in {str1} is {count}")