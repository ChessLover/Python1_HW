# Create the list list2 with the following values ['a', 'abc', 'xyz', 's', 'aba', '1221']։ Count how
# many items from the list list2 are at least of length 2 and have the same first and last
# characters (i.e. ‘ala’,’sbhcues’, etc.). Print the result.

list2 = ['a', 'abc', 'xyz', 's', 'aba', '1221']

count = 0 

for l in list2: 
    if len(l)>1 and l[0]==l[-1]: 
        print(l)
        count += 1
        
print("Number of values from list which have at least length of 2 and the same first and last chars: ", count)