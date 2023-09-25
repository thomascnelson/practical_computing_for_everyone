# variable scope demonstration
# the two x's are in different scopes
def my_function():
    x = 100
    return x

x = 1

print(my_function())
print(x)

