print("------------------------------------")
project = "cake"
difficulty = 3 
ingredients = ["flour", "butter", "sugar", "eggs", "cocoa powder", "baking powder"]

if "apple" in ingredients:
    print("List contains apple.")
else: 
    print("No any apple in the list.")
    
print("------------------------------------")

if "butter" in ingredients:
    print("List contains butter.")
else: 
    print("No any butter in the list.")    
  
print("------------------------------------")

if "eggs" or "margarine" in ingredients:
    print("List contains either eggs or margarine.")
else: 
    print("No any eggs or margarine in the list.")    
 
print("------------------------------------")

if "eggs" and "margarine" in ingredients:
    print("List contains either eggs or margarine.")
else: 
    print("No any eggs and margarine in the list.")    
    
print("------------------------------------")

flour = 175
butter = 175 
sugar = "100g"
eggs = 2 
cocoa_powder = "1ts"
baking_powder = 0.5

print("flour type is: ", type(flour))
print("butter type is: ", type(butter))
print("sugar type is: ", type(sugar))
print("eggs type is: ", type(eggs))
print("cocoa_powder type is: ", type(cocoa_powder))
print("baking_powder type is: ", type(baking_powder))

print("------------------------------------")

print("flour - ", flour)
print("butter - ", butter)
print("sugar - ", sugar)
print("eggs - ", eggs)
print("cocoa_powder - ", cocoa_powder)
print("baking_powder - ", baking_powder)

print("------------------------------------")