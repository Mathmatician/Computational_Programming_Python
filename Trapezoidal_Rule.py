# Author: Jerome Richards
# Trapezoidal Rule
#
# Description: Utilzes the trapezoidal rule to find the area under an acceleration function. The function is F(t) = 9.8

import numpy as np
import matplotlib.pyplot as plt
import math





# Name: The inquired function, F
# Parameters: a time input, t
# Returns: a floating point value
def F(t):
    return 9.8;





# Name: Trapezoidal
# Parameters: an array of output values, f, produced by the inquired function
# Returns: an array
def Trapezoidal(f):
    A = [];
    area = 0;
    i = 0;
    for i in range(0, len(f)):
        area = area + (delta/2)*( f[i] + f[i - 1] );
        A.append(area);
        i = i + 1;
    return A;

###############################################################################################################
#                                                                                                             #
# Creates a delta by taking the difference between point a and be, then dividing by the number of partitions. #
# As we increment by delta, each index value, i, will be stored in the t_vals array denoting time and each    #
# value evaluated by the function, F(i), will be stored in the y_vals.                                        #
#                                                                                                             #
###############################################################################################################
y_vals = [];
t_vals = [];
a = 0;
b = 6;
partitions = 1000;
delta = (b - a) / partitions;
i = a;
while i < b:
    y_vals.append(F(i));
    t_vals.append(i);
    i = i + delta;



###############################################################################################################
#                                                                                                             #
# We store all the values into y_vals into the acc array, which is the values for the accelerations values.   #
# By rules of kinematics, finding the area under the acceleration function gives us the velocity, and finding #
# the area under the velocity gives us the position, which we have simply labed as y.                         #
#                                                                                                             #
###############################################################################################################
acc = y_vals; # array of acceleration values
vel = Trapezoidal(acc); # array of velocity values
y = Trapezoidal(vel); # array of position values on the y-0axis

print('Acceleration:', acc[len(acc) - 1]);
print('Velocity:', vel[len(vel) - 1]);
print('Position:', y[len(y) - 1]);
print();

plt.plot(t_vals, acc, label = "Acceleration");
plt.plot(t_vals, vel, label = "Velocity");
plt.plot(t_vals, y, label = "Position");
plt.legend(loc = "best");
plt.show();
