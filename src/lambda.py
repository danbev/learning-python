import dis

#s is a bound variable parameter
l = lambda s: print(s)
l(10)
print(type(l))
dis.dis(l)
print(l)

# applying without binding to a local variable first
# Immediately Invoked Function Expression (IIFE) ("iffy")
(lambda s: print(s))("something")

two_args = lambda s, s2: print(s, s2)
two_args("first", "second")


