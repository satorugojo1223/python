mc = input("does the child has medical cause (Y/N)")
if mc.lower() == "n":
    att = int(input("enter the attendance"))
    if att > 75:
        print('you are allowed to write')
    else:
        print("you are not eligible")
elif mc.lower() == "y":
    print("you are allowed the exam")
else:
    print("invalid input")