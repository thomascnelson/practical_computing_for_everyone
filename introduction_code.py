# compute the density of the sun
# set initial values for variables
pounds = 4.385e30
kgs = pounds/2.2

# the print function
print("The mass in kg is:", kgs)

# importing something
import math
pi = math.pi
print(pi)

# current radius
radius = 696000

# doing math
volume = 4/3 * pi * radius**3
print(volume)

# current density of the sun
density = kgs / volume
print(density)

# changing variables
# density of the sun when it goes white dwarf
radius = 7500
volume = 4/3 * pi * radius**3
density = kgs / volume
print(density)

