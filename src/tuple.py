t1 = 'one', 'two'
print(t1)
t2 = ('one', 'two')
print(t2)

b = {}
bigram = ('a', 'b')
# The get method of a dictionary will return the value of the key if it exists,
# otherwise it will return the default value, which in this case is 0.
b[bigram] = b.get(bigram, 0) + 1
print(b)
