
import numpy as np

def gaussPipSimp(n, matrix):

    x = np.zeros(n)

    for i in range(n):
        if matrix[i][i] == 0.0:
            return 'Divide by zero detected!'
            
        for j in range(i+1, n):
            mult = matrix[j][i]/matrix[i][i]
            
            for k in range(n+1):
                matrix[j][k] = matrix[j][k] - mult * matrix[i][k]

    x[n-1] = matrix[n-1][n]/matrix[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = matrix[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - matrix[i][j]*x[j]
        
        x[i] = x[i]/matrix[i][i]
    respuesta = ''
    for i in range(n):
        respuesta +=  f'solution is:  X{i} = {x[i]:0.3f}\n' 

    return respuesta