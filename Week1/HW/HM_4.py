print("------------------------------------")

text = input()

# Welcome to USA. usa is awesome, isn't it?

count = text.count("USA") + text.count("usa")

text_lowercase = text.lower()
new_text = text_lowercase.replace("usa", "Armenia")

print("The given string: ", text)
print("The USA/usa count is: ", count)
print("The new string: ",new_text)

print("------------------------------------")