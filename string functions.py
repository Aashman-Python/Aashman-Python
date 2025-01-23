#Ends with function

str="I'm studing python"
print(str.endswith("a"))#Output: False
print(str.endswith("hon"))#Output: True

# Nothing


print(" ")

#Capitalize function
str="python is easy"
print(str.capitalize())#Output: Python is easy

str="python can be easy"
str=str.capitalize()
print(str)#Output: Python can be easy 

# Nothing


print(" ")

#Reaplace old new
str="Ooshmon"
print(str.replace("o" ,"a"))#Output: Aashman
str="Ooshmon"
str="Ooshmon".replace("o","a")
print(str)#Output: Oashman

str="Ooshmon"
str=str.replace("o","a").replace("O","A")
print(str)#Output: Aashman

# Nothing


print(" ")

#Find function
str="Python is a programming language"
print(str.find("P"))#Output: 0 
print(str.find("y"))#Output: 1 
print(str.find("t"))#Output: 2
print(str.find("h"))#Output: 3
print(str.find("o"))#Output: 4
print(str.find("n"))#Output: 5
print(str.find("Z"))#Output: -1

# Nothing


print(" ")


# Count function
str="Python is a programming language"
print(str.count("P"))#Output: 1
print(str.count("y"))#Output: 1
print(str.count("t"))#Output: 2
print(str.count("h"))#Output: 2
print(str.count("o"))#Output: 2
print(str.count("n"))#Output: 3
print(str.count("Z"))#Output: 0