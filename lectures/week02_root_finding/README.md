# Week 2: Root-Finding Methods – Bracketing and Open Methods

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce numerical methods for finding roots of equations.  
Students will learn both **bracketing** and **open methods**, understand their convergence behavior, and apply them to engineering problems.

---

## 📘 Lecture 1 – Bracketing Methods for Root Finding

### Learning Outcomes
- Understand the concept of root-finding in engineering problems  
- Apply graphical techniques to estimate roots  
- Use bisection and false-position methods effectively  
- Determine good initial guesses through incremental search  

### Lecture Flow
1. **Introduction to Root-Finding (15 min)**  
   - Definition of a root and why it matters in engineering  
   - Real-world examples: equilibrium points, flow balance, circuit analysis  
   - Overview of root-finding categories: bracketing vs open methods  

2. **Graphical Methods (20 min)**  
   - Visual approach to estimating roots  
   - Strengths and limitations  
   - *Example:* Plot \( f(x) = x^3 - 6x^2 + 11x - 6 \)  

3. **Bisection Method (35 min)**  
   - Concept and algorithm  
   - Convergence properties and stopping criteria  
   - *Example:* Find the root of \( f(x) = x^3 - 4x - 9 \) between 2 and 3  
   - *Exercise:* Manual iteration (2–3 steps)  

4. **False-Position (Regula-Falsi) Method (30 min)**  
   - Comparison with bisection  
   - Formula derivation and implementation steps  
   - Discussion: when it performs better/worse  

5. **Incremental Search and Initial Guesses (20 min)**  
   - How to bracket a root  
   - Using sign changes and function evaluation tables  
   - *Example:* Finding initial interval for nonlinear functions  

### 🎓 Assignments / Practice Ideas
- Implement the bisection and false-position methods in a spreadsheet or Python.  
- Compare iteration counts for both methods for the same problem.  
- Homework: Problems on bracketing and error analysis.

---

## 📘 Lecture 2 – Open Methods for Root Finding

### Learning Outcomes
- Apply fixed-point iteration and understand convergence conditions  
- Implement Newton-Raphson, Secant, and Brent’s methods  
- Handle multiple roots and systems of nonlinear equations  
- Compare convergence speed and stability of open methods  

### Lecture Flow
1. **Recap and Discussion (10 min)**  
   - Review of bracketing methods  
   - Limitations leading to open methods  

2. **Simple Fixed-Point Iteration (25 min)**  
   - Concept of transforming \( f(x)=0 \) into \( x=g(x) \)  
   - Convergence condition: \( |g'(x)| < 1 \)  
   - *Example:* \( f(x) = e^{-x} - x \)  
   - *Exercise:* Perform a few iterations manually  

3. **Newton-Raphson Method (35 min)**  
   - Derivation and formula \( x_{i+1} = x_i - f(x_i)/f'(x_i) \)  
   - Geometric interpretation  
   - Fast convergence but derivative dependence  
   - *Example:* \( f(x) = x^3 - 5x + 3 \)  

4. **Secant Method (25 min)**  
   - Derivative-free alternative to Newton-Raphson  
   - Algorithm and convergence rate  
   - *Example:* Same function as Newton-Raphson for comparison  

5. **Brent’s Method Overview (10 min)**  
   - Combines bisection, secant, and inverse quadratic interpolation  
   - Reliability and efficiency in practice  

6. **Multiple Roots and Systems (15 min)**  
   - Modifications to handle repeated roots  
   - Intro to solving nonlinear systems (conceptual only)  

7. **Summary & Discussion (10 min)**  
   - Method comparison table (speed vs stability)  
   - Choosing the right root-finding method for engineering problems  

---

### 🎓 Suggested Homework
1. Implement **Newton-Raphson** and **Secant** methods in code.  
2. Compare convergence rates for the same function using different methods.  
3. Explore **failure cases** where open methods diverge.  
4. Optional: Try **Brent’s method** using built-in library (e.g., `scipy.optimize.brentq`).  

---

## 🧭 Instructor Notes
- Emphasize convergence and error control.  
- Demonstrate numerical results using a calculator or small Python script.  
- Encourage students to visualize function behavior with plots.  
- Discuss trade-offs between robustness (bracketing) and speed (open methods).
