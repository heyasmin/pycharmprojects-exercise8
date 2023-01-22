#!/usr/bin/python
# the above is a hash bang, this where mac users find python, bin is for binary

# the sys is a python module that can show file path
import sys

# https://docs.python.org/3/library/sys.html?highlight=sys#module-sys
# argument_count is our variable and the len is a built-in function that checks the length.
# argv is a vector -> list of argument (which is a parameter, input)
argument_count = len(sys.argv)

# this is a conditional statement, testing what is in our argument_count.
if argument_count > 1:
    print("Too many args")
else:
    where = 'World'  # create a variable called where and assign the value "World" to it
    print("Hello " + where)  # glue strings together concatenate
    print("Hello", where)  # takes multiple arguments/ parameters/ inputs

print('Goodbye from ' + sys.argv[0])  #this always prints cause it's not part of the conditional
# square brackets are for lists