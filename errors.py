# typo - NameError
my_integer = 6
my_intiger + 1

# index out of range - IndexError
my_list = [1,2,3,4,5]
my_list[5]

# key isn't spelled right - KeyError
my_dictionary = {'Name':'Thomas', 'Age':58}
my_dictionary['name']

# TypeError - tuple is immutable
my_tuple = (1,2,3,4,5)
my_tuple[2] = 0

# dealing with errors with try except
try:
   # code that might produce errors
except:
    # when error arises, then this block of code exceutes
    # if not, this block of code doesn't execute

# a common error, division by zero
a = 10
b = 0
a / b

# how to deal with it
a = 10
b = 0
try:
    a / b
except:
    print("Sorry, you can't divide by zero")

