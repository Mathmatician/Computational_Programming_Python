# Author: Jerome Richards
# Derivative
#
# Uses the least squres meathod to find a trend line

import numpy as np
import matplotlib.pyplot as plt
import Read_Data as RD


##########################################
# Please reference textbook:             #
#                                        #
#     Numerical Analysis Second Edition  #
#                 By:                    #
#            Timothy Sauer               #
#                                        #
# to understand the logic and reasoning  #
# behind each declared variable and      #
# array.                                 #
#                                        #
##########################################



# Description: Uses least squares method to fit y = mx + b to the data and generate a trend line
# Parameters: data on the horizontal axis, x_data, and on the vertical axis, y_data
# Returns: two arrays of size two - x values with x[0] as the start point and x[1] as the end point on horizontal axis,
#          and y values wity y[0] as the start point and y[1] as the end point on vertical axis
def TrendLineFunction(x_data, y_data):

    if len(x_data) != len(y_data):
        print('Both arrays must be the same length');
        return 0, 0;

    def F(x):
        return (m*x + b);


    N = len(x_data);
    A = np.ones((N, 2));
    for i in range(0, N):
        A[i, 0] = x_data[i];

    A_t = A.transpose();
    a_h = np.matmul(A_t, A);
    c = np.matmul(A_t, y_data);
    a_inv = np.linalg.inv(a_h);
    S = np.matmul(a_inv, c);

    m = S[0]; # slop of trend line
    b = S[1];

    x = [];
    y = [];
    x.append(x_data[0]);
    y.append(F(x_data[0]));
    x.append(x_data[len(x_data) - 1]);
    y.append(F(x_data[len(x_data) - 1]));

    return x, y;
