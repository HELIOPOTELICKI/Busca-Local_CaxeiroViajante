'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from random import shuffle, uniform
import pandas as pd


class NewMatrix:
    def __init__(self):
        self.distanceDictionary = {}
        self.matrix = pd.DataFrame(self.setMatrix())
        self.populationCost = pd.DataFrame(self.setCost())
        self.bestCost = self.setBestCost()

    def getMatrix(self):
        return self.matrix

    def getCost(self):
        return self.populationCost

    def getBestCost(self):
        return self.bestCost

    def getDistanceDictionary(self):
        return self.distanceDictionary

    def getDistanceByKey(self, key):
        return self.distanceDictionary[key]

    def setDistanceDictionary(self, key, value):
        self.distanceDictionary[key] = value

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

    def generateDistance(self, key):
        if key in self.getDistanceDictionary():
            return self.getDistanceByKey(key)
        else:
            value = uniform(0, 1)
            self.setDistanceDictionary(key, value)
            invertedKey = self.invertedKey(key)
            self.setDistanceDictionary(invertedKey, value)
            return value

    def setCost(self):
        noneList = [None for i in range(0, 20)]
        distances = [noneList.copy() for i in range(0, 20)]
        df = self.getMatrix().copy()
        df['start'] = pd.DataFrame(df, columns=[0])

        for y in range(0, 20):
            for x in range(0, 20):
                cityStart = df[x][y]
                if (x == 19):
                    cityNext = df['start'][y]
                else:
                    cityNext = df[x + 1][y]

                key = (f'{cityStart}-{cityNext}')
                distances[y][x] = self.generateDistance(key)

        costMatrix = pd.DataFrame(distances)

        costMatrix = costMatrix.sum(axis=1)
        df['cost'] = costMatrix

        return df

    def setBestCost(self):
        df = self.getCost().copy()
        df = df.drop(columns=['start'])
        df = df.sort_values('cost')
        return df.head(10)