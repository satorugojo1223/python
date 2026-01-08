b = int(input("enter  base"))
p = int(input("enter  power"))

res = 1

for i in range(p):
    res = res*b
print(f"the answer to {b} power {p} is {res}")