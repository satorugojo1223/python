try:
    bill = float(input("Enter total bill amount: "))
    paid = float(input("Enter amount paid: "))

    if bill < 0 or paid < 0:
        print("Error: Amounts cannot be negative")
    elif paid > bill:
        print("Error: Paid amount cannot be more than bill")
    else:
        due = bill - paid
        print("Due Amount:", due)

except ValueError:
    print("Error: Please enter valid numbers")
