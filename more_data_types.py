# boolean
type(True)
type(False)
bool(0)
bool(1)

# integers
x = 5
type(x)
0b1010  # Integer (base  2: binary)
0o12    # Integer (base  8: octal)
10      # Integer (base 10: decimal)
0x0a    # Integer (base 16: hexadecimal)

# floats
x = 10.0
type(x)
j = 10.
type(j)
1e1          # Float (scientic notation)

# comples numbers
complex(0)
10 + 0j      # Complex

# constants
float('inf') # Infinity as a float
float('nan') # Not a number as a float (undefined)
import math
math.pi      # the constant pi
math.e       # the constant e

# be careful with numerical precision and rounding
0.1 * 3
(0.1 * 3) == 0.3
1e400

# tuples
my_tuple = 1,2,3
type(my_tuple)
type((4,5,6))

# sets
type({1,2,3})
my_list = [1,2,2,2,3,4,5,5,5,6]
my_list
set(my_list)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set1.intersection(set2)
set1.union(set2)
set1.symmetric_difference(set2)

# strings
"Hello, world!"
type("Hello, world!")
"Hello, world!" + " " + "Nice to see you!"
"Hello, world!"[1]
"Hello, world!"[7:-1]
"Hello, world!".upper()


