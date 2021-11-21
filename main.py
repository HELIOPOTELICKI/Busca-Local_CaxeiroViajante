'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from generateMatrix import NewMatrix

m = NewMatrix()
df = m.getBestCost()
print(df, end='\n\n')