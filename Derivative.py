# Author: Jerome Richards
# Derivative
#
# Description Takes the derivative of the given function, F(x), and compares it in a plot with the origional function.

import math
import numpy as np

def FunctionDerivative(FUNC, start, end, DELTA, NUM_OF_dF):


    # Name: The derivative of the inquired function, F.
    # Parameters: a function, f, a floating point value x, and the derivative n (n determines the amount of times to take a derivative.)
    # Returns: a floating point value
    def dF(f, x, n):
        if n <= 0:
            return f(x);
        else:
            h = 0.01;
            return (dF(f, x + h, n - 1) - dF(f, x, n - 1)) / h;


    ###########################################################
    #                                                         #
    # Creates a y array with the original function's y values #
    #                                                         #
    ###########################################################

    x = [];
    y = []; # y values for the original function
    delta = DELTA; # incremental distance on x-axis
    i = start;
    while i < end:
        x.append(i);
        y.append(dF(FUNC, i, NUM_OF_dF));
        i = i + delta;

    return x, y;
