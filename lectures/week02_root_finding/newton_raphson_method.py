import math

def newton_raphson(x0, es, imax):
    """
    Newton-Raphson Method to find root of f(x) = e^(-x) - x

    Parameters:
        x0   : initial guess
        es   : desired relative error (%) for stopping
        imax : maximum number of iterations

    Returns:
        xr   : estimated root
        ea   : approximate relative error (%)
        iter : number of iterations
    """

    def f(x):
        return math.exp(-x) - x       

    def df(x):
        return -math.exp(-x) - 1    

    iter = 0
    xr = x0
    ea = 100.0  

    while True:
        xrold = xr
        xr = xrold - f(xrold) / df(xrold) 
        iter += 1

        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100 

        if ea < es or iter >= imax:
            break

    return xr, ea, iter

root, error, iterations = newton_raphson(x0=0.5, es=0.0001, imax=20)
print(f"Estimated root = {root:.6f}")
print(f"Approximate relative error = {error:.6f}%")
print(f"Iterations = {iterations}")
