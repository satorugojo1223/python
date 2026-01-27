str1 = input("enter the choice : ")
for i in str1:
    if i.lower() == "a":
        print("A is present")
        break
else:
    print("A is not present in the phrase!")