'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from random import shuffle, uniform, random
import pandas as pd


class NewMatrix:
    def __init__(self):
        self.distanceDictionary = {}
        self.matrix = self.setMatrix(None)
        self.populationCost = pd.DataFrame(self.setCost())
        self.bestCost = self.setBestCost()
        self.bestValue = self.getBestCost().min()
        self.bestSolution = self.getBestCost().head(1)

    # gets e sets
    def getMatrix(self):
        return self.matrix.copy()

    def getCost(self):
        return self.populationCost.copy()

    def getBestCost(self):
        return self.bestCost

    def getDistanceDictionary(self):
        return self.distanceDictionary.copy()

    def getDistanceByKey(self, key):
        return self.distanceDictionary[key]

    def setDistanceDictionary(self, key, value):
        self.distanceDictionary[key] = value

    # Inverte a chave(cidadeInicial-cidadeObjetivo),
    # para que a ida e volta tenham a mesma distancia
    def invertedKey(self, key):
        left = key.split('-')[0]
        right = key.split('-')[1]
        return (f'{right}-{left}')

    # Gera a matriz 20x20
    def setMatrix(self, data):
        if (data is None):
            matrix = []
            list = [i for i in range(1, 21)]

            for number in list:
                shuffledList = list.copy()
                shuffle(shuffledList)
                matrix.append(shuffledList)

            return pd.DataFrame(matrix)
        else:
            self.matrix = data

    # Verifica se a chave passada ja existe,
    # caso não exista, cria uma nova
    def generateDistance(self, key):
        if key in self.getDistanceDictionary():
            return self.getDistanceByKey(key)
        else:
            value = uniform(0, 1)
            self.setDistanceDictionary(key, value)
            invertedKey = self.invertedKey(key)
            self.setDistanceDictionary(invertedKey, value)
            return value

    # Copia a primeira coluna do DataFrame na ultima,
    # Calcula as distâncias, e as soma na coluna "Cost"
    def setCost(self):
        noneList = [None for i in range(0, 20)]
        distances = [noneList.copy() for i in range(0, 20)]
        df = self.getMatrix()
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

    # Coleta os 10 melhores resultados
    def setBestCost(self):
        df = self.getCost()
        df = df.drop(columns=['start'])
        df = df.sort_values('cost')
        df = df.head(10)

        return df

    # Roleta, para selecionar os pais
    def dadSelector(self, df_BestCost):
        addedCosts = df_BestCost['cost'].sum(axis=0)
        cols = df_BestCost.index
        sortedVal = random() * addedCosts
        sumVals = 0
        i = 0

        while i < len(df_BestCost) and sumVals < sortedVal:
            sumVals += df_BestCost['cost'][cols[i]]
            i += 1

        if (i == len(df_BestCost)):
            return i - 1

        return i

    # Retorna os pais em um dataframe
    def dadsNewGen(self, dad_index, mom_index):
        df_BestCost = self.getBestCost()
        indexes = df_BestCost.index
        i = 0

        for ind in list(indexes):
            df_BestCost.rename(index={ind: str(i)}, inplace=True)
            i += 1

        dad = df_BestCost.iloc[dad_index]
        mom = df_BestCost.iloc[mom_index]

        concat = pd.concat([dad, mom], axis=1)
        dads = pd.DataFrame(concat).transpose()

        return dads

    # Troca algum cromossomo do pai pelo da mãe
    def changeValues(self, dads, column):
        index = list(dads.index)
        valueDad = dads[column][index[0]]
        valueMom = dads[column][index[1]]

        dads[column][index[0]] = valueMom
        dads[column][index[1]] = valueDad

        return dads, valueDad

    # Verifica se o cromossomo possui dois valores iguais
    def duplicated(self, dads, valueDads, randomColumn):
        row = []

        for i in range(0, 20):
            try:
                if (dads[i][1] == valueDads):
                    row.append(i)
            except (ValueError):
                pass

        if (randomColumn in row):
            row.remove(randomColumn)

        if (len(row) == 0):
            return -1

        return row[0]

    # Realiza o crossover até não terem mais cromossomos repetidos
    def crossover(self, dads):
        randomColumn = int(uniform(0, 19))

        dads, valueDads = self.changeValues(dads, randomColumn)

        while (True):
            row = self.duplicated(dads, valueDads, randomColumn)

            if (row > -1):
                dads, valueDads = self.changeValues(dads, row)
                randomColumn = row
            else:
                break

        sons = dads.drop(columns=['cost'])
        return sons