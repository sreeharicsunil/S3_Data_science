import numpy as np
import matplotlib.pyplot as plt

# Scores
y1 = [22, 30, 35, 35, 26]   # Men
y2 = [25, 32, 30, 35, 29]   # Women

# X-axis labels
x_labels = ['G1', 'G2', 'G3', 'G4', 'G5']
x1 = np.arange(5)

width = 0.40

# Bar plots
plt.bar(x1 - 0.2, y1, color='green', width=width, label='Men')
plt.bar(x1 + 0.2, y2, color='red', width=width, label='Women')

# Labels
plt.xticks(x1, x_labels)
plt.xlabel('Person')
plt.ylabel('Scores')

# Legend and title
plt.legend()
plt.title('Scores by Group and Gender')

plt.show()