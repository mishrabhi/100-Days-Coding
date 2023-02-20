# Sridhar was a seasoned traveler. He liked to visit new places. More than all he was a meticulous planner. This time he was planning to visit Europe. He wrote down his travel itinerary like as follows:
# If he wanted to visit Madrid, Paris, Munich, Warsaw and Kiev in this order, he would write it down like as:

# Madrid Paris 100

# Paris Munich 200

# Munich Warsaw 150

# Warsaw Kiev 120

# More formally, if he wanted to go from A to B directly and the price is C dollars, then he would write

# A B C

# on a card. Each move was written on a different card. Sridhar was a great planner, so he would never visit the same place twice. Just before starting his journey, the cards got shuffled. Help Sridhar figure out the actual order of the cards and the total cost of his journey.

t = int(input())
while t:
    t -= 1
    n = int(input())
    forwardMap = {}
    totalCost = 0
    inData = [None]*n
    destinations = set()
    sources = set()
    for i in range(n-1):
        inData[i] = input()
        forwardMap[inData[i].split()[0]] = inData[i]
        sources.add(inData[i].split()[0])
        destinations.add(inData[i].split()[1])
        totalCost += int(inData[i].split()[2][:-1])
    start = sources.difference(destinations).pop()
    for i in range(n-1):
        destination = forwardMap[start]
        print(destination)
        start = destination.split()[1]
    print('%d$'%totalCost)