# dictionaries can store almost limitless amount of information

dic = {'color': 'Red', 'Points': '5'}
print(dic)
print(dic['color'])
print(dic['Points'])

# dictionaries in python are based on 'key' and its 'value' like color is a key and Red is the value
# each key have a value but that value can be anything even a dictionaries
# we can place any object as a value created in python
# as in the previous print statement we have provided a key and the value of that key got printed

new_point = dic['Points']
print(f'The points are {new_point}:')

# Adding a new key-value pairs
# Dictionaries are dynamic structures
print(dic)
dic['player'] = 'Salman'
dic['age'] = 20
print(dic)

# dictionaries retain the order in which they were defined

# Empty Dictionaries

dic1 = {}  # syntax to define an empty dictionary

if dic1:
    print("Not an empty dictionary")
else:
    print("An empty dictionary")

dic1['HTML'] = 'Hypertext Markup Language'
dic1['Use'] = 'Mostly for website layout'
print(dic1)

# Modifying values in a dictionaries

print(dic)
dic['color'] = 'Yellow'
print(dic)

player = {'x-axis': 10, 'y-axis': 20, 'name': 'salman', 'speed': 'fast'}

# considering the player is moving in x-axis

print(player)
if player['speed'].lower() == 'slow':
    player['x-axis'] = player['x-axis'] + 1
elif player['speed'].lower() == 'medium':
    player['x-axis'] = player['x-axis'] + 2
else:
    player['x-axis'] = player['x-axis'] + 3
print(player)

# Removing key-value pair

print(dic)
del dic['Points']
print(dic)

# storing similar info of different object in a dictionary

fav_programming = {
    'ali': 'Python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(fav_programming)

# using get() to access the values

# the way of accessing the value by providing the key in square bracket will cause error if that key is does not exist

# print(dic['Points'])  # will give error as before the point key was deleted

# in get() function we assign two values one is the key and second is the default value if the key doesnot exist

point_value = dic.get('Point', "No point keyword available")
print(point_value)
#  by using get() we have omitted an error that can be occurred
point_value = dic.get('player', "No point keyword available")
print(point_value)

#  Looping through Dictionaries

# items() function is necessary when working with loops on dictionary as it returns key-value paired that's the reason
# we have used two variable in loop
for name, language in fav_programming.items():
    print(f"{name.title()} favorite language is {language.title()}")

# looping through all key in dictionaries
# to print all the keys from a dictionaries we use key() function

for name in fav_programming.keys():
    print(name)
#  following code can also be written as
print("Printing exact same value without key()")
for name in fav_programming:
    print(name)

# printing sorted dictionaries

for name, language in sorted(fav_programming.items()):  # here by placing the dictionaries in the sorted() the whole
    # dictionary is printed as sorted
    print(f"{name.title()} favorite language is {language.title()}")

# looping through all value in dictionaries we use value()

for language in fav_programming.values():
    print(language)

# nesting in dictionaries

# we can have a list of dictionaries or a list of items in a dictionary ( imp )

# A list of dictionary

alien_0 = {'color': 'Red', 'points': 10}
alien_1 = {'color': 'Green', 'points': 5}
alien_2 = {'color': 'Blue', 'points': 7}

list1 = [alien_0, alien_1, alien_2]

print(list1)

for value in list1:
    print(value)

alien = []

for value in range(20):
    new = {'color': 'Green', 'Point': 8}
    alien.append(new)
print("Nesting")
for value in alien[3:10]:
    print(value)

for value in alien[:10]:
    if value['color'].lower() == 'green':
        value['color'] = 'Yellow'

print("updating")

for value in alien:
    print(value)

# list in dictionary

dic2 = {
    'Salman': ['Football', 'Throwball'],
    'Ali': ['Badminton', 'Tennis']
}

for name, sports in dic2.items():
    print(f"\n{name} favourite sports are :")
    for sport in sports:
        print(sport)

# Dictionary in a dictionary

student = {
    'salman': {
        'age': 20,
        'class': "3rd Semester",
    },
    'syed': {
        'age': 15,
        'class': "Class 9",
    },
    'ali': {
        'age': 10,
        'class': "Class 6",
    },
    'zaidi': {
        'age': 18,
        'class': "Inter",
    }
}

for name, info in student.items():
    print(name.title())
    for value,value2 in info.items():
        print(f"{value} is = {value2}")


# Question : What if dic have two same key
