def cube(n):
    return n*n*n

def divisible_by_3(n):
    if n%3 == 0:
        return cube(n)
    else:
        False

print("the cube of a number is divisible by 3",divisible_by_3(12))
print("the cube of a number is",divisible_by_3(5))


