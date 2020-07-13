import Session as wSess
import Constants as wConst
import sys
import json

def simulate(GAP, Process, rawTests, finishedTests, variable):
    s = wSess.Session(54321)
    s.selections.GAP_Selection = GAP
    s.selections.Process_Selection = Process
    s.selections.rawTests = rawTests
    s.selections.finishedTests = finishedTests

    s.balance = float("inf")

    cycles = 10000
    matrix = []


    if(variable == "GAP"):

        for key in wConst.GAP:
            s.selections["GAP_Selection"] = key
            data = s.cycle(cycles)

            result = json.loads(data)
            result["key"] = key
            matrix.append(result)

    if(variable == "Process"):
        for key in wConst.PROCESS:
            s.selections["Process_Selection "] = key
            data = s.cycle(cycles)

            result = json.loads(data)
            result["key"] = key
            matrix.append(result)
    
    if(variable == "rawTests"):
        for i in range(0, 51):
            print(i)
            s.selections["rawTests"] = i
            data = s.cycle(cycles)

            result = json.loads(data)
            result["key"] = i

            matrix.append(result)
    
    if(variable == "finishedTests"):
        for i in range(0, 51):
            print(i)
            s.selections["finishedTests"] = i
            data = s.cycle(cycles)

            result = json.loads(data)
            result["key"] = i

            matrix.append(result)

    return matrix