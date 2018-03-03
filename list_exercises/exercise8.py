list1 = [12, 34, 2, 5]
list2 = [4, 7, 16, 12]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i] * list2[i])
print(list3)