import pandas as pd
import matplotlib.pyplot as plt

nqueens = pd.read_csv('data/wine/nqueens_results.csv')
nqueens.drop(columns="Unnamed: 9", inplace=True)

# fig, ax = plt.subplots()
#
input_variation = nqueens[['Algorithm','N','Fitness Score']][nqueens['N'] == 50]
# input_variation.set_index('Algorithm',inplace=True)
ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='N', y='Fitness Score', kind='scatter', label='GA', c='red')
input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='N', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
input_variation[input_variation['Algorithm'] == 'SA'].plot(x='N', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='blue')
input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='N', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
plt.xlabel('N = 50')
plt.title('Comparing Algorithms')

# #
#
# var = nqueens[['Algorithm','Fitness Score', 'Param2', 'Param1']][nqueens['N'] == 50]
# ax = var[(var['Algorithm'] == 'GA') & (var['Param1']==200)].plot(x='Param2', y='Fitness Score', label='Population=200', kind='scatter', c='b')
# var[(var['Algorithm'] == 'GA') & (var['Param1']==400)].plot(x='Param2', y='Fitness Score', label='Population=400', kind='scatter', c='r', ax= ax)
# # # var[(var['Algorithm'] == 'GA') & (var['Param1']==500)].plot(x='Param2', y='Fitness Score', label='Population=500', kind='scatter', c='y', ax= ax)
#
# plt.title('Genetic Algorithms - Varying Parameters')
# plt.xlabel('# Crossovers')

# var = nqueens[['Algorithm','Fitness Score', 'Param2', 'Param1']][nqueens['N'] == 50]
# ax = var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==200)].plot(x='Param2', y='Fitness Score', label='Population=200', kind='scatter', c='b')
# var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==400)].plot(x='Param2', y='Fitness Score', label='Population=400', kind='scatter', c='r', ax= ax)
## plt.title('MIMIC - Varying Parameters')
# plt.xlabel('Population Kept')


var = nqueens[['Algorithm','Train time', '# Iterations', 'Param1']][nqueens['N'] == 50]
ax = var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==200)].plot(x='# Iterations', y='Train time', label='Population=200', kind='scatter', c='b')
var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==400)].plot(x='# Iterations', y='Train time', label='Population=400', kind='scatter', c='r', ax= ax)
# plt.title('MIMIC - Varying Parameters')
# plt.xlabel('Population Kept')


plt.legend(loc='best')
plt.show()
#
