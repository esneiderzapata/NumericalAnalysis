from python.EvaluadorFunciones import Evaluar

def RaicesMultiples(x0,e,n,funcion,derivada,segundaDerivada):
    i = 1
    flag = 1
    condicion = True
    while condicion:        
        x1 = x0 - ((Evaluar(funcion,x0) * Evaluar(derivada,x0)) / ((Evaluar(derivada,x0))**2 - Evaluar(funcion,x0) * Evaluar(segundaDerivada,x0)))
        x0 = x1
        i = i + 1
        if i > n:
            flag = 0
            break
        condicion = abs(Evaluar(funcion,x1)) > e
    
    if flag==1:
        respuesta = f'La raiz es: {x1:0.8f}'
    else:
        respuesta =  'Esta funcion no converge'
    datos = {'x' : x1, 'Iteraciones' : i , 'Respuesta' : respuesta, 'Error' : abs(Evaluar(funcion,x1)) }
    return datos
