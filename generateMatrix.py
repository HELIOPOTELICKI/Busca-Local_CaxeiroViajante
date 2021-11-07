from random import shuffle, uniform
import pandas as pd


class NewMatrix:
    def __init__(self):
        self.matrix = pd.DataFrame(self.setMatrix())
        self.populationCost = pd.DataFrame(self.setCost())
        self.bestCost = self.setBestCost()

    def getMatrix(self):
        return self.matrix

    def getCost(self):
        return self.populationCost

    def getBestCost(self):
        return self.bestCost

    def invertedKey(self, key):
        left = key.split('-')[0]
        right = key.split('-')[1]
        return (f'{right}-{left}')

    def setMatrix(self):
        matrix = []
        list = [i for i in range(1, 21)]

        for number in list:
            shuffledList = list.copy()
            shuffle(shuffledList)
            matrix.append(shuffledList)

        return matrix

    def setCost(self):
        distances = [[None for i in range(0, 20)] for i in range(0, 20)]
        df = self.getMatrix().copy()
        df['start'] = pd.DataFrame(df, columns=[0])
        distanceDictionary = {}

        for y in range(0, 20):
            for x in range(0, 20):
                cityStart = df[x][y]
                if (x == 19):
                    cityNext = df['start'][y]
                else:
                    cityNext = df[x + 1][y]

                key = (f'{cityStart}-{cityNext}')

                if key in distanceDictionary:
                    distances[y][x] = distanceDictionary[key]
                else:
                    value = uniform(0, 1)
                    distanceDictionary[key] = value
                    invertedKey = self.invertedKey(key)
                    distanceDictionary[invertedKey] = value
                    distances[y][x] = value

        costMatrix = pd.DataFrame(distances)

        costMatrix = costMatrix.sum(axis=1)
        df['cost'] = costMatrix

        return df

    def setBestCost(self):
        df = self.getCost().copy()
        df = df.drop(columns=['start'])
        df = df.sort_values('cost')
        return df.head(10)
