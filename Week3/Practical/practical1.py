import sys 

script_name = sys.argv[0]
print("Script name: ", script_name)

num_of_arguments = len(sys.argv[1:]) 

print("Number of arguments: ", num_of_arguments)

print("Argument values: ", sys.argv)