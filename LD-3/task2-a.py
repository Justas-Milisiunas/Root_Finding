from interpolation import f, newton_interpolation_f, np, chebyshev_range
import matplotlib.pyplot as plt

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [10.5617, 11.1504, 14.4338, 16.9788, 21.0081, 24.7199, 28.526, 27.9448, 25.7463, 23.1029, 16.7226, 11.5084]

# Made interpolation function
interpol_f = newton_interpolation_f(x_range, y_range)

# X and Y values calculation
# range_x = np.arange(1, 12, 12/n)
range_x = chebyshev_range(100, 1, 12)
range_y = [interpol_f(_x) for _x in range_x]

# Shows f(x) and interpolation graphs
plt.scatter(x_range, y_range, label='Month`s temp. avg.')
plt.plot(range_x, range_y, 'r', label='Temp. interpolation')

plt.xticks(x_range)
plt.xlabel('Month')
plt.ylabel('Temp. avg.')

plt.grid(True)
plt.legend()
plt.show()
