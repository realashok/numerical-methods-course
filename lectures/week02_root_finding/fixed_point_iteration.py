import math

def fixpt(x0, es, imax): 
    xr = x0
    iter = 0
    ea = 100.0 
    while True:
        xrold = xr
        xr = math.exp(-xrold)     # for f(x) = e^(-x) - x
        iter += 1
        # Compute approximate relative error
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100
        if ea < es or iter >= imax:
            break
    return xr, ea, iter

root, error, iterations = fixpt(x0=0, es=0.5, imax=20)
print(f"Estimated root = {root:.6f}")
print(f"Approximate relative error = {error:.4f}%")
print(f"Iterations = {iterations}")
