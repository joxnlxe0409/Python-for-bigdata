import matplotlib.pyplot as plt
import numpy as np

xData = np.arange(20, 50)
yData = xData + 2*np.random.randn(30)

plt.scatter(xData, yData)
plt.title("Real Age, Physical Age")
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.savefig("age.jpg ", dpi = 600)
plt.show()