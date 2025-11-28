import matplotlib.pyplot as plt
import numpy as np

years = [1960, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7640]

x_range = range(len(years))

# Adjust positions for each country

plt.bar([x - 0.25 for x in x_range], jp, width = 0.25, label="Japan")
plt.bar(x_range, ko, width = 0.25, label="South Korea")
plt.bar([x + 0.25 for x in x_range], ch, width = 0.25, label="China")

# Labels and title
plt.xlabel('Year')
plt.ylabel('GDP (in billions)')
plt.title('GDP Comparison Over Time')
plt.xticks(x_range, years)

# Adding a legend
plt.legend()

plt.show()
