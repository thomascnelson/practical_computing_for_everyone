# Python uses dynamic variable typing
temperature = 32
type(temperature)

temperature = 32.1
type(temperature)

# lists and dictionaries are important
list_of_temperatures = [5, 10, 15, 20]
print(list_of_temperatures)
type(list_of_temperatures)
parameter_dictionary = {'temperature':32, 'velocity':10, 'method':'USWS'}
print(parameter_dictionary['method'])
type(parameter_dictionary)


# creating initial values for our computation
temperature = 32
velocity = 10
print(temperature)
print(velocity)
print("The current temperature is", temperature, "degrees Farenheit")

# introduction to Python errors - Name Error
temerature + velocity

# using Python as a super calculator
35.74+0.6215*temperature-35.75*velocity**0.16+0.4275*temperature*velocity**0.16


# computing wind chill
temperature = 32
velocity = 10
wind_chill = 35.74 + 0.6215*temperature -35.75*velocity**0.16 + 0.4275*temperature*velocity**0.16
print("The wind chill factor when the temperature is", 
      temperature, 
      "degrees and the wind velocity is", 
      velocity, 
      "is", 
      wind_chill)


# lots of built-in functions
# how to call a funtion
round(wind_chill, 2)

# using a function call as a parameter in another function
print("The wind chill factor when the temperature is", 
      temperature, 
      "degrees and the wind velocity is", 
      velocity, 
      "is", 
      round(wind_chill, 2))


# creating our own function
# passing function arguments (parameters)
def wind_chill(temperature, velocity):
    return round(35.74 + 0.6215*temperature -\
                 35.75*velocity**0.16 +\
                 0.4275*temperature*velocity**0.16,
                 2)

# using it
wind_chill(32, 10)


# adding flow control - using logic - if statement
# demonstrating code indentation
# using / to wrap around text in one line
# setting a default argument value
def wind_chill(temperature, velocity, metric=False):
    if metric == True:
        print('Metric')
        return round(13.12 + 0.6215*temperature -\
                     11.37*velocity**0.16 +\
                     0.3965*temperature* \
                     velocity**0.16, 2)
    else:
        print('Not metric')
        return round(35.74 + 0.6215*temperature -\
                     35.75*velocity**0.16 +\
                     0.4275*temperature* \
                     velocity**0.16, 2)

wind_chill(temperature=10, velocity=10, metric=True)


# smilifying the code
def wind_chill(temperature, velocity, metric=False):
    if metric:
        return round(13.12 + 0.6215*temperature -\
                     11.37*velocity**0.16 +\
                     0.3965*temperature* \
                     velocity**0.16, 2)
    return round(35.74 + 0.6215*temperature -\
                 35.75*velocity**0.16 +\
                 0.4275*temperature* \
                 velocity**0.16, 2)


# overriding a default parameter
wind_chill(temperature=10, velocity=10, metric=True)
wind_chill(temperature=10, velocity=10)


# if - else statements
velocity = 80
if velocity > 74:
    print("Wow, it is a hurricane!")
else:
    print("It is not a hurricane.")


# boolean logic
0 == False
1 == True
1 == False
0 == True

if 'foo':
    print('True')
else:
    print('False')

if 0:
    print('True')
else:
    print('False')


# our final prototype
def wind_chill(temperature, velocity, metric=False):
    if metric:
        return round(13.12 + 0.6215*temperature - 11.37*velocity**0.16 + 0.3965*temperature*velocity**0.16, 2)
    return round(35.74 + 0.6215*temperature - 35.75*velocity**0.16 + 0.4275*temperature*velocity**0.16, 2)

wind_chill(temperature=10, velocity=10, metric=True)


# Python lists are useful
my_list = [1, 2, 3, 4, 5]
my_list
type(my_list)
len(my_list)
my_list[0]
my_list[:3]
my_list[3:]
my_list[1:4]
my_list.extend([9,10,11])
my_list
my_list.append(['a','b','c'])
my_list
my_list[-1]
my_list[-1][0]
my_list[-1]
my_list.reverse()
my_list
my_list = [1,2,3]
my_list


# iterating over something with for loops
for item in my_list:
    print(item)

# the range() function
for x in range(5):
    print(x)

# the len() function
for x in range(len(my_list)):
    print(my_list[x])

# using logic within loops
for x in range(10):
    if (x == 1):
        continue
    if (x > 5):
        break
    print(x)


