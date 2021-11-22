from numpy import zeros
def difDivs (x, y):
    n = len (x)
    matriz = zeros((n,n))
    for i in range(n):
        matriz[i][0] = y[i]
    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            matriz[j][i] = (matriz[j][i-1] - matriz[j-1][i-1]) / (x[i] - x[0])

    respuesta = ''
    for i in range(0,n):
        respuesta += f'({x[i]:0.2f}'
        for j in range(0, i+1):
            respuesta += f' {matriz[i][j]:0.6f}'
        respuesta += ')\n'   
    return respuesta     