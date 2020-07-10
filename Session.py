import wMath
import random
import numpy as np
import math as wMath
import Lot as wlot
import Calculations as wCalc
import Constants as wConst
import uuid

class Session:
    

    def __init__(self):
        self.username = "undefined"
        self.balance = wConst.DEFUALTGAME["balance"]
        self.UGID = "undefined"

        self.selections = {
            "GAP_Selection": wConst.DEFUALTGAME["GAP_Selection"],
            "Process_Selection": wConst.DEFUALTGAME["Process_Selection"],
            "rawTests": wConst.DEFUALTGAME["rawTests"],
            "finishedTests": wConst.DEFUALTGAME["finishedTests"]
        }

        self.statistics = { 
            "cycles": 0,
            "outbreaks": 0,
            "outbreak_multiplier": 1,
            "steps": 0,
            "peak": 5000
        }

    def construct(self, username):
        self.UGID = uuid.uuid1()

        if (username == "undefined"):
            self.username = self.UGID
        else:
            self.username = username
        

        print("Session " + self.UGID + " has been created!")

    
    def summary(self):
        self.obj = {
            "ID": "null", #self.ID, //no id?
            "Balance": self.balance,
            "GAP_Selection": self.selections["GAP_Selection"],
            "Process_Selection": self.selections["Process_Selection"],
            "rawTests": self.selections["rawTests"],
            "finishedTests": self.selections["finishedTests"],
            "cycles": self.statistics["cycles"],
            "outBreaks": self.statistics["outbreaks"],
            "peak": self.statistics["peak"]
        }
        print(self.obj)
    
    def between(self, n, upperLimit, lowerLimit):
        if(n > upperLimit):
          return upperLimit
        elif (n < lowerLimit):
          return lowerLimit
        else:
          return n
    
    def profile(self):
        prof_obj = {
            "GAP_Selection": wConst.GAP[self.selections.GAP_Selection]["Price"],
            "Process_Selection": Process[this.selections.Process_Selection].Price,
            "rawTests": this.selections.rawTests * Prices.PerRawTest,
            "finishedTests": this.selections.finishedTests * Prices.PerFinishedTest,
        }


    



    

    # def getBalance(self):
    #     print(self.balance)
    
    # def getUser(self):
    #     print(self.username)

