import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
from interpolation import hermite_interpolation_spline

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [10.5617, 11.1504, 14.4338, 16.9788, 21.0081, 24.7199, 28.526, 27.9448, 25.7463, 23.1029, 16.7226, 11.5084]

interpolation_f = hermite_interpolation_spline(x_range, y_range)

plt.scatter(x_range, y_range, label='Month`s avg. temp')
plt.plot(np.arange(x_range[0], x_range[-1], 0.01),
         [interpolation_f(_x) for _x in np.arange(x_range[0], x_range[-1], 0.01)],
         'r', label='Spline')

plt.xlabel('Month')
plt.ylabel('Temp. avg.')
plt.title('Hermite interpolation spline')

plt.grid(True)
plt.legend()
plt.show()
