list1 = [22,45,67,54,32,16,23]


list2 = list(set(list1))


list2.sort()


print("Second largest element is:", list2[-2])