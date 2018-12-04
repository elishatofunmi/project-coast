## linear regression with one variable

class Hypothesis:
    def __init__(self, **params):
        # params is a dictionary that takes in to parameters the x or data
        # and y the target variable to be predicted
        self.variable_x = params['x']
        self.target_class = params['y']
        return

    #def outline_features():
     #   return outline_features

    def hypothesis(linear=True, polynomial=False,  init_theta_0= 10, outline_features):
    # this function returns either a linear function or a polynomic function
    # outline features can be a value or a list of values


    if (linear == True) & & (polynomial == True):
        raise "linear and polynomial can't be true at the same time"
    else:

        if linear == True:

            hypothesis = theta_0 + theta_1 * outline_features
        else:
            pass

        if polynomial == True:
            hypothesis = theta_0 + theta_1 * outline_features[0] + outline_features[1] * theta_2

        elif polynomial == 'quadratic':
            hypothesis = theta_0 + theta_1 * outline_features[0] + pow(outline_features[1], 2) * theta_2

        elif polynomial == 'degree_3':
            hypothesis = theta_0 + theta_1 * outline_features[0] + pow(outline_features[1], 2) * theta_2 + pow(
                outline_features[3], 3) * theta_3
        else:
            print "polynomial degree exceeds 3"

    return hypothesis






class minimize_param(hypothesis,x,y, linear = True, polynomial = False, params = {}):
    # params contains all the parameters that would be minimized
    def __init__(self):
        self.number_of_training_examples = np.shape(x)[0] # total number of training values
        self.linear = linear
        self.polynomial = polynomial
        self.x = x
        self.y = y
        solution = 0
        solution = self.return_solution
        return solution

    def compute_hypothesis(value):
        # must be able to compute a single value or multiple values
        init_hypothesis = hypothesis.hypothesis(self.linear,self.polynomial ,value)
        return init_hypotheis

    def compute_square(self,x,y):
        numpy_x, numpy_y, difference, sum_diff  = x, y, [],0
        compute_hypothesis_x = x.apply(self.compute_hypothesis)
        for i,j in zip(compute_hypothesis_x, numpy_y):
            difference.append(pow(i-j, 2))

        sum_diff = np.sum(np.array(difference))

        return sum_diff

    def return_solution(self):
        value = 0
        value = (0.5 * self.compute_square(self.x,self.y))/ self.number_of_training_examples
        return value







class parameter_learning(minimize_param, numb_of_param, x,y):
    # continuously updates theta 0 and theta 1
    def __init__(self, theta_1, learning_param):
        self.init_theta_1 = theta_1
        self.learning_param = learning_param
        self.x, self.num_of_param,self.y, self.list_param = x, numb_of_param, y, []
        self.updated_values = {}
        self.list_param = self.generate_numbers_of_param
        self.updated_values = self.update_others


    def generate_numbers_of_param(self):
        param_list = []
        for i in range(1, self.num_of_param):
            param_list.append("theta_"+ str(i))
        return param_list


    def update_theta_0(self):
        dict_param['Theta_0'] = self.theta_1
        self.init_theta_1 -= self.learning_param * minimize_param(self.x,self.y, param = dict_param)
        return self.init_theta_1

    def update_others(self):
        # returns a key to value pair of the parameters and their updated values
        dict_parameter = {}
        for param in self.list_param:
            dict_parameter[param] = 0 # assuming 0 as the initial values of the parameter
        for k in self.list_param:
            parameter -= self.learning_param * minimize_param(self.x, self.y, dict_parameter)
            dict_parameter[k] = parameter

        return dict_parameter

















if "__name__" == "__main__":
    hyp = Hypothesis()
    minimize = minimize_param()
    param_learn = parameter_learning()

