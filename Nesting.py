#Nesting
# Example of nesting with input

# Nested if statements
def check_number():
    number = int(input("Enter a number: "))
    if number > 0:
        if number % 2 == 0:
            print("The number is positive and even.")
        else:
            print("The number is positive and odd.")
    elif number < 0:
        if number % 2 == 0:
            print("The number is negative and even.")
        else:
            print("The number is negative and odd.")
    else:
        print("The number is zero.")

# Nested loops
def print_pattern():
    rows = int(input("Enter the number of rows: "))
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

# Call the functions
check_number()
print_pattern()