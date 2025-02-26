import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Objective function
def objective(x):
    return -x**2 + 5

# Hill Climbing with real-time plotting
def hill_climb(start, steps=200, step_size=0.2):
    current = start
    points = [current]  # Store points to plot
    for _ in range(steps):
        neighbor = current + random.uniform(-step_size, step_size)
        if objective(neighbor) > objective(current):
            current = neighbor
            points.append(current)
    return points

# Prepare data
x = np.linspace(-3, 3, 100)
y = objective(x)
start = random.uniform(-3, 3)
points = hill_climb(start)

# Plot setup
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Objective Function', color='blue')
plt.scatter([start], [objective(start)], color='green', label='Start Point', zorder=5)
plt.title('Hill Climbing Visualization (Step-by-Step)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend()
plt.grid(True)

# Plot each point with a 0.5-second interval
for point in points:
    plt.scatter([point], [objective(point)], color='red', zorder=5)
    plt.pause(0.5)  # Pause for 0.5 seconds between points

# Final solution point
solution = points[-1]
plt.scatter([solution], [objective(solution)], color='black', label='Final Solution', zorder=6)
plt.legend()
plt.show()

