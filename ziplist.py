a = [1,2,3,4,5,6]
b = ["a","b","c","d","e","f"]
print(list(zip(a,b)))
print("zip in reverse")
print(list(zip(a,b[::-1])))
stocks = ["nividia","intel","amd RYZEN","RAM"]
prices = [25000,9000,10000,10000000000000000000000000000000000000000000000000000]

print("stock prices")
dic_stocks = {s:p for s,p in zip (stocks,prices)}
print(dic_stocks)