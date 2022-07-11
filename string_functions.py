# preferred website greek for greek
# following are the important built-in string functions

message = 'This is a strIng, As it MusT be WritTen in siNgle or doUble quote: '
short_message = 'It is a message'
print(message.lower())  # this will convert all the letter in lower case

print(message.upper())  # this will convert all the letter in upper case

print(message.title())  # this will convert all the first letter of a word in upper case and the rest of the word in
# lower case

print(message.capitalize())  # Converts the first character of the string to a capital (uppercase) letter and the
# remaining to lower case

print(message.casefold())  # casefold() method is used to implement caseless string matching. It is similar to lower()
# string method but case removes all the case distinctions present in a string. i.e ignore cases when comparing.

print(short_message.center(20,
                           '*'))  # center() method creates and returns a new string that is padded with the specified character

print(message.count('s'))  # count() function is an inbuilt function in python programming
# language that returns the number of occurrences of a substring in the given string.
print(message.count('s', 10, 30))  # second and third parameter is the start and end point to search in

# Encodes strings with the specified encoded scheme
print(short_message.encode('utf-8', "replace"))

print(short_message.endswith('message'))  # Returns “True” if a string ends with the given suffix
print(message.endswith('quote: '))  # to get true the suffix must be exactly same
print(short_message.endswith('is', 0, 5))  # here i find out that the starting value didn' have to be exact by thr
# ending value must be that where the string ends

message1 = 'Salman\tali\tzaidi'
print(message1.expandtabs(8))  # Specifies the amount of space to be substituted with the “\t” symbol in the string

print(short_message.find('s'))  # Returns the lowest index of the substring if it is found

# Python format() function has been introduced for handling complex string formatting more efficiently. (imp)

print("This is {}".format("Salman"))  # can use the string built-in in this way
format_txt = 'I am {} years old'
print(format_txt.format(18))

print("This is {} and my age is {} and currently i am an {}".format("Salman", 20, "Student"))

# formats with positional and keyword arguments

# positional

print("Hello and {0} to our daily {1}".format('welcome', 'meeting'))
print("Hello and {0} to our daily {1}".format('meeting', 'welcome'))
print("Hello and {1} to our daily {0}".format('welcome', 'meeting'))

# keyword

print("Hello and {h} to our daily {m}".format(h='welcome', m='meeting'))

# positional and keyword

print("It is my {} year of {p} ".format(2, p='programming'))
# print("It is my {} year of {p} ".format(p='programming', 2))  # this will give an error as positional comes first than
# keyword
# print("It is my {} year of {p} {}".format(2, p='programming', 'Bye'))  # same error as in previous

print("It is my {} year of {p} {}".format(2, ', It\'s salman', p='programming'))

var = 'Salman'
var1 = 'Ali'
var3 = 's'
var4 = '5'
print("Hello its %s %s", (var, var1))  # here it will cause error for this specifier to works there is other syntax
print("Hello its %s %s" % (var, var1))  # proper syntax

print('Hello %c it\'s %c pm' % (var3, var4))

i = 1345
print('The number is %d' % i)
print('This number is %i' % i)

#  We can also specify formatting symbols. The only change is using a colon (:) instead of %. For example,
#  instead of %s use {:s} and instead of %d use (:d}

# print('It cost around {0:f} dollar to buy {}' .format(124, 'this parrot'))
# the above code will give error as if we manually assign index than we have to do it for all

print('It cost around {0:f} dollar to buy {1}' .format(124, 'this parrot'))
print('It cost around {0:.3f} dollar to buy {1}' .format(124.46583, 'this parrot'))
print("The {0} of 102 is {1:b}".format('binary', 102))
print("The {0} of 102 is {1:o}".format('octal', 102))
print("The {0} of 1023 is {1:x}".format('hexadecimal', 1023))
print("The {0} of 1023 is {1:X}".format('hexadecimal', 1023))

# print('It cost around {0:d} dollar to buy {1}' .format(124.46583, 'this parrot'))  this will give an error

print('It cost around {0:.0f} dollar to buy {1}' .format(124.46583, 'this parrot'))  # to avoid the above error

#  generating spaces with format()

print("This is a normal {0:10} text".format('p'))
print("This is a normal {0:^10} text".format('p'))
print("This is a normal {0:<10} text".format('p'))
print("This is a normal {0:>10} text".format('p'))
print("This is a normal {0:*^10} text".format('p'))
print("This is a normal {0:#<10} text".format('p'))

# format() with dictionaries

dic = {
    'first_name': 'Salman',
    'middle_name': 'Ali',
    'last_name': 'Zaidi'
}

message = 'My name is {first_name} {middle_name} {last_name}'
print(message.format(**dic))

list1 = [1, 2, 3, 4, 5]

output = ['{:.2f}'.format(val) for val in list1]  # list comprehension used
print(output)


dic1 = {'a': 'Apple', 'b': 'Ball', 'c': 'Carrot'}
print('''A = {a} 
B = {b} 
C = {c}'''.format_map(dic1))  # Python String format_map() method is an inbuilt function in Python, which is used to
# return a dictionary key’s value.

message = 'This is a string, as it must be written in single or double quote: '

print(message.index('string'))  # this function tells at which index the search string/character exist

print(message.index('a', 10, 20))  # it also takes start and end point to search within

print("isalnum()")
str1 = 'num1234'
print(str1.isalnum())  # check whether a string is alphanumeric or not
str1 = 'num 123'
print(str1.isalnum())

print("isalpha()")
str1 = 'Salman'
print(str1.isalpha())
str1 = 'salman1234'
print(str1.isalpha())  # checks if all characters in the string are alphabets,
str1 = 'salman 1234'
print(str1.isalpha())

print("isdecimal()")
str1 = '12345'
print(str1.isdecimal())  # checks if all characters in the string are decimal/numbers
str1 = 'salman'
print(str1.isdecimal())
st1 = '123 salman'
print(str1.isdecimal())

print("isdigit()")
str1 = '12345'
print(str1.isdigit())
str1 = 'BCD'
print(str1.isdigit())
print("ss")

new_string = ""
count = 0
b = chr(44)  # chr() takes one integer argument and returns a string at that ascii value
print(b)
for value in range(55):
    b = chr(value)
    if b.isdigit() == True:
        count += 1
        new_string += b

print(count)
print(new_string)


str1 = 'name_1234'
print(str1.isidentifier())
str1 = '1234_name'
print(str1.isidentifier())
str1 = '_name'
print(str1.isidentifier())

print("islower()")
str1 = 'salman'
print(str1.islower())

str1 = 'salMan'
print(str1.islower())

print('isnumeric()')
str1 = '123456'
print(str1.isnumeric())
str1 = '1234dsd56983'
print(str1.isnumeric())


list2 = ['1', '2', '3', '4']
str2 = '-'
print(str2.join(list2))
str2 = '-'
list2 = ['salman', 'ali', 'zaidi']  # this function simply concatenate different strings
print(str2.join(list2))
list2 = ['a', 'l', 'i']
print(''.join(list2))

message = "This is python programming, python is very advance, python is very simple: "

print(message.partition('is'))  # this separates the string from the given arguments and returns a tuple

print(message.replace('python', 'C++'))

print(message.replace('python', 'C++', 2))



