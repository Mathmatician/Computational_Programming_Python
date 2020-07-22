# Author: Jerome Richards
# Trapezoidal Rule
#
# Description: Utilzes the trapezoidal rule to find the area under an acceleration function. The function is F(t) = 9.8

import numpy as np
import matplotlib.pyplot as plt
import math



# Name: Trapezoidal
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def TrapezoidalOfData(x_data, f):
    x = [];
    y = [];
    area = 0;
    for i in range(0, len(f) - 1):
        delta = x_data[i + 1] - x_data[i];
        area = area + (delta/2)*( f[i] + f[i + 1] );
        y.append(area);
        x.append(x_data[i + 1]);
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


