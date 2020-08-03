# Author: Jerome Richards
# Trapezoidal Rule
#
# Description: Utilzes different integral approximations (trapezoidal, Reiman Sums)

import numpy as np
import matplotlib.pyplot as plt
import math





# Description: Uses Reiman Sums to approximate area under the function produced by the data
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def ReimanSumsOfData(x_data, y_data):
    x = [];
    y = [];
    area = 0;
    for i in range(0, len(y_data) - 1):
        delta = x_data[i + 1] - x_data[i];
        area = area + delta * y_data[i];
        y.append(area);
        x.append(x_data[i]);
    return x, y;






# Description: Uses Reiman Sums to approximate area under function f from point a to b
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def ReimanSumsOfFunction(f, a, b, partitions):
    x = [];
    y = [];
    delta = (b - a) / partitions;
    area = 0;
    i = a;
    while i < b:
        area = area + delta * f(i);
        y.append(area);
        i = i + delta;
        x.append(i);
    return x, y;




# Name: Trapezoidal
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def TrapezoidalOfData(x_data, y_data):
    x = [];
    y = [];
    area = 0;
    for i in range(0, len(y_data) - 1):
        delta = x_data[i + 1] - x_data[i];
        area = area + (delta/2)*( y_data[i] + y_data[i + 1] );
        y.append(area);
        x.append(x_data[i]);
    return x, y;




# Name: Trapezoidal
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def TrapezoidalOfFunction(f, a, b, partitions):
    x = [];
    y = [];
    delta = (b - a) / partitions;
    area = 0;
    i = a;
    while i < b:
        area = area + (delta/2)*( f(i) + f(i + 1) );
        y.append(area);
        i = i + delta;
        x.append(i);
    return x, y;


