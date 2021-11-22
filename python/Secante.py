from python.EvaluadorFunciones import Evaluar

def Secante(x0,x1,e,n,funcion):
    i = 1
    condicion = True
    while condicion:
        if Evaluar(funcion,x0) == Evaluar(funcion,x1):
            return 'Ey ya te dije que cuidado con la division por 0 ヽ(＃`Д´)ノ', True 

        x2 = x0 - (x1-x0)*Evaluar(funcion,x0)/( Evaluar(funcion,x1) - Evaluar(funcion,x0) ) 
        x0 = x1
        x1 = x2
        i = i + 1
        
        if i > n:
            respuesta = 'Nada, no converge (╥﹏╥)'
            break

        condicion = abs(Evaluar(funcion,x2)) > e

    respuesta = f'La raiz es: {x2:0.8f} ＼(＾▽＾)／'
    datos={'x' : x2, 'Iteraciones' : i, 'Respuesta' : respuesta, 'Error' : abs(Evaluar(funcion,x2))}
    return datos, False
