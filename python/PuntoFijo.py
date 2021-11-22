from python.EvaluadorFunciones import Evaluar
from python.graf import grafica

def PuntoFijo(x,e, n,funcion):
    i = 1 
    b = Evaluar(funcion,x)
    error = abs(b-x)
    Lista2=list()
    while(error>=e and i<=n ):
        a = b
        b = Evaluar(funcion,a)
        error = abs(b-a)
        Lista2.append(b)
        i = i + 1
    plot=[(range(i-1),Lista2)]
    graf=grafica(plot)
    datos = {'x0' : a, 'x1' : b, 'Iteraciones' : i, 'error' : error}
    return datos, graf 



