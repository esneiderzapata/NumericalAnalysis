 
 
def lagrange(x, y, xp):
    yp = 0
    n = len(x)
    for i in range(n):
        
        p = 1
        
        for j in range(n):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])
        
        yp = yp + p * y[i] 
    return f'Interpolated value at f({xp:.3f}) is {yp}'
