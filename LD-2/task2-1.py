from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# https://matplotlib.org/3.1.0/gallery/mplot3d/surface3d.html
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.contour.html


X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
XX, YY = np.meshgrid(X, Y)

Z1 = XX ** 2 + 10 * (np.sin(XX) + np.cos(YY)) ** 2 - 10
Z2 = (YY - 3) ** 2 + XX - 8

fig = plt.figure()
fig.canvas.set_window_title('Z1')
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX, YY, Z1, cmap=cm.coolwarm,
                       alpha=0.5)
surfZ = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
cp = ax.contour(X, Y, Z1, levels=0, colors='red')
plt.show()

fig = plt.figure()
fig.canvas.set_window_title('Z2')
ax = fig.gca(projection='3d')
surf = ax.plot_surface(XX, YY, Z2, cmap=cm.summer,
                       antialiased=False, alpha=0.5)
surfZ = ax.plot_surface(XX, YY, np.zeros(np.shape(Z1)), antialiased=False, alpha=0.2)
cp = ax.contour(X, Y, Z2, levels=0, colors='green')
plt.show()

fig = plt.figure()
fig.canvas.set_window_title('Result')
ax = fig.gca()
ax.grid(color='#C0C0C0', linestyle='-', linewidth=0.5)
cp = ax.contour(X, Y, Z1, levels=0, colors='red')
cp = ax.contour(X, Y, Z2, levels=0, colors='green')
plt.show()
