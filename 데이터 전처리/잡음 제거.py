import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.cos(x) + np.random.random(100)

from scipy.signal import savgol_filter
y_filtered = savgol_filter(y, 99, 3)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.subplots()
p = ax.plot(x, y, "o")
p, = ax.plot(x,y_filtered, "g")
plt.subplots_adjust(bottom=0.25)
