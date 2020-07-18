# Author: Jerome Richards
# Derivative
#
# Description Takes the derivative of the given function, F(x), and compares it in a plot with the origional function.

import math
import matplotlib.pyplot as plt


# Name: The inquired function, F
# Parameters: a floating point value, x
# Returns: a floating point value
def F(x):
    return math.log(x + 1);




# Name: The derivative of the inquired function, F.
# Parameters: a function, f, a floating point value x, and the derivative n (n determines the amount of times to take a derivative.
# Returns: a floating point value
def dF(f, x, n):
    if n <= 0:
        return f(x);
    else:
        h = 0.01;
        return (dF(f, x + h, n - 1) - dF(f, x, n - 1)) / h;





################################################################################################################
#                                                                                                              #
# Creates an x array with the original function's x values and a y array for the original function's y values. #
#                                                                                                              #
################################################################################################################


x = []; # x values for the original function
y = []; # y values for the original function
delta = 0.01; # incremental distance on x-axis
N = 10; # End point on the x-axis
i = 0;
while i < N:
    x.append(i);
    y.append(F(i));
    i = i + delta;





######################################################################################################################################
#                                                                                                                                    #
# Creates an x_2 array with the derivative of the original function's x values and a y_2 array for the original function's y values. #
#                                                                                                                                    #
######################################################################################################################################

x_2 = []; # x values for the derivative function
y_2 = []; # y values for the derivative function
i = 0;
while i < N:
    x_2.append(i);
    y_2.append(dF(F, i, 4)); # The third parameter for the dF function means we are taking the 4th derivative
    i = i + delta;





##################################################################################
#                                                                                #
# Plots both the original function and the derivative function on the same graph #
#                                                                                #
##################################################################################
plt.plot(x, y);
plt.plot(x_2, y_2);
plt.show();
