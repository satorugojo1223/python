try:
    n1,n2=eval(input("enter the two numbers seperated by no."))
    r = n1/n2
    print("the result is :",r)
except ZeroDivisionError as ex:
    print("exception occoured",ex)
except SyntaxError as ex:
    print("exception occoured",ex)
except:
    print("wrong input")
else:
    print("no exception")
finally:
        print("nah im the stongest")