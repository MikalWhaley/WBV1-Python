import wMath
import random
import numpy as np
import math
import wMath as wMath
import Lot as wlot
import Calculations as wCalc
import Constants as wConst
import uuid

def list_splice(target, start, delete_count=None, *items):

    # Remove existing elements and/or add new elements to a list.

    # target        the target list (will be changed)
    # start         index of starting position
    # delete_count  number of items to remove (default: len(target) - start)
    # *items        items to insert at start index

    # Returns a new list of removed items (or an empty list)
    

    #Editied to return target instead of remove by Mikechunger should work like JS splice now
        if(delete_count == None):
            delete_count = len(target) - start

        # store removed range in a separate list and replace with *items
        total = start + delete_count
        #removed = target[start:total] # no longer needed so okay
        target[start:total] = items

        return target




class Session:
    

    def __init__(self, ID):
        self.username = "undefined"
        self.balance = wConst.DEFUALTGAME["balance"]
        self.UGID = "undefined"
        self.ID = ID

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
            "GAP_Selection": wConst.GAP[self.selections["GAP_Selection"]]["Price"],
            "Process_Selection": wConst.PROCESS[self.selections["Process_Selection"]]["price"],
            "rawTests": self.selections["rawTests"] * wConst.PRICES["PerRawTest"],
            "finishedTests": self.selections["finishedTests"] * wConst.PRICES["PerFinishedTest"],
            "Total": wConst.GAP[self.selections["GAP_Selection"]]["Price"] +
            wConst.PROCESS[self.selections["Process_Selection"]]["Price"] +
            self.selections["rawTests"] * wConst.PRICES["PerRawTest"] +
            self.selections["finishedTests"] * wConst.PRICES["PerFinishedTest"],
            "Limit": self.between(math.floor(self.balance / ((wConst.GAP[self.selections["GAP_Selection"]]["Price"]) +
            wConst.PROCESS[self.selections["Process_Selection"]]["Price"] +
            self.selections["rawTests"] * wConst.PRICES["PerRawTest"] +
            self.selections["finishedTests"] * wConst.PRICES["PerFinishedTest"])), 1000, 1)
        }
        return(prof_obj)

    def cost(self):
        return (float(wConst.GAP[self.selections["GAP_Selection"]]["Price"]) +
        float(wConst.PROCESS[self.selections["Process_Selection"]]["Price"]) +
        float(self.selections["rawTests"]) * float(wConst.PRICES["PerRawTest"]) +
        float(self.selections["finishedTests"]) * float(wConst.PRICES["PerFinishedTest"]))

    def select(self, id, val):

        id = id.upper()

        
        if( id == "GAP"):

            keys = wConst.GAP.keys()
            
            if(val.upper() in keys):
                self.selections["GAP_Selection"] = val
                return True
                

        if (id == "PROCESS"):

            keys = wConst.GAP.keys()

            if(val.upper() in keys):
                self.selections["Process_Selection"] = val
                return True

        if (id == "RAWTESTS"):

            if(val.isnumeric()):
                self.selections["RAWTESTS"] = val
                return True
        
        if (id == "FINISHEDTESTS"):

            if(val.isnumeric()):
                self.selections["FINISHEDTESTS"] = val
                return True

        if (id == "USERNAME"):
            self.username = val
            return True
        
        return False


    def cycle(self, amount):
        #beforeBalance = self.balance

        #STEP 1 Check For Substantial Balance
        costNum = self.cost()
        price = costNum * amount

        if(price > self.balance):
            return '{"Error": "Total Price of Cycle(' + price + ') exceeds current balance(' + self.balance + ')"}'
        #STEP 2 Get GAP Multipliers
        Gap = wConst.GAP[self.selections["GAP_Selection"]]

        # // STEP 3 Generate Lots
        lots = []

        for i in range(0, amount):
            lot = wlot.Lot()
            lots.append(lot)
            lot.ID = i

            #print(lot.total_cfu)

            m = wMath.random_distribution(Gap["Multiplier"], Gap["STD"])

            lot.total_cfu *= .25
            lot.total_cfu *= m

        # // STEP 4 Raw and Finished Product Testing

        outbreakChances = []

        # // STEP 4.1 Raw Testing

        rawCaught = 0

        c = 0
        while(c < len(lots)):
            lot = lots[c]
            rawTestingCalculation = 1 - wMath.poisson(0, (lot.getCFUPerPound() * 150) / 454, False)
            
            chanceOfPositive = wMath.compound_probability(rawTestingCalculation, self.selections["rawTests"])
            positive = wMath.random_test(chanceOfPositive)
            
            if (positive):
                lots = list_splice(lots, c, 1)
                rawCaught += 1
                c -= 1
            c += 1
    
        # Step 4.2 Finished Testing

        finishedCaught = 0
        c = 0
        while(c < len(lots)):
            lot = lots[c]
            process = wConst.PROCESS[self.selections["Process_Selection"]]["Reduction"]
            reduced = lot.total_cfu * (1 / math.pow(10, process))
            CFUsPerPound = reduced / lot.lot_size


            testingCalculation = 1 - wMath.poisson(0, (CFUsPerPound * 150)/454, False)
            chanceOfPositive = wMath.compound_probability(testingCalculation, self.selections["finishedTests"])
            positive = wMath.random_test(chanceOfPositive)

            if (positive):
                lots = list_splice(lots, c, 1)
                finishedCaught += 1
                c -= 1
            c += 1 
    
        #  // STEP 5 Out Break Probability Calculation


        # total_cfus = 0
        # total_counted = 0

        # for i in range(0, len(lots)):
        #     total_cfus += lots[i].total_cfu
        #     total_counted += 1
        
        # average_cfus = total_cfus / total_counted

        # print('Average Cfus > ' + str(average_cfus))

        # outbreakChances = []

        for i in range(0, len(lots)):
            # this line
            #print(wConst.PROCESS[self.selections["Process_Selection"]]["Reduction"])
            outbreakChances.append(wCalc.get_possibility_of_outbreak(lots[i], wConst.OUTBREAKREQUIREMENTS["Sick"], wConst.OUTBREAKREQUIREMENTS["Susceptible"], wConst.OUTBREAKREQUIREMENTS["Dose"], wConst.PROCESS[self.selections["Process_Selection"]]["Reduction"]))
            #print(wCalc.get_possibility_of_outbreak(lots[i], wConst.OUTBREAKREQUIREMENTS["Sick"], wConst.OUTBREAKREQUIREMENTS["Susceptible"], wConst.OUTBREAKREQUIREMENTS["Dose"], wConst.PROCESS[self.selections["Process_Selection"]]["Reduction"]))

        #  // STEP 6 Outbreak random probability test

        outbreaks = 0




        probOut = 0
        probCount = 0 

        c = 0

        while(c < len(lots)):

            probOut += outbreakChances[c]
            probCount += 1
            #print(wMath.random_test(outbreakChances[c]))

            if(wMath.random_test(outbreakChances[c])):
                outbreaks += 1
                lots = list_splice(lots, c, 1)
                outbreakChances = list_splice(outbreakChances, c, 1)
                c -= 1
            c += 1
            #print(outbreaks)

        probOut = probOut / probCount
        #print("Average Probability of outbreak > " + str(probOut))




        outbreak_cost = 0

        for i in range(1, outbreaks + 1):
            # print("outbreaks" + str(outbreaks))
            # print("multiplier" + str(self.statistics["outbreak_multiplier"]))
            #print("outbreak cost: " + str(outbreak_cost))

            outbreak_cost += 10000 * self.statistics["outbreak_multiplier"]
            # Updated because 2^n is to great so max is set to 33 being 17 trillion
            if i < 20:
                self.statistics["outbreak_multiplier"] *= 2
        
        # print("lots:" + str(len(lots)))
        # print("outbreak Cost" + str(outbreak_cost))
        # print("Price" + str(price))
        self.balance += (int(wConst.PRICES["SuccessfulLot"]) * len(lots)) - int(outbreak_cost) - int(price)

        #print("balance: " + str(self.balance))

        self.statistics["cycles"] += float(amount)
        self.statistics["outbreaks"] += outbreaks


        results = {
            "lots": float(amount),
            "lotsPassed": len(lots),
            "rawCaught": rawCaught,
            "finishedCaught": finishedCaught,
            "outbreaks": outbreaks,
            "gain": (wConst.PRICES["SuccessfulLot"] * len(lots)) - outbreak_cost - price,
            "costPerLot": costNum
        }

        self.statistics["steps"] +=1 

        if(self.balance > self.statistics["peak"]):
            self.statistics["peak"] = self.balance

        if (self.balance < 0):
            print("Game Over Triggered on Server")

        return results
        
            
        


