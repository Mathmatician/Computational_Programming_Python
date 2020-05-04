# Author: Jerome Richards
# Discrete Cosine Fourier Transform
#
# Interpolates the data using A Discrete Cosine Transform (DCT)


import matplotlib.pyplot as plt
import numpy as np


# The Data
x = [0, 1, 2, 3, 4, 5, 6, 7]; # The time data
data = [-2.2, -2.8, -6.1, -3.9, 0.0, 1.1, -0.6, -1.1]; # the price data



############################################################################
#                                                                          #
# Function creates all the constants needed for our Discrete Cosine matrix #
#                                                                          #
############################################################################
def Constants(i, j, n):
    a = 1;
    if i <= 0:
        a = float(1/np.sqrt(2));
    return np.sqrt(2/float(n))*a*np.cos( (i*(2*j + 1)*np.pi)/(2*float(n)) );







################################################
#                                              #
# Function that creates Discrete Cosine matrix #
#                                              #
################################################
def DCTMatrix(n):
    Mx = np.zeros((n, n));
    for i in range(0, n):
        for j in range(0, n):
            Mx[i, j] = Constants(i, j, n);
    return Mx;






#########################################################
#                                                       #
# The derived function that interpolates the given data #
#                                                       #
#########################################################
def InterpFunc(t, y, n):
    v = y[0]/(np.sqrt(n));
    SUM = 0;
    for k in range(1, n):
        SUM = SUM + y[k]*np.cos( (k*(2*t + 1)*np.pi)/(2*float(n)) );
    SUM = SUM*(np.sqrt(2/float(n)));
    return v + SUM;








#########################################################
#                                                       #
# Generates the fourier constants and stores in array f #
#                                                       #
#########################################################
N = len(data);
C = DCTMatrix(N);
f = np.matmul(C, data); # the fourier constants






#############################################################################################
#                                                                                           #
# This sets the fourier constants equal to zero if it does not meet the specified threshold #
#                                                                                           #
#############################################################################################
thresh = 0;
for i in range(0, len(f)):
    if abs(f[i]) < thresh:
        f[i] = 0;






#################
#               #
# Plot the data #
#               #
#################
x_end = N - 1;
dx = 0.01;
X = [];
Y = [];
i = 0;
while i < x_end:
    X.append(i);
    Y.append(InterpFunc(i, f, N));
    i = i + dx;


plt.plot(X, Y, color='red', label='DCT');
plt.legend(loc='best');
plt.show();

