# Author: Jerome Richards
# Cubic Spline Interpolation
#
# Interpolates the data using Cubic Splines



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

import numpy as np
import matplotlib.pyplot as plt

x_data = [0, 1, 2]; # Data on the x-axis
y_data = [3, -2, 1]; # Data on the y-axis




#################################################################
#                                                               #
# The cubic spline fomula function once all constants are found #
#                                                               #
#################################################################
def S(x, x_0, a, b, c, d):
    return ( a + b*(x - x_0) + c*((x - x_0)**2) + d*((x - x_0)**3) );





delta_x = np.zeros((len(x_data) - 1, 1));  # The differences in length between x values
delta_y = np.zeros((len(x_data) - 1, 1));  # The differences in length between y values
D = np.zeros((len(x_data) - 1, 1));  # List of 'd' terms that will be used in the Spline Function
B = np.zeros((len(x_data) - 1, 1));  # List of 'b' terms that will be used in the Spline Function

M = np.zeros((len(x_data), len(x_data)));  # The Spline Matrix
h = np.zeros((len(x_data), 1));  # The Spline Vector




############################################
#                                          #
# Populates the delta_x and delta_y arrays #
#                                          #
############################################
for i in range(0, len(x_data) - 1):
    delta_x[i] = x_data[i + 1] - x_data[i];
    delta_y[i] = y_data[i + 1] - y_data[i];





###############################
#                             #
# Populates the Spline Matrix #
#                             #
###############################
M[0][0] = 1;
for i in range(1, len(x_data) - 1):
    M[i][i - 1] = delta_x[i - 1];
    M[i][i] = 2*(delta_x[i - 1] + delta_x[i]);
    M[i][i + 1] = delta_x[i];

M[len(x_data) - 1][len(x_data) - 1] = 1;






###############################
#                             #
# Populates the Spline Vector #
#                             #
###############################
h[0] = 0;

for i in range(0, len(h) - 2):
    h[i + 1] = 3*( (delta_y[i + 1]/delta_x[i + 1]) - (delta_y[i]/delta_x[i]) );

h[len(h) - 1] = 0;







###################################################################################################
#                                                                                                 #
# The Formula is M*C = h where C is a vector of unknowns. Solving for C, we take the inverse of M #
# and multiply it to both sides to attain C = M_inv*h                                             #
#                                                                                                 #
###################################################################################################
M_inv = np.linalg.inv(M); # inverse of matrix M
C = np.matmul(M_inv, h);  # Solving for C





#####################################
#                                   #
# Populates both the B and D arrays #
#                                   #
#####################################
for i in range(0, len(D)):
    D[i] = (C[i + 1] - C[i])/(3*delta_x[i]);
    B[i] = (delta_y[i]/delta_x[i]) - (delta_x[i]/3)*(2*C[i] + C[i + 1]);






#############################
#                           #
# Plot the Spline functions #
#                           #
#############################
x = [];
y = [];
end = x_data[len(x_data) - 1];
I = 0;
i = x_data[0];
dx = 0.01;
while i < end:
    x.append(i);
    if i >= x_data[I + 1]:
        I = I + 1;
    y.append(S(i, x_data[I], y_data[I], B[I], C[I], D[I]));
    i = i + dx;

plt.plot(x, y);
plt.show();

