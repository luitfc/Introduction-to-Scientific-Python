from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

"""
    solve the second-order ODE y’’ + y’ + y = cos(x), y(0) = y’(0) = 0 over 0 to 20, and plot the numerical solution
"""


def dYdx(Y, x):
    # Here Y is a vector containing two elements: Y[0] = y1, Y[1] = y2
    return [Y[1], np.cos(x) - Y[0] - Y[1]]


U0 = [0, 0]
xs = np.linspace(0, 20, 200)
Us = integrate.odeint(dYdx, U0, xs)
ys = Us[:, 0]

# plot
fig, ax = plt.subplots()
ax.plot(xs, ys)
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y(x)', fontsize=11)
plt.show()
