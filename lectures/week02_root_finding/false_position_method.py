def false_position(f, xl, xu, es=0.01, imax=10):
    """
        f   : function whose root is to be found
        xl  : lower guess
        xu  : upper guess
        es  : stopping criterion (%)
        imax: maximum number of iterations
    """
    if f(xl) * f(xu) > 0:
        print("Invalid initial bracket: f(xl)*f(xu) > 0")
        return None

    iter = 0
    xr_old = xl
    ea = 100  

    print(f"{'Iter':<5}{'xl':<10}{'xu':<10}{'xr':<10}{'f(xl)':<12}{'f(xu)':<12}{'f(xr)':<12}{'ea (%)':<10}")
    print("=" * 80)
    while ea > es and iter < imax:
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu)) 
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100

        print(f"{iter:<5}{xl:<10.4f}{xu:<10.4f}{xr:<10.4f}{f(xl):<12.4f}{f(xu):<12.4f}{f(xr):<12.4f}{ea:<10.4f}")
        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            ea = 0  # root found
        xr_old = xr

    print(f"\nApproximate root = {xr:.6f}")
    print(f"f(xr) = {f(xr):.6f}")
    print(f"Approx. relative error = {ea:.4f}% after {iter} iterations")

    return xr

def f(x):
    return x**3 + 4*x**2 - 10

false_position(f, xl=1, xu=2, es=1, imax=10)
