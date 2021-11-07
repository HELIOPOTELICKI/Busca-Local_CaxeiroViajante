'''
Trabalho 3: Busca Local Caxeiro Viajante
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder
Módulos utilizados: 
    - pip install pandas

'''
from generateMatrix import NewMatrix

m = NewMatrix()

df1 = m.getMatrix()
df2 = m.getCost()
df3 = m.getBestCost()

print(df1, end='\n\n')
print(df2, end='\n\n')
print(df3, end='\n\n')