from matplotlib.pyplot import plot
from python.EvaluadorFunciones import Evaluar
from python.graf import grafica

def Newton(x0,e,n,funcion,derivada):
    i = 1
    flag = 1
    condicion = True
    list1=list()
    while condicion:
        if Evaluar(derivada,x0)  == 0.0:
            return 'Ojo manito con la division por 0', False
        
        x1 = x0 - Evaluar(funcion,x0)/Evaluar(derivada,x0)
        x0 = x1
        i = i + 1
        list1.append(x1)
        if i > n:
            flag = 0
            break
        condicion = abs(Evaluar(funcion,x1)) > e
    
    if flag==1:
        respuesta =f"La raiz es: {x1:0.8f}"
    else:
        respuesta = "Esta funcion no converge"
    plot = [(range (i-1), list1 )]
    graf=grafica(plot)
    datos = {'x' : x1, 'Iteraciones' : i , 'Respuesta' : respuesta, 'Error' : abs(Evaluar(funcion,x1)) }
    return datos, graf