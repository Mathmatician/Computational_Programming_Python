# Author: Jerome Richards
# Discrete Cosine Fourier Transform
#
# Interpolates the data using A Discrete Cosine Transform (DCT)


##########################################
# Please reference textbook:             #
#                                        #
#     Numerical Analysis Second Edition  #
#                 By:                    #
#            Timothy Sauer               #
#                                        #
# to understand the logic and reasoning  #
# behind each declared variable, array,  #
# and function.                          #
#                                        #
##########################################


import matplotlib.pyplot as plt
import numpy as np


# Description: Uses Discrete Cosine Transform Interpolation
# Parameters: data on the vertical axis, y_data, and a threshold variable, thresh, that a fourier constant must meet to not equal zero
# Returns: three arrays - horizontal data stored in x array, vertical data stored in y array, and fourier constants stored in f array
def DiscreteCosineTransform(y_data, thresh):



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
    N = len(y_data);
    C = DCTMatrix(N);
    f = np.matmul(C, y_data); # the fourier constants






    #############################################################################################
    #                                                                                           #
    # This sets the fourier constants equal to zero if it does not meet the specified threshold #
    #                                                                                           #
    #############################################################################################
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
    x = [];
    y = [];
    i = 0;
    while i < x_end:
        x.append(i);
        y.append(InterpFunc(i, f, N));
        i = i + dx;


    return x, y, f;
