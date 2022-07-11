# following are the built-in function of list

list1 = [1, 2, 3, 4, 5, 6, 7]  # inserts the element at the end of the list
list2 = ['Salman', 'Ali', 'zaidi']
list1.append('Salman')
print(list1)

list2.insert(3, 'Ali')  # here the element is added on a specific index
print(list2)


print(list1.extend(list2))
print(list1)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 2, 2]
print(sum(list3))  # if the list contains an alphabet than it will give an error

print(list3.count(2))  # return the total occurrence of the given element
print(list2.count('s'))  # this will give a wrong output as it is searching for an element 's' rather than 's' char...
print(list1.count('Salman'))

print(len(list3))

print(list3.index(2))  # returns the searched indec
print(list3.index(2, 3, 13))

# returns the minimum and maximum values
print("The min")
print(min(list3))
print("The max")
print(max(list3))

print("Sorting")
list4 = [4, 3, 2, 5, 6, 8, 9, 2]
list4.sort()
print(list4)
list4.sort(reverse=True)  # here reverse = True reversed the list
print(list4)
list5 = [4, 3, 2, 5, 6, 8, 9, 2]
sorted(list5)
print(list5)  # this print result will show that the list is still printing in the same order that is because sorted
# does sort the list permanently it returns a sorted list
print(sorted(list5))  # this is the main difference between b\w sort() & sorted()
# sort() permanently sort the list
# sorted() returns a sorted list without effecting the original order

print('Using del to delete')
print(list4)
del list4[3]
print(list4)
print("Using remove")
print(list4)
list4.remove(2)
print(list4)

print('clearing a list')
print(list5)
list5.clear()  # this clears the whole list and make it an empty list and note it that it does not delete the list it
# just clears it and an empty list exist

print(list5)

print(list4)
list4.reverse()
print(list4)

# copy a list
print('copying list')
list6 = list4.copy()
print(list4)
print(list6)

list4.clear()
print(list4)
print(list6)
