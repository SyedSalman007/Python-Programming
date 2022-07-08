# Defining a Tuple

# a tuple is defined with square brackets () and are read only, once assign the value of tuple can not be updated
# each element of the tuple can also be accessed using indexes

dimension = (15, 10)

print(dimension)

print("Rectangle length is = ", dimension[0], "\nRectangle breath is = ", dimension[1])

# dimension[0] = 200  ( this code will give error as tuple' object does not support item assignment )

# as a single element tuple is of no use but it can form with a " , " at the end

dim = (1,) # this is a single element tuple

# looping in tuple

for value in dimension:
    print(value)

dims = (10, 23, 32, 40, 50, 45)

print("Other dimension printing using loop")

for value in dims:
    print(value)

# Writing over tuple

# As the value of the tuple can not be modified, but it can be overwritten
print("Another")

dims = (1, 2, 3, 4, 5)

for value in dims:
    print(value)     # tuple are like data structures



