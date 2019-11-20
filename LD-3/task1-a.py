from interpolation import f, newton_interpolation_f, np
import matplotlib.pyplot as plt

# Number of points
n = 30

# Interpolation function range
range_start = 2
range_end = 10
step_size = (range_end - range_start) / n

# X and Y values calculation
x_range = np.arange(range_start, range_end, step_size)
y_range = [f(x) for x in x_range]

# Made interpolation function
interpol_f = newton_interpolation_f(x_range, y_range)

# Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [f(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.plot(x_range, [interpol_f(x) for x in x_range], 'r', label=f'{n} points interpolation')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.grid(True)
plt.legend()
plt.show()
