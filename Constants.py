GAP = {
    "ASW": {
        "Title": "Accept Suppliers Word",
        "Multiplier": 2,
        "STD": 1,
        "Price": 10
    },
    "USDA": {
        "Title": "USDA Compliant",
        "Multiplier": 1.5,
        "STD": .5,
        "Price": 50
    },
    "LGMA": {
        "Title": "LGMA Compliant",
        "Multiplier": 1,
        "STD": .5,
        "Price": 100
    },
    "SM": {
        "Title": "Super Metrics",
        "Multiplier": .6,
        "STD": .25,
        "Price": 150
    }
}


PROCESS = {
    "CSP1F": {
        "Title": "Controlled Single Pass 1 Flume",
        "Reduction": 1,
        "STD": .2,
        "Price": 500
    },
    "MR1F": {
        "Title": "Managed Recirculation 1 Flume",
        "Reduction": .05,
        "STD": .1,
        "Price": 100
    },
    "CR1F": {
        "Title": "Controlled Recirculation 1 flume",
        "Reduction": .1,
        "STD": 1,
        "Price": 250
    },
    "S1MR2F": {
        "Title": "1st Stage Managed Recirculation 2 Flume",
        "Reduction": .05,
        "STD": 1.5,
        "Price": 150
    },
    "MR2F": {
        "Title": "Managed Recirculation 2 Flume",
        "Reduction": .1,
        "STD": 1,
        "Price": 300
    },
    "CR2F": {
        "Title": "Controlled Recirculation 2 Flume",
        "Reduction": 1.5,
        "STD": .5,
        "Price": 650
    },
    "CR2FWB": {
        "Title": "Controlled Recirculation 2 Flume With Boost",
        "Reduction":  2,
        "STD": .2,
        "Price": 800
    }
}


PRICES = {
    "SuccessfulLot": 1000,
    "PerRawTest": 12,
    "PerFinishedTest": 15
}

UPGRADES = {
    "Lot": {
        "PricePer": 100
    }
}


DEFUALTGAME = {
    "balance": 5000,
    "amountOfLots": 1,
    "GAP_Selection": 'USDA',
    "Process_Selection": 'MR1F',
    "rawTests": 5,
    "finishedTests": 3
}

OUTBREAKREQUIREMENTS = {
    "Sick": 5,
    "Susceptible": 50,
    "Dose": 1
}

MYSQLCREDENTIALS = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "database": "WackBug"
}

def getList(_id):
    _id = _id.upper()

    switcher = {
        "GAP": GAP,
        "PROCESS": PROCESS,
        "PRICES": PRICES,
        "UPGRADES": UPGRADES,
        "DEFAULTS": DEFUALTGAME
    }

    print(switcher.get(_id, "Invalid response"))

