import numpy as np


def f(x):
    """
    Function given by task
    :param x: x value
    :return: y value
    """
    return (np.log(x) / (np.sin(2 * x) + 1.5)) - (x / 7)


def chebyshev_range(count, start, end):
    """
    Calculates x range values using chebyshev polynomial formula
    :param count: Points count
    :param start: x range start
    :param end: x range end
    :return: Calculated x values array
    """
    range_x = []
    for i in range(count):
        temp = (end + start) / 2 + (end - start) / 2 * np.cos((2 * i + 1) * np.pi / (2 * count))
        range_x.append(temp)

    return range_x


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


def akima_points_derivative(range_x, range_y):
    """
    TODO: not working
    Calculates each point slope
    Source: https://en.wikipedia.org/wiki/Akima_spline
    :param range_x: x range values array
    :param range_y: y range values array
    :return: each point calculated slope values array
    """

    def m(index):
        """
        Slope of the line segment calculation (from wiki source)
        :param index: Point index
        :return: Calculated slope of the line segment
        """
        return (range_y[index + 1] - range_y[index]) / (range_x[index + 1] - range_x[index])

    range_s = []
    for i in range(2, len(range_x) - 2):
        range_s.append((np.abs(m(i + 1) - m(i)) * m(i - 1) + np.abs(m(i - 1) - m(i - 2)) * m(i)) / (
                np.abs(m(i + 1) - m(i)) + np.abs(m(i - 1) - m(i - 2))))

    return range_s
