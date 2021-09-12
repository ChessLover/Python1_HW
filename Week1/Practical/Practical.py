#-----------------------------------------------
# Problem 2 

course = "Intro to Python"
student = "Sona Asatryan"
nickname = "ChessLover"
grade = 99 
pyhton_expert = False

print("course:", course)
print("student:", student)
print("nickname:", nickname)
print("grade:", grade)
print("pyhton_expert:", pyhton_expert)

#-----------------------------------------------
# Problem 3 

AB = 3
AC = 4 

BC = pow((AB**2+AC**2),0.5)

print("The hypotenuse of the triangle ABC = ", BC)

#-----------------------------------------------
# Problem 4

text = input()
start_index = int(input())
end_index = int(input())

print("Text: ", text)
print("Start index: ", start_index)
print("End_index: ", end_index)
print("Output string: ", text[start_index:end_index])

#-----------------------------------------------
# Problem 5

str1 = "How are you John?"
name = "Sona"

str2 = str1[:-5] + name + str1[-1]
print(str2)
str2 =  str1.replace("John", name)
print(str2)