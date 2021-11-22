'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from generateMatrix import NewMatrix
import pandas as pd

maxIterations = 10000


def main(matrix):

    print('Primeira matriz')
    print(matrix.getMatrix(), '\n')

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

    print('Nova geracao')
    print(newGen.astype(int), '\n')

    matrix.setMatrix(newGen.astype(int))
    matrix.setCost()
    matrix.setBestCost()

    print(matrix.getMatrix(), '\n')


if __name__ == '__main__':
    m = NewMatrix()
    main(m)