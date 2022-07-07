# the four major decision control statement in python
# if, if-else, if,nested if, if-elif-else

cars = ['audi', 'toyota', 'subaru', 'bmw']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())  # in the following code only the bmw will be printed in the complete upper case

# conditional test

# the condition in the if statement always returns a ture or a false value and is called as conditional test

# when checking your equality the case of the words are significant


word = 'Hello'
if word == 'hello':  # as this code clearly shows that Hello and hello are not same
    print("Equal")
else:
    print("Not equal")

# if the case of the word doesn't matter, and we just want to check that word is present or not than

if word.lower() == 'hello':  # not the condition will be true
    print("Equal")
else:
    print("Not equal")

requested_toppings = 'mushrooms'

if requested_toppings != 'cheese':
    print('Hold the Cheese')
else:
    print("Cheese would be good")

# numerical comparison

age = int(input('Enter your age :'))  # why I have to add int here to tell the type of input, when i tried doing it
# without int then it gives error

if age >= 18:
    print("You are old enough to drive")
else:
    print("Not eligible to drive")

# checking multiple conditions

if (age >= 20) and (age <= 29):  # the square brackets can be ignored, and it won't cause any error
    print("Your are in our twenties")
elif age > 29:
    print("You are older")
else:
    print("You are young")

# simplifying the previous code

if 20 <= age <= 29:  # work more on simplifying the logical statement
    print("Your are in our twenties")
elif age > 29:
    print("You are older")
else:
    print("You are young")

# checking whether the value is in the list or not

list1 = ['Salman', 'Ali', 'Osama', 'Max', 'Alex']

name = input('Enter your name : ')

for Name in list1:
    if Name.lower() == name.lower():
        print("You are already present in the list")
        a = 0
    else:
        a = 1

if a == 1:
    list1.append(name)
    print("List updated")

# checking if the element is not present in a list

banned_user = ['Max', 'Maaz', 'Affan']

user = 'Affan'

if user not in banned_user:  # here we don't need to run a loop like in C or C++, but here the by doing so the whole
    # list is being checked
    print(f"{user} you can comment on it")
else:
    print(f"{user} you can not comment on it")

# boolean expressions == conditional test (both refers same thing)

print(user == 'Affan')  # here the output will be either true or false as in the print an boolean expression is given

if user == 'someone' or user == 'Affan':
    print("This is how or works if any one statement is ture the whole result will be true")

# using if statement with list

items = ['Brush', 'Hair Dryer', 'Books']

for value in items:
    if value.lower() == 'books':
        print('Sorry we are out of books')
    else:
        print(f"{value.title()} is added to your grocery")

# checking that a list is empty or not

list2 = []

if list2:  # we the following line of codes check whether the list is empty or not and to check the list is a good
    # practice
    print("List is not empty")
else:
    print("List is empty")

items_available = ['Brush', 'Hair Dryer']

if items_available:
    for value in items:
        if value in items_available:
            print(f"{value.title()} is purchased")
        else:
            print(f"Sorry we are not of {value.title()}")
else:
    print("No items available")