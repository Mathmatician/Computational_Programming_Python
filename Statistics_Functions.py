# Author: Jerome Richards
# Statistics Functions
#
# Description: Different functions commonly used for Statistics (work in progress)

import numpy as np
import math




# Description: Finds the average of a set of data points
# Parameters: an array of data points
# Returns: the average
def Average(data):
    avg = 0;
    N = len(data);
    for i in range(0, N):
        avg = avg + data[i];
    avg = avg / N;
    return avg;





# Description: Finds the middle value of data points when in order from lowest to greatest or vice versa
# Parameters: an array of data points
# Returns: the average of the two middle values if the size of the array is even or simply the middle number of the data points
def Median(data):
    N = len(data);
    # Copy data
    copied_data = [];
    for i in range(0, N):
        copied_data.append(data[i]);

    # Bubble Sort
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            if copied_data[i] < copied_data[i + 1]:
                tmp = copied_data[i];
                copied_data[i] = copied_data[i + 1];
                copied_data[i + 1] = tmp;
    if N % 2 == 0:
        i = int(N / 2);
        v = copied_data[i - 1] + copied_data[i];
        return v / 2;
    i = int(N / 2);
    return copied_data[i];








# Description: Finds the most frequently appearing value in a set of data points
# Parameters: an array of data points
# Returns: an array of most frequently appeared values and an integer that is the frequency amount
def Mode(data):
    N = len(data);
    y = [];
    count_arr = np.zeros(N);
    for i in range(0, N):
        for j in range(0, N):
            if data[j] == data[i]:
                count_arr[j] = count_arr[j] + 1;
                break;
    highest = 0;
    for i in range(0, N):
        if count_arr[i] > count_arr[highest]:
            highest = i;

    for i in range(0, N):
            if count_arr[highest] == count_arr[i]:
                y.append(data[i]);

    return y, int(count_arr[highest]);








# Description: Finds the spread of the data using the variance principle
# Parameters: an array of data points
# Returns: an array of the variance spread for each data point and a floating point number that is the variance value of the data set
def Variance(data):
    avg_dist = 0;
    lst = [];
    N = len(data);
    AVG = Average(data);
    for i in range(0, N):
        v = (data[i] - AVG)**2;
        avg_dist = avg_dist + v;
        lst.append(v);
    avg_dist = avg_dist / N;
    return lst, avg_dist;








# Description: Finds the spread of the data using the variance principle
# Parameters: an array of data points and a DELTA parameter specifying the range to be graphed from the center point of the Gaussian
# Returns: an array of the variance spread for each data point and a floating point number that is the variance value of the data set
def GaussianDistribution(data, DELTA):
    tmp, v = Variance(data);
    avg = Average(data);
    std_dev = np.sqrt(v);

    def GaussianFunction(x):
        return (1 / (std_dev * np.sqrt(2*np.pi)) ) * np.exp( (-1/2)*( (x - avg)/std_dev )**2 );

    x = [];
    y = [];
    x_0 = avg - DELTA;
    x_f = avg + DELTA;
    dx = 0.01;
    i = x_0;
    while i < x_f:
        x.append(i);
        y.append(GaussianFunction(i));
        i = i + dx;
    return x, y;








# Description: Finds the spread of the data using the variance principle
# Parameters: an array of data points, an initial point x_0, and an end point x_f
# Returns: an array of the variance spread for each data point and a floating point number that is the variance value of the data set
def GaussianBoundDistribution(data, x_0, x_f):
    tmp, v = Variance(data);
    avg = Average(data);
    std_dev = np.sqrt(v);

    def GaussianFunction(x):
        return (1 / (std_dev * np.sqrt(2*np.pi)) ) * np.exp( (-1/2)*( (x - avg)/std_dev )**2 );

    x = [];
    y = [];
    dx = 0.01;
    i = x_0;
    while i < x_f:
        x.append(i);
        y.append(GaussianFunction(i));
        i = i + dx;
    return x, y;








# Description: Finds the spread of the data using the Poisson principle
# Parameters: an array of data points, an initial point x_0, and an end point x_f
# Returns: an array of the Poisson spread for each data point and a floating point number that is the variance value of the data set
def PoissonBoundDistribution(data, x_0, x_f):
    avg = Average(data);

    def PoissonFunction(x):
        numerator = EvaluateLargeExponent(avg, x);
        denominator = StirlingApproximation(x);
        return ( numerator / denominator ) * np.exp( -avg );

    x = [];
    y = [];
    dx = 0.01;
    i = x_0;
    while i < x_f:
        x.append(i);
        y.append(PoissonFunction(i));
        i = i + dx;
    return x, y;








# Description: Is used to approximate the factorial of the input parameter x
# Parameters: any number (does not have to be integers only)
# Returns: the approximate answer of x!
def StirlingApproximation(x):
    v = 0;
    if v > 20:
        v = EvaluateLargeExponent(x / math.e, x);
    else:
        v = (x / math.e)**x;
    return np.sqrt(2 * np.pi * x) * v;








# Description: Is used to evaluate large exponents
# Parameters: base number, x, and exponenet, pwr
# Returns: x^pwr (x**pwr)
def EvaluateLargeExponent(x, pwr):
    return 10**( pwr * np.log10(x) );



