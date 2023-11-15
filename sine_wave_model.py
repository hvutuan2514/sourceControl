import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 5 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# citation: https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/#

