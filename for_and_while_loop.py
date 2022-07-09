#
#
# # while loop
#
# # for loop takes a certain amount of collection and its block is repeated once for each item in the collection, whereas
# # while loop is excuted till a certain value\condition is not achieved
#
# num = 1
# while num <= 5:  # as soon as the condition turns false the loop ends
#     print(num)
#     num += 1
#
# #  letting the user end the loop
#
# prompt = 'Tell me something and i will repeat it back, also to close the program type \'quit\': '
#
# message = ""  # input(prompt)
#
# while message.lower() != 'quit':
#     if message != 'quit':
#         print(message)
#     message = input(prompt)
#
# # using a flag
#
# # flag is a variable that determines whether the program is active, it acts as a signal to the program
#
# flag = True
# #  this code is also much more optimize than the previous as it checks only one validation
# while flag:
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     else:
#         flag = False

#  break statement is used to exit block of code when we don't want the remaining line to execute
active = active2 = True
while active:
    while active2:
        print("Its about to break")
        active = False
        break
    print("Salman")

#  the above code clearly show that break keyword exits the pointer from a single block


# continue is another keyword used in loops to skip the remaining lines of codes that are not important to execute

# as breaks exits from the block, continue returns to the beginning of the loop
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

#  loop and list

unconfirmed_user = ['salman', 'ali', 'zaidi']
confirmed_user = []

#  empty list will always return a boolean value of false

while unconfirmed_user:
    user = unconfirmed_user.pop()
    print(f"Verifying the user : {user.title()}")
    confirmed_user.append(user)

print("Verified user are :")
for value in confirmed_user:
    print(value)

#  removing specific values from a list using loops

list1 = ['ali', 'zaidi', 'syed', 'ali', 'ali', 'salman', 'ali']
print(list1)
while 'ali' in list1:
    list1.remove('ali')
print(list1)
# using for loop
list2 = ['ali', 'zaidi', 'syed', 'ali', 'ali', 'salman', 'ali']
print(list2)
for value in list2:
    list2.remove('ali')
print(list2)

# loop and dictionaries
# dic = {}
flag = True
# while flag:
#     prompt = "Enter your name: "
#     prompt1 = 'Enter the country you were born in: '
#     prompt2 = 'To exit enter quit: '
#     key = input(prompt)
#     value = input(prompt1)
#     dic[key] = value
#     print(dic)
#     message = input(prompt2)
#     if message.lower() == 'quit':
#         flag = False

#  If the loop doesn't work or when the condition of the loop turns false the else block will execute

y = False
while y:
    print('Salman')
else:  # loop else block
    print('zaidi')

# *****   pass   *****

# pass does nothing at all: it’s an empty statement placeholder.
# pass statement is generally written when the coder doesn't know what to code in a function etc
# ellipses ( ... ) they also do nothing in the code, and they can also appear on the same line as a statement header
# and may be used to initialize variable names if no specific type is required:

t = ...

a = 10
b = 5

if b > a:
    pass
else:
    print("a>b")

list3 = ['a', 'b', 'c', 'd']

for value in list3:
    if value == 'a':
        pass
    else:
        print(value)

# loop else

y = 57
x = y // 2
while x > 1:
    if y % x == 0:
        print(f"{y} is a factor of : {x}")
        # break  # if this break is omitted that else condition will be executed as soon as the condition of the while
        # loop becomes false
    x -= 1
else:
    print(f"{y} is a prime number ")

#  here the else block provides a great advantage and that is that if the while loop doesn't reach to any factor that
# divisible than it's going to be a prime number that is mentioned in else block
#  by using else block we didn't need to add an if condition within a loop that had been executed in every repetition

# without else block
y = 57
x = y // 2
while x > 1:
    if y % x == 0:
        flag1 = 1
        break
    else:
        flag1 = 0
    x -= 1

if flag1 == 0:
    print(f"{y} is a prime number")
else:
    print(f"{y} is not a prime number it is divisible by {x}")

list1 = ['ali', 'salman', 'zaidi', 'abid', 'mustafa', 'taha', 'hassan']
flag2 = False
while list1:  # and not flag2:
    if 'salman' in list1:
        print("this list contain it")
        break
        # flag2 = True
    else:
        print("this list does not contain it")
else:  # if flag2:
    print('this flag is true')

# here we can see that we can use else block after the loop

for v in ['salman', 'ali', 'zaidi']:
    print(v)

for v in list1:
    print(v)
#sum1 = ...  # if I will declare this variable in this way it will
sum1 = 0
# give an error 'unsupported operand type(s) for +: 'ellipsis' and 'int' '
for v in [1, 2, 3, 4, 5]:
    sum1 = sum1 + v  # if i will perform this function without declaring the variable separately then it will bean error
print(sum1)

# for loop and also be applied on string

for v in 'SALMAN': print(v)

tupl = ('hello', 'it\'s', 'me')

for v in tupl: print(v, end=' ')

T= [(1, 2), (3, 4), (5, 6), (7, 8)]
list4 = []
for (a, b) in T:  # as in the list the elements are tuples, so we have to set the elements and the same way
    print(a, b)
    list4.append(a)
    list4.append(b)
print(list4)

dic = {'Name': 'Salman', 'City': 'Karachi', 'Father': 'Hashim'}

for att in dic:  # if we just right dictionary name don't use .items() then only the keyword will be assigned to att
    print(att, " => ", dic[att])
print("Different way")

for att, val in dic.items():
    print(att, " => ", val)

list5 = []
#  copy dictionary in a list
for att, val in dic.items():
    list5.append(att)
    list5.append(val)
print(list5)


print("\n")
for both in T:
    a, b = both
    print(a, b)

a, *b, c = (1, 2, 3, 4, 5, 6, 7)
print(a, b, c)

# the above assignment is manually done as

p = (1, 2, 3, 4, 5, 6, 7)

a, b, c = p[0], p[1], p[2:]
print(a, b, c)

