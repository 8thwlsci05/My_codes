'''
file: NA week hw.2
date: Mar.14.2022
phJuan
'''

import numpy as np

tolsiz = 4

coe = np.array([[1, 2, 2, 1],
              [2, -4, 1, -5],
              [2, 1, -2, -4],
              [-1, 2, 1, -2]], dtype = float)
              
res = np.array([17, 8, 10, 17], dtype = float)

for i in range(tolsiz):
    for j in range(i+1,tolsiz):
        res[j] = res[j] - res[i]*(coe[j,i]/coe[i,i])
        coe[j,i:tolsiz] = coe[j,i:tolsiz] - coe[i,i:tolsiz]*(coe[j,i]/coe[i,i])

print(coe)
