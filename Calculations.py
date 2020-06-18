from numpy import random

def get_possibility_of_outbreak(lot, sick, susceptible, dose, process):
    return 1-random.poisson