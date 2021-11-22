from numpy import zeros,array


def pivoteo_total(Ab,k,n):
    mayor = 0
    fila_mayor = k
    columna_mayor = k
    for r in range(k,n):
        for s in range(k,n):
            if abs(Ab[r][s]) > mayor:
                mayor = abs(Ab[r][s])
                fila_mayor = r
                columna_mayor = s
    if mayor == 0:
        return "El sistema no tiene solución única"
    else:
        if fila_mayor != k:
            Ab[fila_mayor],Ab[k] = Ab[k],Ab[fila_mayor]
        if columna_mayor != k:
            for row in Ab:
                row[k],row[columna_mayor] = row[columna_mayor],row[k]            
    return Ab

def gauss(A,i):
    rows = len(A)
    cols = len(A)+1
    pivote = A[i][i]
    if pivote != 0.0:
        for r1 in range(i+1,rows): 
            multiplicador =A[r1][i]/pivote
            for c in range(i,cols): 
                if abs(A[r1][c]-(multiplicador*A[i][c]))<1e-10:
                    A[r1][c]=0
                else:A[r1][c]=A[r1][c]-(multiplicador*A[i][c])
    return A

def regresiva(Matrix,b):
    matrix = array(Matrix)
    n = len(matrix)
    X = zeros(n)
    X[n-1] = b[n-1]/matrix[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum_ax=0
        for j in range(i+1,n):
            sum_ax+= matrix[i,j]*X[j]
        X[i]=(b[i]-sum_ax)/matrix[i,i]
    return X    

def gaussPipTot(matrix,n):
    for i in range(n):
        xd=pivoteo_total(matrix,i,n)
        matrix = gauss(xd,i)
    b = [fila.pop() for fila in matrix]
    x = regresiva(matrix,b)
    respuesta = ''
    for i in range(n):
        respuesta +=  f'solution is:  X{i} = {x[i]:0.3f}\n' 

    return respuesta    