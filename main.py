import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import openpyxl

# zad1
# imiona = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imiona, header=0)
# print(df)
# dzieci = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(dzieci)
# dzieci.plot()
# plt.xticks(np.arange(2000, 2018, step=1))
# plt.xticks(rotation=90)
# plt.show()

# zad2

# imiona = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imiona, header=0)
# print(df)
# dzieci = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(dzieci)
# wykres = dzieci.plot.bar()
# wykres.set_xlabel('Plec')
# wykres.set_ylabel('Mln')
# wykres.legend()
# plt.title('Liczba dzieci danej płci urodzonych w latach 2000-2017')
# plt.xticks(rotation=0)
# plt.yticks(np.arange(0, 4000000, step=500000))
# plt.show()


