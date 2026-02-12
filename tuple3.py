tuplex = (0,0,0,1,0,1)
sun = 0
rain = 0
for i in tuplex:
    if i == 0:
        sun+=1
    else:
        rain+=1
if sun > rain:
    print("it is a good weather")
else:
    print("get and umbrella and still go to school      --great words by my mom")