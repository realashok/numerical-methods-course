import math

def bisection(f, xl, xu, tol=1e-6, max_iter=100):
    """
    Perform the bisection method to find a root of f(x) = 0 in [xl, xu].
    
    Parameters
    ----------
    f : function
        The function for which the root is sought.
    xl, xu : float
        Lower and upper guesses that bracket the root (f(xl)*f(xu) < 0).
    tol : float, optional
        Absolute tolerance for stopping (default 1e-6).
    max_iter : int, optional
        Maximum number of iterations (default 100).
        
    Returns
    -------
    xr : float
        Estimated root.
    iters : int
        Number of iterations used.
    history : list of dict
        Iteration history for analysis or plotting.
    """
    
    if f(xl) * f(xu) >= 0:
        raise ValueError("Function does not change sign over [xl, xu].")
    
    history = []
    xr = xl
    
    for i in range(1, max_iter + 1):
        xr = (xl + xu) / 2.0
        fl, fr = f(xl), f(xr)
        history.append({
            "iter": i,
            "xl": xl,
            "xu": xu,
            "xr": xr,
            "f(xl)": fl,
            "f(xr)": fr,
            "interval_width": xu - xl
        })
        
        if fr == 0 or (xu - xl)/2.0 < tol:
            break
        if fl * fr < 0:
            xu = xr
        else:
            xl = xr
    return xr, i, history


def f(x):
    return x**3 - x - 2  

xl=float(input("Enter lower bound: "))
xu=float(input("Enter higher bound: "))
root, iters, hist = bisection(f, xl, xu, tol=1e-6)

print(f"Estimated root = {root:.9f}")
print(f"Iterations = {iters}")
print(f"{'iter':>4} {'xl':>10} {'xu':>10} {'xr':>10} {'f(xr)':>12}")
print("-" * 50)
for h in hist[iters-10:iters]:
    print(f"{h['iter']:4d} {h['xl']:10.6f} {h['xu']:10.6f} {h['xr']:10.6f} {h['f(xr)']:12.6g}")
