
from python.EvaluadorFunciones import Evaluar
from python.graf import grafica
def Biseccion(x0,x1,e,funcion):
    i = 1
    if Evaluar(funcion,x0) * Evaluar(funcion,x1) > 0.0:
        return'Rango invalido \n Intenta con otros valores.', False
        
    condicion = True
    list1 = list()
    list2 = list()
    list3 = list()
    while condicion:
        x2 = (x0 + x1)/2
        list1.append(Evaluar(funcion,x0))
        list2.append(Evaluar(funcion,x1))
        list3.append(Evaluar(funcion,x2))
        if Evaluar(funcion,x0) * Evaluar(funcion,x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        i = i + 1
        condicion = abs(Evaluar(funcion,x2)) > e
    datos = {'x0': x0,'x1': x1, 
            'f(x0)': Evaluar(funcion,x0),
            'f(x1)': Evaluar(funcion,x1), 
            'iteraciones': i, 
            'raiz' : x2}
    plot=[(range(i-1),list1),(range(i-1),list2),(range(i-1),list3)]
    graf= grafica(plot)
    return datos, graf



    
