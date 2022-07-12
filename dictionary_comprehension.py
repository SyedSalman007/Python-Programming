# dictionary comprehension syntax is :
# {key: value for (key, value) in iterable}

list1 = ['name', 'class', 'city', 'country']
list2 = ['salman', '2nd year', 'karachi', 'pakistan']

dic = {k: v for (k, v) in zip(list1, list2)}  # dictionary comprehension
print(dic)

dic1 = {k: k**2 for k in range(1, 11)}
print(dic1)

dic2 = {k.title(): k*3 for k in 'coding'}  # variable can also be
print(dic2)



