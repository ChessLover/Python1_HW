# Create the dictionary d with the following values {“name”: “Armen”, “age”: 15, “grades”:
# [10, 8, 8, 4, 6, 7] }. Write the following program:
# Take the list of Armen’s grades from the dictionary d and calculate the average of his
# grades. If the average of the grades is larger than 7 - print “Good job”, otherwise - print
# “You need to work more.''

d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7] }

grades_average = sum(d["grades"])/ len(d["grades"])

if grades_average > 7: 
    print("Good job!")
else: 
    print("You need to work more.")
    
    
