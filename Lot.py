import numpy as np
import math
import random
import wMath as wMath


def gaussianRand():

    generate = True
    if(generate):


        x1 = 0.0
        x2 = 0.0
        w = 0.0


        while True:
            #do code
            x1 = (2.0 * random.uniform(0, 1)) - 1
            x2 = (2.0 * random.uniform(0, 1)) - 1
            w = (x1* x1) + (x2 * x2)
            if(w >= 1.0):
                break

        w = math.sqrt((-2.0 * math.log10(w)) // w)
        
        value0 = x1 * w
        value1 = x2 * w

        result = value0
    else:
        result = value1

    generate = not generate

    return result


def gaussianRandAdj(mean, stddev):
    value = gaussianRand()
    return ((value * stddev ) + mean)


def around(base, distnace):
    x = base * distnace
    y = (x * 2) * random.uniform(0, 1)
    f = (y - x) + base
    return f

probability_of_small_cluster = .1
probability_of_medium_cluster = .05
probability_of_large_cluster = .005

class Lot:



    def __init__(self):
        self.lot_size = 100000
        self.total_cfu = 0
        self.clusters = []
        self.ID = 0

        

    def initialize(self):
        self.cycle() 

    def cycle(self):
        self.compound_background_sources()
        self.compound_small_clusters()
        self.compound_medium_clusters()
        self.compound_large_clusters()
        self.compound_large_event()


    
    def compound_background_sources(self):
        self.total_cfu += abs(wMath.random_distribution(14, 5))


    def compound_small_clusters(self):
        RNG = math.floor(random.uniform(0, 1) * 10000 ) + 1

        if (RNG <= 10000 * probability_of_small_cluster):
            c = Cluster(750)
            self.clusters.append(c)
            self.total_cfu += c.CFUs
            self.compound_small_clusters()


    def compound_medium_clusters(self):
        RNG = math.floor(random.uniform(0, 1) * 10000 ) + 1

        if (RNG <= 10000 * probability_of_medium_cluster):
            c = Cluster(2500)
            self.clusters.append(c)
            self.total_cfu += c.CFUs
            self.compound_medium_clusters()

    def compound_large_clusters(self):
        RNG = math.floor(random.uniform(0, 1) * 10000 ) + 1

        if (RNG <= 10000 * probability_of_medium_cluster):
            c = Cluster(5000)
            self.clusters.append(c)
            self.total_cfu += c.CFUs
            self.compound_large_clusters()

    def compound_large_event(self):
        chance = .00001
        RNG = math.floor(random.uniform(0, 1) * 10000 ) + 1

        if (RNG <= 10000 * chance):
            self.total_cfu += 50000
        
    def info(self, log):
        info = "Lot " + self.ID + " | Total CFUs: " + self.total_cfu + "; CFUs per #: " + (self.total_cfu // self.lot_size) + "; Total Clusters: " + len(self.clusters)
        if (log):
            print(log(info))
        return info

    def getCFUPerPound(self):
        return(self.total_cfu // self.lot_size) 


class Cluster:

    def __init__(self, CFUs): 
        self.CFUs = wMath.random_distribution(CFUs, 3)

    def getCFUs(self):
        return self.CFUs