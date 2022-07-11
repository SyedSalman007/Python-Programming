# following are the built-in dictionary function

dic = {'a': 'apple', 'b': 'ball'}

print(dic.get('a'))
print(dic.get('c'))  # the get() function will return 'None' by default if there is no 2nd parameter
print(dic.get('c', 'There is no c'))  # if there is 2nd parameter then that will be printed

# nested get() can be used for nested dictionary

dic2 = {'alpha': {'a': 'apple', 'b': 'banana'}, 'digits': [1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 2, 2]}

print(dic2.get('alpha', 'No alpha here').get('b', 'There is no b'))  # using nested get()
print(dic2.get('digits', 'None').count(2))

print(dic.keys())
for val in dic.keys():
    print(val)

print("Before")
val = dic.keys()
print(val)

dic.update({'c': 'carrot'})
print('After')
print(val)
# by the above example we can clearly see that the key are updated automatically even without assigning the key again
# Note: The indexing will not work because dict_keys in Python 3 does not support indexing.

i = 0

for val in dic:
    if i == 1:
        #  print(f"The key is {i}")
        print("The key is = " + val)
    i += 1


print("Before")
val = dic.values()  # values() is used to print all the values of the keyword in dictionary
print(val)

dic.update({'d': 'drawing'})
print('After')
print(val)

# important thing to note is that key() & values() returns the values as list

salary = {"raj" : 50000, "striver" : 60000, "vikram" : 5000}

list1 = salary.values()
print('The salary = ', end='')  # best way to merge int and str or next print statement with the previous
print(sum(list1))
# another way to print in the above format
print('The salary = ' + str(sum(list1)))

# items() unpacks dictionary as a list of tuples

list2 = salary.items()
print(list2)
del salary['raj']
print(list2)

# trying to delete by using value

# del salary[5000] // this has caused error as we cannot del items using values

salary.clear()  # this function clears the whole dictionary but do not delete it
print("Salary dictionary cleared")
print(salary)

# the disadvantage of using clear() is that if we assign a dict to another dict and then clears the first dict then the
# second dictionary is cleared too.

dic3 = {'name': 'salman', 'city': 'karachi'}
dic3_2 = dic3

dic3.clear()
print("Dic3 = ", dic3)
print("Dic3_2 = ", dic3_2)

# as we can see both are cleared to avoid this to happen we do
print("better way")
dic3 = {'name': 'salman', 'city': 'karachi'}
dic3_2 = dic3

dic3 = {}
print("Dic3 = ", dic3)
print("Dic3_2 = ", dic3_2)

# copy just returns a copy of that dictionary

dic4 = dic3_2.copy()
print("copying dictionary")
print(dic3_2)
print(dic4)

# updating dictionary
dic3_2.update({'country': 'pakistan'})
print(dic3_2)
print(dic4)


# as copy() function performs a shallow copy so if one is cleared the other won't be effected

dic3_2.clear()
print(dic3_2)
print(dic4)

list3 = ['a', 'b', 'c']
dic5 = dict.fromkeys(list3)
print(dic5)
dic5 = dict.fromkeys(list3, 1)  # instead of 1 we can place a variable with value stored or any list or empty list []
print(dic5)
dic6 = dic5.fromkeys('a')  # here calling the fromkey() form another dic won't cause any effect it is better to call it
# with dict
print(dic6)

list4 = [1, 2, 3]
dic7 = dict.fromkeys(list3, list4)
print(dic7)
print('After appending')
list4.append(4)
print(dic7)
print("another way")
dic8 = {k: list(list4) for k in list3}
print(dic8)


Dictionary1 = { 'A': 'Apple', 'B': 'Ball', 'C': 'Carrot'}
print('Set default')
value = Dictionary1.setdefault('A')
print(value)

value = Dictionary1.setdefault('D')
print(value)

value = Dictionary1.setdefault('E', 'Elephant')  # this default also set the key and the value in original dictionary
print(value)
print(Dictionary1)

val = Dictionary1.pop('A', 'A not found')
print(Dictionary1)
print(val)

value = Dictionary1.popitem()  # this function deletes the last element from the end and return the
# deleted item as tuple
print("The deleted item is : " + str(value))
print(Dictionary1)

