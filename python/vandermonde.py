from numpy import array, matrix, zeros
from python.gaussPipPar import gaussPipPar

def vandermonde(matrizX, matrizY):

    s = (len(matrizX),len(matrizX))
    matriz = zeros(s)
    for i in range(len(matrizX)):
        cont = 0
        for j in range(len(matrizX)-1,-1,-1):
            matriz[i][cont] = matrizX[i]**j
            cont += 1

    return gaussPipPar(matriz, matrizY)
