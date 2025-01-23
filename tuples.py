# Tuples in Python

# Creating a tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Nested tuples
nested_tuple = (1, (2, 3), 4)
print("Nested tuple:", nested_tuple)
print("Access nested element:", nested_tuple[1][1])

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.4)
print("Mixed tuple:", mixed_tuple)

# Tuple unpacking
a, b, c = my_tuple
print("Unpacked values:", a, b, c)

# Concatenation
concat_tuple = my_tuple + (4, 5, 6)
print("Concatenated tuple:", concat_tuple)

# Repetition
repeat_tuple = my_tuple * 2
print("Repeated tuple:", repeat_tuple)

# Slicing
slice_tuple = my_tuple[1:3]
print("Sliced tuple:", slice_tuple)

# Length of tuple
print("Length of tuple:", len(my_tuple))

# Checking membership
print("Is 2 in tuple?", 2 in my_tuple)
print("Is 5 in tuple?", 5 in my_tuple)

# Iterating through a tuple
for item in my_tuple:
    print("Item:", item)

# Tuple methods
print("Count of 2 in tuple:", my_tuple.count(2))
print("Index of 3 in tuple:", my_tuple.index(3))