# How to plot a simple bar graph using python?
# It can be done by using a module- matplotlib and its submodule pyplot

import matplotlib.pyplot as plt

xaxis = ['apple', 'banana', 'orange']
yaxis = [34, 56, 78]

plt.bar(xaxis, yaxis)
plt.show()