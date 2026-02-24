x = [1,34,45,78]
y = [29,46,87,98]

xy = list(map(lambda a,b: a+b ,x,y))
print(x)
print(y)
print("the addition of x,y is",)
print(x,y)

List1 = [2,3,4,5,6,7,8,9,10,11]
def sqr(x):
    return x*x
print("the square of the list :")
print(list(map(sqr,List1)))