# -*- coding: utf-8 -*-
"""numpyaula2ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OR9R1Z_ECUEQ3LqLlPO4WnnyeL83JieU
"""

pandas

!pip install pandas
import pandas as pd
data={'Nome': ['Alice','Bob', 'Carlos'], 'Idade': [25,30,22], 'Salário':[50000, 60000, 70000]}
df=pd.DataFrame(data)
print(df.head())
media_salarial=df['Salário'].mean()
print(f'Média salarial:{media_salarial}')

#filtando dados no dataframe
filtrados=df[df['Idade']>28]
print('pessoas com mais de 28 anos:', filtrados)

import numpy as np
#criando um array numpy
valores=np.array([10,20,30,40,50])

#operações básicas
print('Soma:', np.sum(valores))
print('Média:', np.mean(valores))
print('Desvio padrão:', np.std(valores))

import pandas as pd

#criando um dataframe com valores ausentes
data={'Nome':['Ana', 'Alice', 'Bruno', 'Carlos', 'Sara', None], 'Idade':[28, None, 23,33,45,34], 'Salário':[5000,6000,5600,None,6900,4500]}
df=pd.DataFrame(data)

#exibindo o dataframe original (com os valores ausentea)
print(df)

#removendo linhas com valores ausentes
df_limpo=df.dropna()
print(df_limpo)

#preenchendo valores ausentes com a média da coluna:
df['Idade']=df['Idade'].fillna(df['Idade'].mean())
df['Salário']=df['Salário'].fillna(df['Salário'].mean())
print (df)

from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Criando um DataFrame
data = {'Idade': [20, 30, 40, 50],
        'Salário': [20000, 50000, 80000, 110000]}
df = pd.DataFrame(data)

# Normalizando os dados para ficar entre 0 e 1
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)


print(df)


print(df_normalizado)