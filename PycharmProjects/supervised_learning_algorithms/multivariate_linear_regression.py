import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def cost_function(x, theta_0, theta_1):  # calculate the linear hypothesis given two parameters
    # theta_0 and theta_1
    return theta_0 + theta_1 * x


def n_parameters(n=4):
    value = n
    dicted_parameters = {}
    for k in range(value):
        concat = 'theta_' + value
        dicted_parameters[concat] = None
    return dicted_parameters


def n_hypothesis(x, theta_0):
    "default number of features is 4"
    init_theta0 = theta_0
    no_of_parameters, calculated_y, dicted_params = np.shape(x), 0, {}
    dicted_params = n_parameters(n=no_of_parameters)
    calculated_y = [init_theta0 + a * (b.T) for a, b in zip(x, dicted_params.values())]
    return calculated_y


def n_cost_function(x, y):
    m = np.shape(x)[0]
    cal_y, sum_euclidean_distance, Euclidean_distance = n_hypothesis(x), 0, []
    Euclidean_distance = [(a - b) ** 2 for a in x for b in y]
    sum_euclidean_distance = sum(Euclidean_distance)
    return sum_euclidean_distance / (2 * m)


learning_rate = 0.01


def minimize(x, y, alpha=learning_rate, initial_theta, value_of_theta=1):
    m = np.shape(x)[0]
    cal_y, sum_euclidean_distance, Euclidean_distance = n_hypothesis(x), 0, []
    Euclidean_distance = [a - b for a in x for b in y]
    # x[0], x[1] is all the elements in the first and second column
    Euclidean_solution = [j * k for j in Euclidean_distance for k in x[value_of_theta - 1]]
    sum_euclidean_distance = sum(Euclidean_distance)
    theta = sum_euclidean_distance * alpha / (m)
    if initial_theta == theta:
        return theta

    else:
        minimize(x, y, alpha=learning_rate, initial_theta=theta, value_of_theta=1)


def minimize_n_cost_function(**params):
    theta_params = params
    counter = 1
    for k in theta_params.keys():
        theta_params['theta_1'] = minimize(x, y, alpha=learning_rate,
                                           initial_theta=theta_params['theta_1'], value_of_theta=counter)









