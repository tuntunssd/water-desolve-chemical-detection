import matplotlib.pyplot as plt
import numpy as np

# Generate random data for accuracy levels
accuracy_levels = np.random.rand(10) * 100  # 10 random accuracy levels between 0 and 100

# Generate corresponding epochs
epochs = range(1, len(accuracy_levels) + 1)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(epochs, accuracy_levels, marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('Accuracy Level Graph')
plt.xlabel('chamical detection')
plt.ylabel('Accuracy (%)')

# Show grid
plt.grid(True)

# Show the plot
plt.show()



