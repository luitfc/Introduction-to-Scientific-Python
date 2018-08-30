from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x_raw = np.linspace(0, 2*np.pi, 10)
y_raw = np.sin(x_raw**(2/3))

linear = interpolate.interp1d(x_raw, y_raw)  # linear interpolation
cubic = interpolate.interp1d(x_raw, y_raw, kind='cubic')  # cubic interpolation
x_new = np.linspace(0, 2*np.pi, 50)

fig, ax = plt.subplots()
ax.plot(x_raw, y_raw, '*', label='Raw')
ax.plot(x_new, linear(x_new), '-', linewidth=0.6, label='Linear')
ax.plot(x_new, cubic(x_new), '--', linewidth=0.6, label='Cubic')
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y(x)', fontsize=11)
ax.legend()
plt.show()