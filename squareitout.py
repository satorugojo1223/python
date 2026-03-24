start = int(input("Start: "))
end = int(input("End: "))

for n in range(start, end + 1):
    print(n*n, "even" if n*n%2==0 else "odd")