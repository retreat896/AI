
import matplotlib.pyplot as plt
import numpy as np
import random

# Objective function
def objective(x):
    return -x**2 + 5


x = np.linspace(-3, 3, 100)
y = objective(x)
start = random.uniform(-3, 3)
solution = objective(start)

plt.plot(x, y, label='Objective Function')
# Final solution point

plt.scatter([start], [solution], color='green', label='Start Point', zorder=6)

plt.title('Hill Climbing Example')
plt.legend()
plt.show()
