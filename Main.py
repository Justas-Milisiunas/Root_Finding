from Window import Window
import matplotlib
from Graph import Graph
import numpy
from matplotlib import style
from NumericalMethods import NumericalMethod

matplotlib.use("TkAgg")
style.use("ggplot")

# 0.16 * x ** 5 - 1.57 * x ** 4 + 4.38 * x ** 3 - 1.15 * x ** 2 - 6.29 * x + 0.15
function = numpy.poly1d([0.16, -1.57, 4.38, -1.15, -6.29, 0.15])
# function = numpy.poly1d([0.15, 1, -0.1])
derivative = function.deriv()

alpha = -50
max_iterations = 1000
precision = 1e20
eps = 1e-4
print(f"Patikrintos x reikšmės {function.roots}")

window = Window(title='Skaitmeniniai algoritmai 12 vr.', size='1250x630')
function_x_values = numpy.arange(-2, 1, 0.0001)
function_y_values = [function(x) for x in function_x_values]

graph = Graph(start_x=function_x_values[0], end_x=function_x_values[-1], frame=window.get_graph_frame())
graph.add_toolbar()
# graph.show_function(function_x_values, function_y_values, 'b', 'f(x)')

methods = NumericalMethod(precision, eps, alpha, max_iterations, function,
                          derivative, function_x_values, graph)

window.add_buttons(methods)

window.start()
