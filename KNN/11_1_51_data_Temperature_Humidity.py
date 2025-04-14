
# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# read data
df = pd.read_csv('03_52_dataTemperatureHumidity.csv', delimiter=',')
df.columns=['T','H','Class']

# plot
labels, index = np.unique(df["Class"], return_inverse=True)
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
sc=ax1.scatter(df['T'], df['H'], marker='o', c=index, alpha=1.0, s=100, edgecolor='black')
ax1.legend(sc.legend_elements()[0], labels)
plt.show()