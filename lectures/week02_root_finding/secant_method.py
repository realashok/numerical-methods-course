import math

def f(x):
    return math.exp(-x) - x

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero!")
            return None
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        ea = abs((x2 - x1)/x2)
        print(f"Iteration {i+1}: x = {x2}, error = {ea}")
        if ea < tol:
            return x2
        x0, x1 = x1, x2
    print("Method did not converge.")
    return None

x_minus1 = 0
x0 = 1.0
root = secant_method(x_minus1, x0)
print(f"\nEstimated root: {root}")
