from python.EvaluadorFunciones import Evaluar
from python.graf import grafica
def BusquedasIncrementales(funcion,x0,delta,iteracion):
    fx0 = Evaluar(funcion,x0)
    x1= x0 + delta
    fx1 = Evaluar(funcion,x1)
    i=0 
    list1 = list()
    list2 = list()
    if Evaluar(funcion,x0) == 0.0:
        return f"La raiz esta en x0 = {x0}", False
    while (fx0 * fx1) > 0 and  i < iteracion :
        x0 = x1 
        fx0 = fx1 
        x1= x0 + delta
        fx1 = Evaluar(funcion,x1)
        list1.append(x1)
        list2.append(fx1)
        i = i + 1
    if fx1:
        respuesta = f"x1 es raiz: {x1}"
    elif fx1 * fx0 < 0:
        respuesta = f"Entre x0 = {x0} y x1 = {x1} hay almenos una raiz"
    else:
        respuesta = "No hay solucion"

    datos = {'x0':x0, 'f(x0)':fx0, 'x1':x1, 'f(x1)':fx1,'iteraciones':i,'Respuesta':respuesta}
    graf = grafica([(list1,list2)])

    return datos, graf
