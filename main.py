'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from generateMatrix import NewMatrix
import matplotlib.pyplot as plt
import pandas as pd

maxIterations = 10000


def main(matrix):
    lastIt = 0

    for iteration in range(0, maxIterations):

        if (iteration == lastIt + 1000):
            lastIt += 1000
            print(f'Processando: {int(iteration/100)}%')

        newGen = pd.DataFrame()
        df_BestCost = matrix.getBestCost()

        for i in range(0, 5):
            dad = matrix.dadSelector(df_BestCost)
            mom = matrix.dadSelector(df_BestCost)
            dads = matrix.dadsNewGen(dad, mom)

            sons = matrix.crossover(dads)
            newGen = newGen.append(sons)
            newGen = newGen.append(dads)

        newIndex = [i for i in range(0, 20)]
        newGen.index = newIndex

        newGen = newGen.drop(columns=['cost'])

        matrix.setMatrix(newGen.astype(int))
        matrix.populationCost = matrix.setCost()
        matrix.bestCost = matrix.setBestCost()

        value = matrix.bestCost

        if (matrix.bestValue.cost > value.cost.min()):
            matrix.bestValue = value.min()
            matrix.bestSolution = value.head(1)

    return matrix


if __name__ == '__main__':
    m = NewMatrix()
    print('=_=_= Iniciando mutação =_=_=')
    print('Tamanho da população: 20')
    print('Número de cidades: 20')

    m = main(m)

    print('=_=_= Mutação finalizada =_=_=')
    print(f'Melhor custo: {m.bestValue.cost}')
    df = m.bestSolution.drop(columns=['cost'])
    print(f'Melhor solução: \n{df}')