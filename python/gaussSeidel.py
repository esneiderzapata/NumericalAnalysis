from numpy import zeros, ones, abs, max, array 
def gaussSeidel(a, B, tol, iter):       
    n = len(a)      
    X=zeros(n)
    a = array(a)
    B = array(B)
    diferencia = ones(n,dtype=float)
    err = 2*tol
    itera = 0
    #stops if error is less than error or exceds iterations
    while not(err<=tol or itera>iter):
        for i in range(0,n,1):
            suma=0
            for j in range(0,n,1):
                if(j!=i):
                    suma=suma+a[i,j]*X[j]
            nuevo=(B[i]-suma)/a[i,i]
            diferencia[i]=abs(nuevo-X[i])
            X[i]=nuevo
        err = max(diferencia)
        itera = itera+1               
    
    respuesta = ''
    for i in range(n):
        respuesta +=  f'solution is:  X{i} = {X[i]:0.3f}\n' 

    return respuesta  