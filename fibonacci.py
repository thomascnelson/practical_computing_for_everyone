# function to compute the Fibonacci sequence 
# given the number of iterations n
# Returns a list
def fibonacci(iterations):
    fib_sequence = []
    a = 0
    b = 1
    for i in range(iterations):
        fib_sequence.append(a)
        c = a + b
        a = b
        b = c
    return fib_sequence

sequence = fibonacci(20)
print(sequence)
print(sum(sequence))



