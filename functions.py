def cost_function(predicted, actual):
    """ Returns the cost function of given predicted and actual Y values """
    m = len(predicted)
    j = (1 / (2*m)) * sum(predicted, actual)
    return j


def sum(predicted, actual):
    """ Returns the sum of all ^2 differences of H(hypot)-Y values """
    sum = 0
    for count, instance in enumerate(predicted):
        try:
            sum += (predicted[count] - actual[count]) ** 2
        except OverflowError:
            print("Divergent")
            break
    return sum


def hypothesis(parameters, x):
    """ Returns an array consisting of predicted Y values """
    predicted = []
    for x_val in x:
        predicted.append(parameters[0] + parameters[1] * x_val)
    return predicted


def simul_update(parameters, rate, predicted, actual, x):
    """ Simultaneously updates the parameters (rate = learning rate) """
    temp = []
    for count, parameter in enumerate(parameters):
        temp.append(parameters[count] - rate * pderiv(count, predicted,
                                                      actual, x))
    for count, parameter in enumerate(parameters):
        parameters[count] = temp[count]


def pderiv(d_, predicted, actual, x):
    """ d_ is the variable to derive with respect to """
    m = len(predicted)
    if d_ == 0:
        sum_ = 0
        for count, instance in enumerate(predicted):
            sum_ += (predicted[count] - actual[count])
    else:
        sum_ = 0
        for count, instance in enumerate(predicted):
            sum_ += (predicted[count] - actual[count]) * x[count]
    pderiv = (1/m) * sum_
    return pderiv
