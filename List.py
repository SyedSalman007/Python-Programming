# list can have any data type value in it

list1 = ["John", 40, "Salman", 20.343, 1 + 3j]  # list consisting of multiple data types

print(list1)

# accessing specific value from a list

list2 = ["John", "Alex", "Robert", "Max", "Stella"]  # list is indexed John is 0 index and Stella is 4
# list are ordered collections
print(list2[2])  # to print Robert we will place the index to be 2
print(list2[-2])  # by using the negative indexes we can access the list from left to write

print(list2[1:3])  # printing range of values from the list

# using the list values in other variables

message = f"This is a message for {list2[4]}"
print(message)

# modifying elements in the list

list2[0] = "Salman"  # this name will be replaced with the value at the mentioned index

print(list2)

# adding elements in the list

list2.append("Johnny")  # now the name johnny will be added at the end of the list

print(list2)

list3 = []
list3.append("Hello")
list3.append("World")
list3.append("Program")
print(list3)

# to add element in the list at any location

list3.insert(2, "Python")  # here Python will the placed exactly at the index

print(list3)

# Removing elements from the list
# using del we can delete any element from the list just by giving its possible index
del list2[3]  # Max will be deleted from the list
print(list2)

# using pop() to delete any element help us to hace access of that value after being delete

pop_list = list2.pop()  # the last element of the list is deleted and then returned to the assigning variable
print(list2)
print(pop_list)  # Johnny is stored in this variables

# removing element by value
# this is done when the position of the element to be removed is unknown

print(list3)
list3.remove('Python')
print(list3)

to_be_removed = 'Alex'
list2.remove(to_be_removed)
print(list2)
print(f"{to_be_removed} was removed from this chat")

# remove will delete that specific once so if that element reoccurs in that list then we use loop

# Organizing a list

# sort() sorts the list permanently

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # sort the elements and the alphabetic order
# now the list is sorted permanently and cannot be reverted


# to sort in reversed alphabetic order

cars.sort(reverse=True)
print(cars)

# temporarily sorting the list using sorted() function

# here we will be able to display the list in the sorted order without disturbing its actual order

car = {'bmw', 'audi', 'toyota', 'subaru'}

print("Original order of the list")
print(car)

print("Sorted order of the list")
print(sorted(car))

print("Original order of the list Again")
print(car)

# sorting the order alphabetically is more complex if all the values are not in lowercase

# printing the list in the reverse order

print(cars)
cars.reverse()
print(cars)

# length of the list
# len() function is used

print(len(cars))

# **********       WORKING WITH LISTS       **********

# using For loops

magicians = ['alice', 'david', 'carolina']
for name in magicians:  # here the element from the list is copied in the name variable
    print(name)
    print(f"{name.title()} thats a great trick !")  # we can add as many line of code in loop, the main thing to notice
# is that all the line to be executed in the loop must be indented

print(magicians)

# Making Numerical list

# range() function generates a series of numbers

for value in range(1, 6):
    print(value)

# using range() to make a list

Num_List = list(range(1, 6))  # if the list keyword is not used then [ range(1, 6) ] is stored exactly in the variable
# therefore by using the list keyword it assigns the value in a form of a list

print(Num_List)

# we can also list the number with spaces

num_list = list(range(2, 11, 2))  # here the number will the store with a gap of 2 and then an even number list we will
# be formed

print(num_list)

# ** this sign represents exponents
squares_value = []
squares = []  # empty list

for value in range(1, 11):
    squares_value.append(value)
    squares.append(value ** 2)

print(squares_value)
print(squares)

# min, max, and sum of a numeric list in python

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(list4))
print(max(list4))
print(sum(list4))

# List Comprehension

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# by using list comprehension we have optimized our previous code


# Slicing a list

players = ['Charles', 'marina', 'salman', 'ali']
print(players[1:3])
print(players[:2])
print(players[1:])
print(players[-2:])
print(players[0:3:2])  # gives a gap of one

# looping through a slice

player = ['Charles', 'marina', 'salman', 'ali']

for play in player[:2]: # here the loop will run till the indexed value 2
    print(play.title())

# Copying a list

played = player[:]  # copying all the elements of in another list

print(played)


played = player[2:]  # copying all the elements of in another list after index 2

print(played)

played = player[:2]  # copying all the elements of in another list till index 2

print(played)

played.append("Zaidi") # adding another element at the end of the list
print(player)
print(played)

# while copying elements from one list to another slicing is very imp
print(" hello ")
play = player # here a imp point if we do this then it will be treated as a single list and change in any will effect
# both
print(play)

print("Check the change")
play.append("Zain")
print(player)  # as from the output its clear that i have added the element in play but it was also included in player.

