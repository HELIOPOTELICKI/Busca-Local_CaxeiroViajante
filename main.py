'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from generateMatrix import NewMatrix
import pandas as pd

# Iterações máxima
maxIterations = 10000


def main(matrix):
    lastIt = 0

    # Itera as 10k vezes
    for iteration in range(0, maxIterations):

        if (iteration == lastIt + 1000):
            lastIt += 1000
            print(f'Processando: {int(iteration/100)}%')

        newGen = pd.DataFrame()
        df_BestCost = matrix.getBestCost()

        # Geração de filhos
        for i in range(0, 5):
            # Coleta os cromossomos do pai
            dad = matrix.dadSelector(df_BestCost)

            # Coleta os cromossomos da mãe
            mom = matrix.dadSelector(df_BestCost)

            # Gera 2 filhos através dos pais
            dads = matrix.dadsNewGen(dad, mom)

            # Realiza o crossover
            sons = matrix.crossover(dads)

            # Adiciona os filhos na nova matriz
            newGen = newGen.append(sons)

            # Adiciona os pais na nova matriz
            newGen = newGen.append(dads)

        # Organiza os índices
        newIndex = [i for i in range(0, 20)]
        newGen.index = newIndex

        # Remove a antiga coluna de custo, para recalcular
        newGen = newGen.drop(columns=['cost'])

        # Salva todas as informações geradas, e reinicia o processo
        matrix.setMatrix(newGen.astype(int))
        matrix.populationCost = matrix.setCost()
        matrix.bestCost = matrix.setBestCost()

        value = matrix.bestCost

        if (matrix.bestValue.cost > value.cost.min()):
            matrix.bestValue = value.min()
            matrix.bestSolution = value.head(1)

    return matrix


if __name__ == '__main__':
    # Ao iniciar o objeto, ja cria a matriz 20x20 e calcula as distâncias
    m = NewMatrix()
    print('=_=_= Iniciando mutação =_=_=')
    print('Tamanho da população: 20')
    print('Número de cidades: 20')

    m = main(m)

    print('Processando: 100%\n')
    print('=_=_= Mutação finalizada =_=_=\n')
    print(f'Melhor custo: {m.bestValue.cost}')
    df = m.bestSolution.drop(columns=['cost'])
    print(f'Melhor solução: \n{df}')