import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def cost_function(x, theta_0, theta_1): # calculate the linear hypothesis given two parameters
    # theta_0 and theta_1
    return theta_0 + theta_1*x


no_of_training_examples = None
def minimize_cost_function(m = no_of_training_exammples, x, y, theta_0, theta_1):
    """The minimize cost function computes the minimum euclidean distance given
    theta_0 and theta_1 by using data x and y"""
    var_x, var_y = np.array(x), np.array(y)
    compute_1, compute_2, compute_3 = (0,0,0)
    minimized_solution = []
    for i in range(m):
        compute_1 = var_y[i] - cost_function(var_x[i],theta_0, theta_1) # finds the computed Euclidean distance between
        #  x and its corresponding value y
        compute_2 = pow(compute_1,2) # square of the distance
        minimized_solution.append(compute_2) # appends the corresponding solution to a list minimized_solution
    compute_3 = sum(minimized_solution)/ (2 * m) # compute the minimized cost function of x and y by dividing by
    # twice the number of training examples
    return compute_3



def differential_of_minimized_cost_function_theta_0(m = no_of_training_examples, x, y, theta_0, theta_1, initial_theta0):
    """"It is a recursive function that keeps updating
    the value of theta_0"""
    initial_val = initial_theta0
    compute_1 = [val cost_function(val, theta_0, theta_1)] # computes the corresponding value of x given theta_0 and theta_1(list comprehension)
    compute_2 = [var_x-var_y for var_x, var_y in zip(compute_1,y)] # subtracts the corresponding values of x and y
    theta = sum(compute_2)/m
    if initial_theta0 == theta:
        return theta
    else:
        differential_of_minimized_cost_function(m = no_of_training_examples, x, y, theta_0 = theta, theta_1, initial_theta0 = initial_val) # returns itself (recursion)


def differential_of_minimized_cost_function_theta_1(m = no_of_training_examples, x, y, theta_0, theta_1, initial_theta1):
    """It is a recursive function that keeps updating
    the value of theta_1"""
    initial_val = initial_theta1
    compute_1 = [val cost_function(val, theta_0, theta_1)] # computes the corresponding value of x given theta_0 and theta_1(list comprehension)
    compute_2 = [var_x-var_y for var_x, var_y in zip(compute_1,y)] # subtracts the corresponding values of x and y (list comprehension)
    theta = sum(compute_2)/m
    if initial_theta == updated_theta:
        return updated_theta
    else:
        differential_of_minimized_cost_function(m = no_of_training_examples, x, y, theta_0, theta_1 = theta, initial_theta1 = initial_val) # returns itself (recursion)



learning_rate = None
def converging_parameter(alpha=learning_rate, theta0, theta1):
    initial_theta = {'theta_0': theta0, 'theta_1': theta1} # dictionary that retains the initial value of theta
    updated_theta = {'theta_0': updated_theta_0, 'theta_1': updated_theta_1} # dictionary that retains the updated value of theta
    differential_of_minimized_cost_function = 0
    compute_0, compute_1, updated_theta_0, updated_theta_1 = (0,0,0,0) # unpacking variables

    # compute the minimized cost function for theta 0 using the function (differential_of_minimized_cost_function_theta_0)
    compute_0 = differential_of_minimized_cost_function_theta_0(m = no_of_training_examples, x, y,theta_0, theta_1, initial_theta0 = initial_theta['theta_0']) * alpha
    updated_theta['theta_0'] = available_theta['theta_0'] - compute_1 # updated value of the theta 0


    # compute the minimized cost function for theta 1 using the function (differential_of_minimized_cost_function_theta_1)
    compute_1 = differential_of_minimized_cost_function_theta_1(m=no_of_training_examples, x, y, theta_0, theta_1,initial_theta1 = initial_theta['theta_1']) * alpha
    updated_theta['theta_1'] = available_theta['theta_1'] - compute_1 # updated value of the theta 1

    return updated_theta.values() # returns the updated value of both theta_0 and theta_1

