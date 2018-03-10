import pandas as pd
import matplotlib.pyplot as plt

nqueens = pd.read_csv('data/wine/nqueens_results.csv')
nqueens.drop(columns="Unnamed: 9", inplace=True)

# fig, ax = plt.subplots()

input_variation = nqueens[['Algorithm','N','Fitness Score']][nqueens['N']==120]
# input_variation.set_index('Algorithm',inplace=True)
ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='N', y='Fitness Score', kind='scatter', label='GA', c='red')
input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='N', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
input_variation[input_variation['Algorithm'] == 'SA'].plot(x='N', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='blue')

input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='N', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')

# for key, grp in nqueens.groupby(['Algorithm']):
#     ax = grp.plot(ax=ax, kind='line', x='N', y='Fitness Score', label=key)
# input_variation.plot()
plt.xlabel('N=120')
plt.legend(loc='best')
plt.show()