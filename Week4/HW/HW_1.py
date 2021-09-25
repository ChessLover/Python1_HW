# Create the dictionary d with the following values {“name”: “Armen”, “age”: 15,
# “grades”: [10, 8, 8, 4, 6, 7] }. Write the following program:
# If the dictionary d doesn’t contain a key “weight” => take a number n of type int as a user
# input (using the function input()) and add the key:value pair “weight” : n to the
# dictionary d. Otherwise, if the dictionary d contains a key “weight”, print the value at the
# key “weight”.

d = {"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7] }

if "weight" not in d.keys():
    n = int(input())
    d["weight"] = n
    print(d)
else: 
    print("Dict value at the key weight: ", d["weight"])