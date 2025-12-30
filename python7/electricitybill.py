units = float(input("enetr the units : "))
if  units<50:
    amt = 2.60 *units+25
elif  units<100:
    amt = 3.25 *units+35
elif  units<200:
    amt = 5.26 *units+45
else:
    amt = 7.20 *units+75
print('the amt is $ :',amt)