# phase 2 - using lists to compute lots at once
def wind_chill(temperature, velocity, metric=False):
    if metric:
        return round(13.12 + 0.6215*temperature - 11.37*velocity**0.16 + 0.3965*temperature*velocity**0.16, 2)
    return round(35.74 + 0.6215*temperature - 35.75*velocity**0.16 + 0.4275*temperature*velocity**0.16, 2)

temperature_list = [5,10,15,20,25,30,35,40]
velocity_list = [5,10,15,20,25,30,35,40]

for temp in temperature_list:
    print(wind_chill(temperature=temp, velocity=10, metric=False))


# nesting for loops
for temp in temperature_list:
    for vel in velocity_list:
        print(wind_chill(temperature=temp, velocity=vel, metric=False))

# storing the output in a list of lists
table = []
for temp in temperature_list:
    row = []
    for vel in velocity_list:
        row.append(wind_chill(temperature=temp, velocity=vel, metric=False))
    table.append(row)
table


# Pandas is a must know package
import pandas as pd
wind_chill_table = pd.DataFrame(table)
wind_chill_table

# manipulating data frames
wind_chill_table.index = temperature_list
wind_chill_table.columns = velocity_list
wind_chill_table.columns.name = "Velocity"
wind_chill_table.index.name = "Temperature"

wind_chill_table

# buil-in functions of data frames
wind_chill_table.head()
wind_chill_table.tail()
wind_chill_table.shape
wind_chill_table.size

# slicing df's
wind_chill_table[20]
wind_chill_table[20][1:4]
wind_chill_table[20][20]
wind_chill_table[[15, 20]][2:4]

# more functions
wind_chill_table.max()


# using a dictionary to create a data frame
# here is our dictionary - demonstrating comments
data = {'Employee':['Thomas', 'Ellen', 'Emily'], 'Salary':[75000, 100000, 85000]}
data['Employee']
data['Salary']

import pandas as pd
df = pd.DataFrame(data)
df
df.shape
df.size
len(df)
df.columns
df['Employee']
df.Salary
df['Employee'][:2]
df.Salary[1]
df['Age'] = ['58','44','29']
df
df.loc[:,'Age']
df.iloc[1]
df.iloc[1]['Employee']
df.loc[:,'Salary'].max()
df.loc[:,'Salary'].mean()



# function to compute wind chill given the temperature, 
# wind veocity, and specify if metric or not 
def wind_chill(temperature, velocity, metric=False):
    if metric:
        return round(13.12 + 0.6215*temperature -\
                     11.37*velocity**0.16 +\
                     0.3965*temperature*velocity**0.16, 2)
    return round(35.74 + 0.6215*temperature -\
                 35.75*velocity**0.16 +\
                 0.4275*temperature*velocity**0.16, 2)

# specify a rage of temperatures and velocities for which to make our table
temperature_list = [5,10,15,20,25,30,35,40]
velocity_list = [5,10,15,20,25,30,35,40]

# create our table of values using nested looping
table = []
for temp in temperature_list:
    row = []
    for vel in velocity_list:
        row.append(wind_chill(temperature=temp, velocity=vel, metric=False))
    table.append(row)

# make our table a Pandas data frame
import pandas as pd
wind_chill_table = pd.DataFrame(table)

print(wind_chill_table)


# change the index and column names
wind_chill_table.index = temperature_list
wind_chill_table.columns = velocity_list
wind_chill_table


# giving names
wind_chill_table.columns.name = "Velocity"
wind_chill_table.index.name = "Temperature"
wind_chill_table

# look at a specific temp series
wind_chill_table.loc[20]

# series
print(type(wind_chill_table.loc[20]))
list(wind_chill_table.loc[20])

# series to list
twenty_degrees = list(wind_chill_table.loc[20])

# insert the 0 wind value
twenty_degrees.insert(0, 20)
twenty_degrees


# plotting with matplotlib
import matplotlib.pyplot as plt
plt.plot(twenty_degrees)

# making it pretty
x_axis_values = list(wind_chill_table.columns)
x_axis_values.insert(0, 0)
x_axis_values
plt.plot(x_axis_values, twenty_degrees)

# even more pretty
import matplotlib.pyplot as plt
plt.plot(x_axis_values, twenty_degrees)
plt.title("Wind chill as a function of wind velocity at 20 degrees")
plt.xlabel("Wind velocity")
plt.ylabel("Wind chill")

