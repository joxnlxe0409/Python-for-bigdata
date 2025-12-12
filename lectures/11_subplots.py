import matplotlib.pyplot as plt

# Create a 2x2 grid of subplots
fig, ax = plt.subplots(2, 2, figsize=(5, 5))

# Plot data on each subplot
ax[0, 0].plot(range(10), 'r')  # Red line
ax[1, 0].plot(range(10), 'b')  # Blue line
ax[0, 1].plot(range(10), 'g')  # Green line
ax[1, 1].plot(range(10), 'k')  # Black line

# Show the plot
plt.show()

