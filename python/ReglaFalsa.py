from python.EvaluadorFunciones import Evaluar

def ReglaFalsa(x0,x1,e,funcion):
    i = 1
    condicion = True
    if Evaluar(funcion,x0) * Evaluar(funcion,x1) > 0.0:
        return 'Rango invalido Intenta con otros valores.', True
    while condicion:
        x2 = x0 - (x1-x0) * Evaluar(funcion,x0)/( Evaluar(funcion,x1) - Evaluar(funcion,x0) )
        if Evaluar(funcion,x0) * Evaluar(funcion,x2) < 0:
            x1 = x2
        else:
            x0 = x2
        i = i + 1
        condicion = abs(Evaluar(funcion,x2)) > e

    datos = {'x0':x0,'x1':x1,'f(x0)':Evaluar(funcion,x0),'f(x1)':Evaluar(funcion,x1),'respuesta':x2, 'iteraciones':i}
    return datos, False
  
