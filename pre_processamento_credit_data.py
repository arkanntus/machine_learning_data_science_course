# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 21:02:48 2019

@author: arkan
"""
import pandas as pd
base = pd.read_csv('credit-data.csv')

base.describe()

base.loc[base['age'] < 0]

# apagar a coluna
base.drop('age', 1, inplace=True)

# apagar somente os registros com problema
base.drop(base[base.age < 0].index, inplace=True)

# preencher os valores manualmente

# preencher os valores com a média
base.mean()
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92