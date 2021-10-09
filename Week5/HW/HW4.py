# Create 2 lists with the following values: list1 = [1, 3, 5, 7, 9, 11, 13, 15] and list2 = [4, 6,
# 14, 11, 8, 16]։ Go over the elements of list1 using a for loop, break from the loop as
# soon as you see a value that is also present in list2.

list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [4, 6, 14, 11, 8, 16]

for x in list1: 
    print(x)
    if x in list2: 
        break
    
