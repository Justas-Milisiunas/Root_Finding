from Window import Window
from Toolbar import Toolbar
import tkinter
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from Graph import Graph
import matplotlib.lines as mlines
import numpy
import time
from matplotlib import style
from NumericalMethods import NumericalMethod
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("TkAgg")
style.use("ggplot")

# # Simple iteration method
# def show_graph_1():
#     global current_page
#
#     if current_page is not 1:
#         clear_frame(graph_frame)
#
#     # Creates plot for displaying graphs
#     figure = Figure(figsize=(10, 6), dpi=100)
#     # line = mlines.Line2D([0, 0], [10000, 10000], color='red')
#     # figure.lines.extend([line])
#     ax = figure.add_subplot(111)
#
#     # Adds f(x) graph
#     plot_numbers = [function(x) / alpha + x for x in function_range]
#     ax.plot(function_range[0], 0, "ro")
#     ax.plot(function_range[-1], 0, "ro")
#     ax.plot(function_range, plot_numbers, '-b', label='f(x)')
#
#     # Adds g(x) = y graph
#     ax.plot(function_range, function_range, '-r', label='g(x)')
#
#     root = simple_iteration_method(ax)
#     print(f"Gautas x = {root}")
#
#     # Adds labels
#     ax.legend(loc='upper left')
#     ax.grid(True)
#     canvas = FigureCanvasTkAgg(figure, master=graph_frame)
#     canvas.get_tk_widget().pack()
#     canvas.draw()
#
    # # Adds graph's toolbar
    # toolbar = tkinter.Frame(master=graph_frame)
    # toolbar.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
    # toolbar.pack()
    # toolbar = NavigationToolbar2Tk(canvas, toolbar)
    # toolbar.config(background='white')
#
#     current_page = 1
#
#
# def show_graph_2():
#     global current_page
#
#     if current_page is not 2:
#         clear_frame(graph_frame)
#
#     figure = Figure(figsize=(10, 6), dpi=100)
#     ax = figure.add_subplot(111)
#
#     # Adds f(x) graph
#     plot_numbers = [function(x) for x in function_range]
#     ax.plot(function_range[0], 0, "ro")
#     ax.plot(function_range[-1], 0, "ro")
#     ax.plot(function_range, plot_numbers, '-b', label='f(x)')
#
#     # Adds labels
#     ax.legend(loc='upper left')
#     ax.grid(True)
#     canvas = FigureCanvasTkAgg(figure, master=graph_frame)
#     # canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)
#     canvas.get_tk_widget().pack()
#     canvas.draw()
#     canvas.flush_events()
#
#     #
#     root = newton_method()
#     print(root)
#
#     toolbar = tkinter.Frame(master=graph_frame)
#     toolbar.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
#     toolbar.pack()
#     toolbar = NavigationToolbar2Tk(canvas, toolbar)
#     toolbar.config(background='white')
#
#
# def show_graph_3():
#     global current_page
#
#     if current_page is not 3:
#         clear_frame(graph_frame)
#
#     figure = Figure(figsize=(10, 6), dpi=100)
#     ax = figure.add_subplot(111)
#
#     # Adds f(x) graph
#     plot_numbers = [function(x) for x in function_range]
#     ax.plot(function_range, plot_numbers, '-b', label='f(x)')
#
#     # Adds labels
#     ax.legend(loc='upper left')
#     ax.grid(True)
#     canvas = FigureCanvasTkAgg(figure, master=graph_frame)
#     canvas.get_tk_widget().pack()
#     canvas.draw()
#     canvas.flush_events()
#
#     # Adds graph's toolbar
#     toolbar = tkinter.Frame(master=graph_frame)
#     toolbar.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
#     toolbar.pack()
#     toolbar = NavigationToolbar2Tk(canvas, toolbar)
#     toolbar.config(background='white')
#
#     # Finds the first root and shows calculations
#     root = scanning_method(ax, canvas)
#     print(f"Saknis x ={root}")
#
#     current_page = 3
#
#
# def clear_frame(frame):
#     for widget in frame.winfo_children():
#         widget.destroy()


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

# window = tkinter.Tk()
# window.title("Skaitmeniniai algoritmai 12 vr.")
# # window.minsize(400, 200)
# window.geometry("1250x630")
# window.resizable(0, 0)
#
# # Adds frames for graph and menu buttons
# graph_frame = tkinter.Frame(window)
# menu_frame = tkinter.Frame(window)
#
# # Sets frames background colors
# graph_frame.configure(background='white')
# menu_frame.configure(background='white')
#
# # Divides window to both frames
# graph_frame.pack(side="left", expand=True, fill="both")
# menu_frame.pack(side="right", expand=True, fill="both")
#
# current_page = 0
#
# # Adds menu buttons
# menu_frame.grid_columnconfigure(0, weight=1)
# menu_graph1 = tkinter.Button(menu_frame, text="Paprastujų iteracijų metodas", width=25, command=show_graph_1).grid(
#     row=0, column=0, sticky="e", pady=(0, 2))
# menu_graph2 = tkinter.Button(menu_frame, text="Niutono (liestinių) metodas", width=25, command=show_graph_2).grid(
#     row=1, column=0, sticky="e", pady=2)
# menu_graph3 = tkinter.Button(menu_frame, text="Skenavimo metodas", width=25, command=show_graph_3).grid(
#     row=2, column=0, sticky="e", pady=2)
#
# window.mainloop()
