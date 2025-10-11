# Week 5: Numerical Integration

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce numerical integration techniques for approximating definite integrals and solving engineering problems.  
Students will learn classical Newton-Cotes formulas, Romberg, adaptive, and advanced quadrature methods.

---

## 📘 Lecture 1 – Newton-Cotes Integration Formulas

### Learning Outcomes
- Apply the trapezoidal and Simpson’s rules for numerical integration  
- Handle integration with unequal segments  
- Understand open formulas and multiple integrals  

### Lecture Flow
1. **Introduction (10 min)**  
   - Motivation: numerical integration when analytical methods are difficult  
   - Applications: physics, engineering, and statistics  

2. **Trapezoidal Rule (30 min)**  
   - Single and composite trapezoidal rule  
   - Error estimation  
   - Example: Integrate \( f(x) = e^{-x^2} \)  

3. **Simpson’s Rules (30 min)**  
   - 1/3 and 3/8 rules  
   - Composite Simpson’s rule  
   - Example: Integrate \( f(x) = \sin(x) \) over [0, π/2]  

4. **Integration with Unequal Segments (15 min)**  
   - Weighted approach for non-uniform grids  
   - Example: Experimental dataset  

5. **Open Integration Formulas (15 min)**  
   - Endpoints not included, useful for unreliable boundary data  

6. **Multiple Integrals (10 min)**  
   - Concept of double and triple integrals  
   - Applications in surface and volume computations  

---

## 📘 Lecture 2 – Integration of Equations (Advanced Methods)

### Learning Outcomes
- Implement Newton-Cotes algorithms for solving equations  
- Apply Romberg and adaptive quadrature for higher accuracy  
- Use Gauss quadrature, improper integrals, and Monte Carlo methods  

### Lecture Flow
1. **Newton-Cotes Algorithms for Equations (10 min)**  
   - Closed and open formulas for approximating integrals  

2. **Romberg Integration (20 min)**  
   - Richardson extrapolation for refined integral estimates  
   - Example: Integrate \( f(x) = e^x \)  

3. **Adaptive Quadrature (20 min)**  
   - Subdivide intervals based on error tolerance  
   - Example: Adaptive Simpson’s method  

4. **Gauss Quadrature (20 min)**  
   - Optimal points and weights for high-accuracy integration  
   - Example: 2-point Gaussian quadrature  

5. **Improper Integrals (10 min)**  
   - Infinite limits or singularities  
   - Example: \( \int_1^\infty 1/x^2 dx \)  

6. **Monte Carlo Integration (15 min)**  
   - Random sampling for multidimensional integrals  
   - Example: Estimate π using random points  

---

### 🎓 Suggested Homework
- Implement Trapezoidal, Simpson, and Romberg integration methods  
- Compare fixed-step vs adaptive quadrature results  
- Apply Monte Carlo integration to a 2D area estimation  
