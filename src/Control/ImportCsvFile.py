"""
In this file the import of file (csv format) is implemented
"""
import csv

def readBeerFile(path):
    """
    :param path: pathname of the file
    :return: list of tuples
    """
    file = open(path, "r")
    allFile = csv.reader(file, delimiter=",")
    count = 0
    totalTuple = []
    for row in allFile:
        if(count != 0):
            totalTuple.append(row)
        count+=1
    file.close()
    return totalTuple

def readUserFile(path):
    """
    :param path: pathname of the file
    :return: list of tuples
    """
    file = open(path, "r")
    allFile = csv.reader(file, delimiter=",")
    count = 0
    totalTuple =[]
    for row in allFile:
        if(count != 0):
            totalTuple.append(row)
        count+=1
    file.close()
    return totalTuple

def readRatingFile(path):
    """
    :param path: pathname of the file
    :return: list of tuples
    """
    file = open(path, "r")
    allFile = csv.reader(file, delimiter=",")
    count = 0
    totalTuple =[]
    for row in allFile:
        if(count != 0):
            totalTuple.append(row)
        count+=1
    file.close()
    return totalTuple

if __name__ == "__main__":
    beers = readBeerFile("D:/Alessandro/Documents/4.Programmi/Programmi Python/Berrer/Beerer/.idea/src/Files/testBeer")
    users = readUserFile("D:/Alessandro/Documents/4.Programmi/Programmi Python/Berrer/Beerer/.idea/src/Files/testUser")
    rating = readRatingFile("D:/Alessandro/Documents/4.Programmi/Programmi Python/Berrer/Beerer/.idea/src/Files/testRecommendation")
    for item in beers:
        print(item[0], item[1])
    for item in users:
        print(item[0], item[1])
    for item in rating:
        print (item[0], item[1])