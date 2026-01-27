def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a = int(input("enter the a value   :   "))
b = int(input("enter the b value   :   "))
ch = input("a.addition\nb.subtraction\nc.multiply\nd.division\n enter you choice(a,b,c,d)  :  ")
if ch=="a":
    print("the addition of two numbers is",add(a,b))
elif ch=="b":
    print("the subtraction of two numbers is",sub(a,b))
elif ch=="c":
    print("the multiply of two numbers is",mul(a,b))
elif ch=="d":
    print("the division of two numbers is",div(a,b))
else:
    print("invalid bro how can someone be so dumb that even after the options are given if the options are not given i could atleast know that i have done a mistake but you are such an failure that you cant even type properly")