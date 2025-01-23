'''age=int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")
else:
    print(f"You can try after {18 - age} years")

#Another example
x=input("Enter the color of the light: ")
if x=="red":
    print("Stop")
elif x=="yellow":
    print("Ready")
else:
    print("Go")'''


# nothing 
print(" ")

name = input("Enter your name: ")
marks = int(input("Enter your marks (out of 10): "))

if marks >= 10:
    print("Fool, you can't get more than 10 marks\n I'll tell to Teacher"+" " + name + " " + "Hahahahaha")
    exit()

if marks == 10:
    grade = "A1"
elif marks == 9:
    grade = "A2"
elif marks == 8:
    grade = "B1"
elif marks == 7:
    grade = "B2"
elif marks == 6:
    grade = "C1"
elif marks == 5:
    grade = "C2"
elif marks >= 4:
    grade = "D"
else:
    grade = "Fail"

print(f"{name}, you got grade: {grade}")