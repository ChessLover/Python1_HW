# Create the list num with the following values [7,8, 120, 25, 44, 20, 27]։ Remove the even
# numbers from the list num, print the initial and changed versions of the list.

num = [7,8, 120, 25, 44, 20, 27]

num_odd = []

print("Lisy num before changes: ", num)

for i in range(len(num)): 
    if num[i] %2 == 1: 
        num_odd.append(num[i])


num = num_odd

print("Lisy num after changes: ", num)