# -*- coding: utf-8 -*-
"""Analisedados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1loS7oy1CS00X2iCR_ozW_KIoVRFYscnq
"""

pip install plotly --upgrade

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

"""**Base dos Dados do COVID-19 Na américa do sul**"""
"""**COVID-19 Database in South America**"""

"""**Fonte: https://www.kaggle.com/anandhuh/covid-in-south-america-latest-data"""

from google.colab import drive
drive.mount('/content/drive')

"""**Exploração dos dados**"""
"""**Data exploration**"""

base_dados = pd.read_csv('/content/covid_south_america.csv')

base_dados

base_dados.describe()

base_dados[base_dados['Total Deaths'] >= 615778.000000]

base_dados[base_dados['Active Cases'] <= 714.000000]

"""**Visualização dos Dados**"""
"""**Data Visualization**"""

grafico = px.scatter_matrix(base_dados, dimensions=['Total Cases', 'Total Deaths', 'Active Cases'])
grafico.show()

"""**Tratamento de valores Faltantes**"""
"""**Treatment of Missing Values**"""

base_dados.isnull()

base_dados.isnull().sum()

base_dados.loc[pd.isnull(base_dados['Total Recovered'])]

base_dados['Total Recovered'].fillna(base_dados['Total Recovered'].mean(), inplace = True)

base_dados.loc[pd.isnull(base_dados['Total Recovered'])]

base_dados.loc[base_dados['Country/Other'].isin([9])]

"""Uma obeservação a se fazer, no código a cima não foi retornado a média pois há uma pouca quantia de dados para o algoritmo do pandas fazer uma media, então não foi retornado, mas se esses dados tivessem mais informações teriamos corrigido os dados faltantes.."""
"""An observation to be made, in the code above the average was not returned as there is a small amount of data for the pandas algorithm to take an average, so it was not returned, but if this data had more information we would have corrected the missing data.."""
