import numpy as np

def gauss_elimination(a, b):
    n = len(b)
    
    # Forward Elimination
    for k in range(n-1):
        for i in range(k+1, n):
            if a[k][k] == 0:
                raise ZeroDivisionError("Division by zero! Pivot element is zero.")
            factor = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - factor * a[k][j]
            b[i] = b[i] - factor * b[k]
    
    # Back Substitution
    x = np.zeros(n)
    x[n-1] = b[n-1] / a[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += a[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i][i]
    
    return x

# Example usage
A = np.array([[3.0, 2.0, -4.0],
              [2.0, 3.0, 3.0],
              [5.0, -3.0, 1.0]])
B = np.array([3.0, 15.0, 14.0])

solution = gauss_elimination(A.copy(), B.copy())
print("Solution:", solution)
