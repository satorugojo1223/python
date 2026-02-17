dic1 = {"best1":3,"pencil2":3,"order":3,"list":2,"right":1}

k = 3
count = 0
for key,value in dic1.items():
    if dic1[key] == k:
        count+=1

print(f"the values which has {k} frenquency is {count}")