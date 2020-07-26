# Author: Jerome Richards
# Statistics Functions
#
# Description: Different functions commonly used for Statistics (work in progress)

import numpy as np


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
        i = N / 2;
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