from numpy import random
from Calculations import calc
import Math

def get_possibility_of_outbreak(lot, sick, susceptible, dose, process):
    return 1 - calc.poisson(sick, (1 // susceptible) * (1 // dose) * (1 // pow(10, process)), True)



#  * @param lot {Object}
#  * @param sick {int} minimum amount of people sick to be considered an outbreak
#  * @param susceptible {int} population size of exposed
#  * @param dose {int} amount of CFUs required to get sick
#  * @param process {number} log reduction