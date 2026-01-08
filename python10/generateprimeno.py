l = int(input("enter the lower limit : "))
kj = int(input("enter the upper limit : "))


for i in range(l,kj+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
