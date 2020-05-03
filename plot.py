#project 1
import math
import numpy as np
import  matplotlib.pyplot as plt
#read table
year, tmp, ma5y, ma10y = np.loadtxt('global.csv', delimiter=',',skiprows=6,unpack=True)
#graficos
plt.plot(year,tmp)
plt.savefig('global.pdf')
#mp.clf()
#mp.plot(zcmb,(muth-muobs)/muobs,'r.')
#mp.savefig('diferencias7348.pdf')

