def tip_amt(amt,per):
    tip = amt * per/100
    tamt = amt + tip
    tamt = round(tamt,2)
    print("the amount is",amt)
    print("the tip given is",tip)
    print("the total amt is",tamt)

amt = float(input("enter the amount :  "))
per = float(input("enter the percentage for the tip : "))
tip_amt(amt,per)