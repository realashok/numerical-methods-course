# Week 3: Solving Systems of Linear Equations

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce direct and iterative methods for solving systems of linear equations, emphasizing Gauss elimination, LU decomposition, and Gauss-Seidel techniques.  
Students will understand algorithmic approaches, numerical stability, and practical implementation.

---

## 📘 Lecture 1 – Gauss Elimination and Variants

### Learning Outcomes
- Understand how linear systems arise in engineering problems  
- Apply Gauss elimination to solve small systems of equations  
- Recognize pitfalls and improve numerical stability  
- Extend elimination to Gauss-Jordan form  

### Lecture Flow
1. **Introduction to Linear Systems (15 min)**  
   - Why systems of equations appear in engineering (e.g., circuits, structures, fluid flow)  
   - Review of matrix notation: \( [A][x] = [b] \)  
   - Difference between direct and iterative methods  

2. **Solving Small Systems (20 min)**  
   - Manual solution of 2×2 and 3×3 systems  
   - Discussion of computational effort and round-off error  

3. **Naive Gauss Elimination (35 min)**  
   - Forward elimination and back substitution  
   - Step-by-step algorithm and example  
   - *Exercise:* Solve a 3×3 system manually  

4. **Pitfalls of Elimination Methods (20 min)**  
   - Round-off errors, division by small pivots, and numerical instability  
   - Example of catastrophic cancellation  

5. **Techniques for Improving Solutions (20 min)**  
   - Partial and complete pivoting  
   - Scaling and normalization  
   - *Demonstration:* Effect of pivoting on solution accuracy  

6. **Gauss-Jordan Method (10 min)**  
   - Extension to obtain both solution and matrix inverse  
   - Comparison with standard Gauss elimination  

### 🎓 Assignments / Practice Ideas
- Solve given 3×3 and 4×4 systems using naive and pivoted elimination.  
- Write a short program or spreadsheet to automate forward/backward substitution.  
- Homework: Discuss how pivoting improves numerical stability.

---

## 📘 Lecture 2 – LU Decomposition and Gauss-Seidel Iteration

### Learning Outcomes
- Factor a coefficient matrix using LU decomposition  
- Use LU factors to efficiently solve systems and compute inverses  
- Understand condition numbers and error sensitivity  
- Apply the Gauss-Seidel method for iterative solution of large systems  

### Lecture Flow
1. **LU Decomposition (35 min)**  
   - Concept of factorizing \( A = LU \)  
   - Forward and backward substitution using \( L \) and \( U \)  
   - Example: Solve a 3×3 system using LU decomposition  
   - *Exercise:* Compute LU factors manually for a small system  

2. **Matrix Inversion via LU (20 min)**  
   - Using LU to compute \( A^{-1} \)  
   - Practical note: Avoid explicit inversion when possible  
   - *Exercise:* Compute inverse of a small 3×3 matrix  

3. **Error Analysis and Conditioning (15 min)**  
   - Sensitivity of solutions to changes in coefficients  
   - Condition number concept and its importance  

4. **Special Matrices (15 min)**  
   - Diagonal, symmetric, and sparse matrices  
   - How structure simplifies computations  

5. **Gauss-Seidel Iterative Method (25 min)**  
   - Algorithm and convergence condition (diagonal dominance)  
   - Comparison with Jacobi method  
   - *Example:* Solve a 3×3 system iteratively  
   - *Exercise:* Perform 3–5 iterations manually  

6. **Solving Systems with Software (10 min)**  
   - Demonstration using Python (NumPy)
   - Discussion: when to use direct vs iterative methods  

7. **Summary & Discussion (10 min)**  
   - Comparison of all methods: Gauss elimination, LU, and Gauss-Seidel  
   - Guidelines for method selection in engineering applications  

---

### 🎓 Suggested Homework
1. Implement **Gauss elimination with partial pivoting** in code.  
2. Factor a given matrix using **LU decomposition** and verify \( A = LU \).  
3. Solve the same system using **Gauss-Seidel** and compare convergence.  
4. Analyze how condition number affects accuracy for ill-conditioned matrices.  

---

## 🧭 Instructor Notes
- Emphasize the difference between direct and iterative approaches.  
- Use small matrix examples for board work; larger ones for computational demos.  
- Highlight numerical issues through examples of unstable systems.  
- Encourage the use of matrix libraries (NumPy, MATLAB) for practice.

