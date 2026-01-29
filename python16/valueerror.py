try:
    n = int(input("enter the number : "))
    print("the value of n is",n)
except ValueError as ex:
    print("an error has occoured")