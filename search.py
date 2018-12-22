# search.py

import csv
import sys

filename = "spirits.csv"

class spirit:
    def __init__(self):
        self.name = ""
        self.origin = ""
        self.rating = ""
        self.cat = ""
        self.slots = ""
        self.ability = ""

    def toList(self):
        return [self.name,self.origin,self.rating,self.cat,self.slots,self.ability]

    def __str__(self):
        return self.name + "\t" + self.origin + "\t" + self.rating + "\t" + self.cat + "\t" + self.slots + "\t" + self.ability

all_spirits = []

with open(filename, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=",")
    j = 0
    for row in reader:
        if j != 0:
            all_spirits.append(spirit())
            all_spirits[-1].name = row[0]
            all_spirits[-1].origin = row[2]
            all_spirits[-1].rating = row[2]
            all_spirits[-1].cat = row[3]
            all_spirits[-1].slots = row[4]
            all_spirits[-1].ability = row[5]
        j += 1



uin = "?"
curList = []
while (uin != "q"):
    del curList[:]
    print("\nSearch: n name, f franchise")
    uin = input(">> ")[0].lower()
    if uin == "n":
        n = input("Name: ").lower()
        for sp in all_spirits:
            if n in sp.name.lower():
                curList.append(sp)
        for sp in curList:
            print(sp)
    elif uin == "f":
        f = input("Franchise: ").lower()
        for sp in all_spirits:
            if f in sp.origin.lower():
                curList.append(sp)
        for sp in curList:
            print(sp)
    elif uin == 'q':
        print("Have a nice day")
        sys.exit(0)
    else:
        print("Invalid input")
            
