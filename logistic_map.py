### Modeling population growth with the logistic map

import matplotlib.pyplot as plt

# r is the growth rate
# p is population as a fraction of the max population
# n is the number of iterations to run in the simulation

# function to compute system state for n time points
def logistic_map(r, p, n):
    state = []                     # result at each time point
    for i in range(n):
        state.append(p)
        p = r*p * (1-p)            # the logistic equation
    return state

# a system with a fixed point attractor
r = 1.8
p = 0.2
n = 50
y = logistic_map(r, p, n)
x = list(range(n))
plt.plot(x, y, marker="o", label="r = 1.8")
plt.ylim(0, 1)
plt.title("Effect of r on system behavior")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()

# a system with a periodic attractor
r = 3.2
p = 0.2
n = 50
y = logistic_map(r, p, n)
x = list(range(n))
plt.plot(x, y, marker="o", label="r = 3.2")
plt.ylim(0, 1)
plt.title("Effect of r on system behavior")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()

# an aperiodic system (strange attractor)
r = 3.8
p = 0.2
n = 50
y = logistic_map(r, p, n)
x = list(range(n))
plt.plot(x, y, marker="o", label="r = 3.8")
plt.ylim(0, 1)
plt.title("Effect of r on system behavior")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()


# plot differnt types of system in one chart
p = 0.2
n = 30

r = 2.5
y1 = logistic_map(r, p, n)
x = list(range(n))

r = 3.2
y2 = logistic_map(r, p, n)

r = 3.8
y3 = logistic_map(r, p, n)

plt.plot(x, y1, marker="o", color='green', label="r=2.5 Fixed Point Attractor")
plt.plot(x, y2, marker="o", color='blue', label="r=3.2 Periodic Attractor")
plt.plot(x, y3, marker="o", color='red', label="r=3.8 Strange Attractor")
plt.ylim(0, 1)
plt.title("Effect of r on system behavior")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()


### Demonstration of sensitive dependence on initial conditions

# create 2 systems and plot on top of each other
# vary the starting poplation by just a tiny amount
# keep everything else exactly the same

r = 3.8
n = 30

# system 1
p1 = 0.20000
y1 = logistic_map(r, p1, n)
x = list(range(n))

# system 2 - same r and n
p2 = 0.20001
y2 = logistic_map(r, p2, n)

plt.plot(x, y1, marker="o", color="blue", label="p=0.20000")
plt.plot(x, y2, marker="x", color="red", label="p=0.20001")
plt.ylim(0, 1)
plt.title("Sensitive dependence on initial conditions")
plt.xlabel("Time Step")
plt.ylabel("Population")
plt.legend()


### The Lyapunov time
# where do the 2 orbits diverge by more than 10%?
for idx, element in enumerate(zip(y1, y2)):
    ratio = (abs(min(element)/max(element)))
    print(ratio)
    if ratio < 0.90:
        print("The Lyapunov time is: ", idx)
        break

