import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """
    Function given by task
    :param x: x value
    :return: y value
    """
    return (np.log(x) / (np.sin(2 * x) + 1.5)) - (x / 7)


def newton_interpolation_coefficients(range_x, range_y):
    """
    Calculates coefficients for newton's interpolation formula
    :param range_x: All x values
    :param range_y: All y values
    :return: Calculated coefficients
    """
    a = [range_y]
    for i in range(len(range_x)):
        a.append([])
        for j in range(1, len(range_x) - i):
            a[i + 1].append((a[i][j] - a[i][j - 1]) / (
                    range_x[np.min([i + j, len(range_x) - 1])] - range_x[np.max([i + j - (i + 1), 0])]))

    return [_a[0] for _a in a[:-1]]


def newton_interpolation_f(range_x, range_y):
    """
    Makes interpolation function
    :param range_x: all x values
    :param range_y: all y values
    :return: Interpolation function
    """
    a_coefficients = newton_interpolation_coefficients(range_x, range_y)

    def interpolation_f(_x):
        """
        Calculates y value from the newton's interpolation function
        :param _x: x value
        :return: y value
        """
        ff = a_coefficients[0]
        tmp = 1
        for ii in range(1, len(a_coefficients)):
            tmp *= (_x - range_x[ii - 1])
            ff += a_coefficients[ii] * tmp

        return ff

    return interpolation_f


# Number of points
n = 30

# Interpolation function range
range_start = 2
range_end = 10
step_size = (range_end - range_start) / n

# X values and Y values calculation
x_range = np.arange(range_start, range_end, step_size)
y_range = [f(x) for x in x_range]

# Made interpolation function
interpol_f = newton_interpolation_f(x_range, y_range)

# Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [f(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.plot(x_range, [interpol_f(x) for x in x_range], 'r', label=f'{n} points interpolation')

plt.legend()
plt.show()
