iteration = 0
solution = 1
term = 1
approximate_error = 100
maxiter = 100
stopping_error = 0.0001

x = float(input("Enter the value of x for finding e^x: "))

while approximate_error > stopping_error and iteration < maxiter:
    iteration += 1
    term *= (x/iteration)
    old_solution = solution 
    solution += term
    approximate_error = abs((solution-old_solution)/solution)*100

    print(f"Iteration: {iteration} | Current Solution: {solution} | Approximate Error: {approximate_error}") 

print("="*100)
print("\nFinal Result:")
print(f"e^{x} ≈ {solution:.10f}")
print(f"Approximate relative error = {approximate_error:.6f}% after {iteration} iterations")