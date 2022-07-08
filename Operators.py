#  arithmetic operators

a = 3  # int(input("Enter a value to add "))
b = 2  # int(input("Enter another a value to add "))

print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

# comparison operator

#  comparison operator always returns a boolean value and are mostly used in conditional statement

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
# these operators are ( and, or, not )
c = 1

if (a > b) and (b > c):
    print("This condition will only be executed if both the condition are true")

if (a > b) or (b > c):
    print("This condition will only be executed if any one condition is true")

print(not True)  # not operator simply revert the result if false then true and vice versa

# identity operator

d = 5
print(id(d))
e = 5
print(id(e))  # as in python the focus ok developer was to optimize the code as much as possible therefore if two
# variable is having same value then the python won.t the assigning new memory location and new value to that variable
# 'e' it will just simplify point e to d

print(d is e)  # true because they have same memory location
print(d is not e)
# identity operator is mostly used when working with multiple severs
# identity operators are used when we have two objects of same name, so they can only be differentiated by their memory
# location

# Membership Operator ( in , not in )
# they are used to check if a sequence is present in the object or not

list1 = []
# list of odd number till 50
for value in range(50):
    if value % 2 != 0:
        list1.append(value)

print(list1)

if 2 in list1:  # here the 'in' keyword checks the whole list that if there is a 2
    print("There is an even number list")
else:
    print("It is an odd number list")

if 3 not in list1:  # here the 'in' keyword checks the whole list that if there is a 2
    print("There is an even number list")
else:
    print("It is an odd number list")
