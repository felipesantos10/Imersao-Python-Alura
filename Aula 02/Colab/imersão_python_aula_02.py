# -*- coding: utf-8 -*-
"""Imersão Python - aula 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O4IlqUg2sXK5e5RnFp2MAOkbfyOm5njQ
"""

import pandas as pd

df_principal = pd.read_excel("/content/[Faça uma cópia para editar] Imersão Python - Tabela de ações (1).xlsx",sheet_name="Principal")
df_principal.head(11)

df_total_de_acoes = pd.read_excel("/content/[Faça uma cópia para editar] Imersão Python - Tabela de ações (1).xlsx",sheet_name="Total_de_acoes")
df_total_de_acoes.head(11)

df_tickets = pd.read_excel("/content/[Faça uma cópia para editar] Imersão Python - Tabela de ações (1).xlsx",sheet_name="Ticker")
df_tickets.head(11)