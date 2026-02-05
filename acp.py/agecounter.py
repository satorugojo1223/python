try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Error: Age cannot be negative")
    else:
        print("Age entered:", age)
        if age % 2 == 0:
            print("Age is Even")
        else:
            print("Age is Odd")

except ValueError:
    print("Error: Please enter a valid number")