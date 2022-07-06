# exploring basic printing ways and escapes character

print(.4e-7)

print('Salman \' Zaidi')  # as this ' would have caused error in the string but due to the escapes character (\) it
# escapes from that error in the string

print(r'foo\nbar')

print(''' printing double quote " and single ' quote also ''')

print("Salman\aZaidi")

# working with input function

message = input("Your First Name")

print(message)

message = input("Your Last Name")
print(message)

x = str("Salman Zaidi")
y = float(3)
c = 34.98
print(type(c))  # type() function will return the data type of that variable
# print(y)

fruits = ["Salman", "Ali", "Zaidi"]
a, b, c, = fruits  # assigning  the values from the list to 3 variables separately
x = '10'
y = '2'

print(x + y)  # concatenating the strings


def myfunc():
    global x  # global keyword usage
    x = 'salman'
    print(x)


myfunc()  # function calling
print(x)
x = 10
y = 13.56
z = complex(y)

print(z)

import random  # testing the random function

print(random.randrange(1, 10))

#  working on triple quote strings

x = """Salman
Ali Zaidi Currently working in
Sastaticket"""
print(x)

# concatenating string and int/float
age = 20
txt = "Salman Age is {}"
print(txt.format(age))  # here the int value is first converted to string and then concatenated with the string
# format() places the value within these bracket {}

# looping on strings

y = "Syed Salman Zaidi Ali age is 20"
a = 0

for x in "Salman":  # the loops will run on the number of character in that string/words
    print(y[a])
    a = a + 1

# checking the string

print("Salman" in y)
if "salman" in y:
    print("Check completed")
else:
    print("check failed")

print("Salman" not in y)

if "salman" not in y:
    print("Yes")
else:
    print("no")

# slicing the string

x = "Salman Ali"
print(x[2:5])
print(x[:5])
print(x[5:])
print(x[-7:-2])


# some string built-in function


x = "saLman Ali Zaidi"
f = 20
print(x.upper())
print(x.lower())
print(x.strip()) # to remove whitespace from the string we can also use rstrip() (for right whitespace removal) and
# lstrip (for left space removal)s
print(x.replace("s", "Z"))

