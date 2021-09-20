import numpy as np
import matplotlib.pyplot as plt


# Description: Approximates the unknown variables of given modeling function
# Parameters: params (coefficients of respective unknown variables) and output_data (raw data)
# Returns: an array with the calculated variables
def DataVariableEvaluator(params, output_data):
    ROW = len(params[0]);
    COL = len(params);
    A = np.ones((ROW, COL));
    for i in range(0, COL):
        for j in range(0, ROW):
            A[j, i] = params[i][j];

    A_t = A.transpose();
    a_h = np.matmul(A_t, A);

    b = np.ones((len(output_data), 1));
    for i in range(0, len(output_data)):
        b[i, 0] = output_data[i];

    c = np.matmul(A_t, b);
    a_inv = np.linalg.inv(a_h);
    ans_final = np.matmul(a_inv, c);
    return ans_final;









# Description: Approximates the unknown variables with Exponential Function Axexp(bx)
# Parameters: x_data, y_data, the delta increment of x, and the end point
# Returns: two arrays - x values and y values with calculated approximated model
def ExponentialTimesXFunction(x_data, y_data, delta_x, end):
    k_params    = [];
    b_params    = [];
    log_data = [];

    for i in range(0, len(x_data)):
        k_params.append(1);
        b_params.append(x_data[i]);
        log_data.append(np.log(y_data[i] / x_data[i]));

    params = [k_params, b_params];
    vars = DataVariableEvaluator(params, log_data);

    def F(x):
        A = np.exp(vars[0][0]);
        return A * x * np.exp(vars[1][0] * x);

    x = [];
    y = [];

    i = 0;
    while i < end:
        x.append(i);
        y.append(F(i));
        i = i + delta_x;

    return x, y;