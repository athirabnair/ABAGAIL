import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
""" 
N-Queens
"""

# nqueens = pd.read_csv('data/wine/nqueens_results.csv')
# nqueens.drop(columns="Unnamed: 9", inplace=True)
#


# #
# input_variation = nqueens[nqueens['N'] == 50]
# # input_variation.set_index('Algorithm',inplace=True)
# ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='N', y='Fitness Score', kind='scatter', label='GA', c='red')
# input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='N', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
# input_variation[input_variation['Algorithm'] == 'SA'].plot(x='N', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='blue')
# input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='N', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
# plt.xlabel('N = 50')
# plt.title('Comparing Algorithms')
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
#
#

# ### Time variation
# var = nqueens#[nqueens['N'] == 50]
# col = 'Test time'
# ax = var[var['Algorithm'] == 'GA'].plot(x='N', y=col, kind='scatter', label='GA', c='red')
# var[var['Algorithm'] == 'RHC'].plot(x='N', y=col, kind='scatter', label='RHC', ax = ax, c='g')
# var[var['Algorithm'] == 'SA'].plot(x='N', y=col, kind='scatter', label='SA', ax = ax, c='blue')
# var[var['Algorithm'] == 'MIMIC'].plot(x='N', y=col, kind='scatter', label='MIMIC', ax = ax, c='y')
# plt.ylabel('Testing Time')
# plt.title('Comparing Testing Times for N-Queens Problem')
#
#



"""
 TSP 
 
"""
#
# tsp = pd.read_csv('data/wine/tsp_results.csv')
# tsp['Distance Score'] = 1/tsp['Fitness Score']
#
# # input_variation = tsp[['Algorithm','N','Fitness Score', 'Distance Score']][tsp['N'] == 50]
# # # input_variation.set_index('Algorithm',inplace=True)
# # ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='N', y='Fitness Score', kind='scatter', label='GA', c='r')
# # input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='N', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
# # input_variation[input_variation['Algorithm'] == 'SA'].plot(x='N', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='b')
# # input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='N', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
# # plt.xlabel('N = 50')
# # plt.title('Comparing Algorithms')
#
#
#
#
# var = tsp[tsp['N'] == 100]
# ax = var[(var['Algorithm'] == 'GA')& (var['Param1']==2000) & (var['Param3'] != 250) & (var['Param2']==1500) ].plot(x='Param3', y='Fitness Score', kind='scatter', c='purple')
# var[(var['Algorithm'] == 'SA') & (np.isclose(var['Param2'], .999))].plot(x='Param1', y='Fitness Score', kind='scatter', c='r', logx=True)
# var[(var['Algorithm'] == 'MIMIC') & (var['Param1'] == 200)].plot(x='Param2', y='Fitness Score', kind='scatter', c='g')
#
# plt.title('Genetic Algorithms - Varying Parameters')
# plt.xlabel('# Mutations')


# plt.legend(loc='best')
# plt.show()
#
"""
Knapsack

"""

# k = pd.read_csv('data/wine/knapsack_results.csv')
#
# input_variation = k[(k['Max Weight'] == 50) & (k['Max Volume'] == 50) & (k['# Items'] != 40)]
# # input_variation.set_index('Algorithm',inplace=True)
# ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='# Items', y='Fitness Score', kind='scatter', label='GA', c='r')
# input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='# Items', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
# input_variation[(input_variation['Algorithm'] == 'SA')].plot(x='# Items', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='b')
# input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='# Items', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
# # plt.xlabel('N = 50')
# plt.title('# Items vs Fitness Score')
#

#
# input_variation = k[(k['Max Volume']==50)& (k['# Items'] == 40) & (k['Max Weight'] != 500) ]
# # input_variation.set_index('Algorithm',inplace=True)
# ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='Max Weight', y='Fitness Score', kind='scatter', label='GA', c='r')
# input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='Max Weight', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
# input_variation[(input_variation['Algorithm'] == 'SA')].plot(x='Max Weight', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='b')
# input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='Max Weight', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
# # plt.xlabel('N = 50')
# plt.title('Max Weight vs Fitness Score')
#

#
# input_variation = k[(k['Max Weight']==50) & (k['Max Volume'] != 50)]
# # input_variation.set_index('Algorithm',inplace=True)
# ax = input_variation[input_variation['Algorithm'] == 'GA'].plot(x='Max Volume', y='Fitness Score', kind='scatter', label='GA', c='r')
# input_variation[input_variation['Algorithm'] == 'RHC'].plot(x='Max Volume', y='Fitness Score', kind='scatter', label='RHC', ax = ax, c='g')
# input_variation[(input_variation['Algorithm'] == 'SA')].plot(x='Max Volume', y='Fitness Score', kind='scatter', label='SA', ax = ax, c='b')
# input_variation[input_variation['Algorithm'] == 'MIMIC'].plot(x='Max Volume', y='Fitness Score', kind='scatter', label='MIMIC', ax = ax, c='y')
# # plt.xlabel('N = 50')
# plt.title('Max Volume vs Fitness Score')
#


# var = k[(k['Max Volume']==50)& (k['# Items'] == 40) & (k['Max Weight'] == 50) ]

# ax = var[(var['Algorithm'] == 'SA') & (var['Param1']==1000000000)].plot(x='Param2', y='Fitness Score', label='Population', kind='scatter', c='b')

# ax = var[(var['Algorithm'] == 'GA') & (var['Param1']==200) & (var['Param3'] == 25) & (var['Param2'] != 150)].plot(x='Param2', y='Fitness Score', label='Population=200', kind='scatter', c='orange')
# var[(var['Algorithm'] == 'GA') & (var['Param1'] == 500) & (var['Param3'] == 25)].plot(x='Param2', y='Fitness Score', label='Population=500', kind='scatter', c='g', ax=ax)
# plt.title('Genetic Algorithms - Varying Parameters')
# plt.xlabel('# Crossovers')

# ax = var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==200) & (var['Param2']!=100)].plot(x='Param2', y='Fitness Score', label='Samples generated = 200', kind='scatter', c='brown')
# var[(var['Algorithm'] == 'MIMIC') & (var['Param1']==500) ].plot(x='Param2', y='Fitness Score', label='Samples generated = 500', kind='scatter', c='pink', ax=ax)
# plt.title('MIMIC - Varying Parameters')
# plt.xlabel('Population Kept')



### Time variation
# var = tsp#[nqueens['N'] == 50]
# col = 'Train time'
# ax = var[var['Algorithm'] == 'GA'].plot(x='N', y=col, kind='scatter', label='GA', c='red')
# var[var['Algorithm'] == 'RHC'].plot(x='N', y=col, kind='scatter', label='RHC', ax = ax, c='g')
# var[var['Algorithm'] == 'SA'].plot(x='N', y=col, kind='scatter', label='SA', ax = ax, c='blue')
# var[var['Algorithm'] == 'MIMIC'].plot(x='N', y=col, kind='scatter', label='MIMIC', ax = ax, c='y')
# plt.ylabel('Training Time')
# plt.title('Comparing Training Times for TSP')

# plt.legend(loc='best')
# plt.show()


