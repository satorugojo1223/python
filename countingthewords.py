def count_words(list1):
    count = 0
    new_list = []
    for i in list1:
        if len(i) > 1 and i[0]==i[-1]:
            count+=1
            new_list.append(i)

    print(new_list)
    return count
list1 = ["young giris a","gozalo","demonslayer","racecar","BMW","vedio games","silk song"]
print("the count of words having first and last charectors are same",count_words(list1))
