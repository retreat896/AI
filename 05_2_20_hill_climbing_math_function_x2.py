
import matplotlib.pyplot as plt
import numpy as np
import random

# Objective function
def objective(x):
    return -x**2 + 5

# Hill Climbing
def hill_climb(start, steps=100, step_size=0.1):
    current = start
    for _ in range(steps):
        neighbor = current + random.uniform(-step_size, step_size)
        if objective(neighbor) > objective(current):
            current = neighbor
    return current

x = np.linspace(-3, 3, 100)
y = objective(x)
start = random.uniform(-3, 3)
solution = hill_climb(start)

plt.plot(x, y, label='Objective Function')
plt.scatter([solution], [objective(solution)], color='red', label='Hill Climbing Result')
plt.title('Hill Climbing Example')
plt.legend()
plt.show()
