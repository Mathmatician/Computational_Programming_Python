# Author: Jerome Richards
# Derivative
#
# Description Takes the derivative of the given function, F(x), and compares it in a plot with the origional function.

import math
import numpy as np


# Name: Takes derivative of received function from starting point to end point
# Parameters: a function, FUNC, starting value start, ending value end, increment value DELTA, and the derivative values NUM_OF_dF (NUM_OF_dF determines the amount of times to take a derivative.)
# Returns: two arrays - x values and y values, with spacings of DELTA increments
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
