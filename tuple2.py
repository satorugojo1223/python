def palindrome(tuple1):
    s = 0
    e = len(tuple1)-1
    while(s<e):
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1 = (1,2,3,4,5,6,5,4,3,2,1)
res = palindrome(tuple1)
if res:
    print("the given tuple is a palindrome")
else:
    print("the given tuple is not palindrome")

