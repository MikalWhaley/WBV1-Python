import numpy as np
import math
import random

def factorial(x):
    if (x==0 or x==1):
        return 1
    return (factorial(x-1) * x)


def poisson(x, lambd, cumulative):
    
    if(cumulative):
        sumVar = float(0)
        for i in range(0, x + 1):
            sumVar += ( float((math.exp(-lambd)) * float(pow(lambd, i))) / float(factorial(i)))
        return sumVar
    else:
        return (math.exp(-lambd) * pow(lambd, x) / factorial(x))


def random_test(probability):
    precision = 100000
    threshold = precision * probability
    rn = random.uniform(0, 1) * precision

    return (threshold > rn)


def random_distribution(mean, std):
    return mean + 2.0 * std * (random.uniform(0, 1) + random.uniform(0, 1) + random.uniform(0, 1) - 1.5)


def compound_probability(probability, factor):

    return (1 - pow(1 - probability, float(factor)))
