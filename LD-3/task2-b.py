import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np


def U(start, end, x):
    """
    Calculates U value for hermite spline
    :param start: Interval start
    :param end: Interval end
    :param x: Current x
    :return: Calculated U for given x
    """
    return (1 - 2 * (1 / (start - end)) * (x - start)) * ((x - end) / (start - end)) ** 2


def V(start, end, x):
    """
    Calculates V value for hermite spline
    :param start: Interval start
    :param end: Interval end
    :param x: Current x
    :return: Calculated V for given x
    """
    return (x - start) * ((x - end) / (start - end)) ** 2


def hermite_interpolation_spline(range_x, range_y):
    """
    Calculates hermite interpolation spline function
    :param range_x: All x values
    :param range_y: All y values
    :return: Hermite interpolation spline function
    """
    range_dy = points_slopes(range_x, range_y)

    def spline_function(x):
        index = np.searchsorted(range_x, x)
        return U(range_x[index - 1], range_x[index], x) * range_y[index - 1] + V(range_x[index - 1], range_x[index],
                                                                                 x) * range_dy[index - 1] \
               + U(range_x[index], range_x[index - 1], x) * range_y[index] \
               + V(range_x[index], range_x[index - 1], x) * range_dy[index]

    return spline_function





def points_slopes(range_x, range_y):
    """
    Calculates slopes for each interval between given points
    :param range_x: x values
    :param range_y: y values
    :return: Slopes array
    """

    slopes = []
    for i in range(len(range_x) - 1):
        slopes.append(slope(range_x[i], range_y[i], range_x[i + 1], range_y[i + 1]))

    slopes.append(slopes[-1])
    return slopes


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
