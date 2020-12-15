#coding: utf-8

import pandas as pd
alunosDTC = {"nome": ['Renato','Roberto','Pedro','Jo�o','Carlos'],
           "notas": [4,7,5,5,9],
           "aprovado": ['não', 'sim', 'não', 'não', 'sim']}
alunosDF = pd.DataFrame(alunosDTC)
#print(alunosDF)
#print(alunosDF.shape)
#print(alunosDF.describe())
print(alunosDF.loc[alunosDF['nome']=='Renato'])