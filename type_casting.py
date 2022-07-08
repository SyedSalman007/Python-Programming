# implicit casting

a = 13
print(type(a))

b = 3.0
print(type(b))

c = a * b
print(c, type(c))

d = a + b
print(d, type(d))

# explicit casting

e = b
print('That\'s e type', type(e))
e = int(a)
print('That\'s e type now', type(e))
e = str(a)
print('And that\'s e type now', type(e))

print("****************")

e = a
print('That\'s e type', type(e))
e = float(a)
print('That\'s e type now', type(e))
e = str(a)
print('And that\'s e type now', type(e))

print("****************")

s = '5'
print('That\'s s type', type(s))
s = int(s)
print('That\'s s type now', type(s))
s = float(s)
print('And that\'s s type now', type(s))

print("Conversion from complex")

f = 2 + 3j
print(f, type(f))
#  g = int(f)  *** here this code give error as complex cannot be converted into int or float
g = str(f)
print(g, type(g))  # but the complex and the type cast to string

h = complex(g)
print(h, type(h))

j = 'Salman'
print(j)
# i = int(j)  *** as str can be type cast to int or float but only if it is a numeric string


