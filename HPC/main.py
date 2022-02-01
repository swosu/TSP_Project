import random
from array import array
#from GuessAndCheck import guessAndCheck
from LoadMap import loadMap

print("Welcome to the Shortest Path program.")

cityCount = 6
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
print(cityMap)
print("If I didn't print out a city matrix, run me again!")

startingCity = 0
#startingCity = random.randint(0, cityCount)
print(startingCity)

#search array pass in startingCity
#find min value based on row and column
def minRow(cityMap, cityCount):
    print("{", end="")
    for i in range(cityCount):
        min = cityMap[i][0]

        for j in range(1,cityCount,1):
            if (cityMap[i][j] < min):
                min = cityMap[i][j]
        print(min)
    print("}")

print(minRow(cityMap, cityCount))

#Need way to remove so that can't repeat city

print('test case')
startingCity = 0
print('City: ' + str(cityMap[0]))



for j in range(0, len(cityMap[startingCity])):

       # print('City: ' + str(j))
        print('j: ' + str(j))
        print('nextCityDistance: ' + str(cityMap[1][j]))
        if int(cityMap[1][j]) < int(cityMap[1][j+1]):
            print('Index at City[ ' + str(j) + '] is smaller')
            temp = cityMap[1][j]
            print(temp)












