# Create the list menu with the following values ['ice cream', 'chocolate', 'apple crisp',
# 'cookies']. Create the variable desert of type String and assign it the user input (use the
# function input()). Write the following program:
# If the value of the variable desert is present in the list menu, print “Your desert will
# arrive in 10 minutes”, otherwise, print “Please choose another desert” and ask the user
# for another input until the value entered by the user is from the list menu.

def check_desert_in_menu (menu): 
    des = input("Input any desert: ")
    if des in menu: 
        return True
    else: 
        return False

menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']

while check_desert_in_menu(menu)==False: 
    print("Please choose another desert.")

print("Your dessert will arrive in 10 minutes.")