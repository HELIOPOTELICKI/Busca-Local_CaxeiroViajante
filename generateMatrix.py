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

    def setMatrix(self):
        matrix = []
        list = [i for i in range(1, 21)]

        for number in list:
            shuffledList = list.copy()
            shuffle(shuffledList)
            matrix.append(shuffledList)

        return matrix

    def setCost(self):
        distances = []
        for i in range(1, 21):
            aux = [uniform(0.0, 1.0) for i in range(1, 21)]
            distances.append(aux)

        costMatrix = pd.DataFrame(distances)
        costMatrix = costMatrix.sum(axis=1)
        df = self.getMatrix()
        df = df.copy()
        df['start'] = pd.DataFrame(df, columns=[0])
        df['cost'] = costMatrix
        df = df.sort_values('cost')

        return df

    def setBestCost(self):
        return self.getCost().head(10)
