import wMath
import random
import numpy as np
import math as wMath
import Lot as wlot
import Calculations as wCalc
import Constants as wConst


class Session:
    

    def __init__(self):
        self.username = "undefined"
        self.balance = wConst.DEFUALTGAME["balance"]

    def getBalance(self):
        print(self.balance)
    
    def getUser(self):
        print(self.username)

if __name__ == "__main__":
    s = Session()
    s.getBalance()
    s.getUser()