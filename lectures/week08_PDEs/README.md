# Week 8: Finite Difference Methods for PDEs

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce finite difference methods for solving partial differential equations (PDEs), focusing on elliptic and parabolic equations.  
Students will learn solution techniques, boundary conditions, and stability considerations for practical engineering problems.

---

## 📘 Lecture 1 – Finite Difference Methods: Elliptic Equations

### Learning Outcomes
- Understand elliptic PDEs, particularly the Laplace equation  
- Apply finite difference methods for discretizing and solving elliptic equations  
- Implement boundary conditions and control-volume approach  
- Use software tools for solving elliptic equations  

### Lecture Flow
1. **Introduction to Elliptic Equations (10 min)**  
   - Definition and examples: Laplace and Poisson equations  
   - Applications: steady-state heat conduction, electrostatics  

2. **The Laplace Equation (20 min)**  
   - Formulation in 2D: \( \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0 \)  
   - Discretization using finite differences  
   - Example: 5-point stencil  

3. **Solution Techniques (25 min)**  
   - Iterative methods: Gauss-Seidel, Successive Over-Relaxation (SOR)  
   - Convergence criteria  
   - *Exercise:* Solve a simple 2D Laplace problem manually  

4. **Boundary Conditions (25 min)**  
   - Dirichlet, Neumann, and mixed boundary conditions  
   - Implementation in finite difference schemes  

5. **Control-Volume Approach (15 min)**  
   - Concept of control volumes and flux balance  
   - Comparison with standard finite difference method  

6. **Software Applications (10 min)**  
   - Using MATLAB, Python, or specialized PDE solvers  
   - Demonstration of solving a Laplace equation  

---

### 🎓 Suggested Homework
- Solve a 2D Laplace equation with Dirichlet boundary conditions using Gauss-Seidel  
- Compare results with a small MATLAB/Python program  
- Explore the effect of grid size on accuracy and convergence  

---

## 📘 Lecture 2 – Finite Difference Methods: Parabolic Equations

### Learning Outcomes
- Understand parabolic PDEs, particularly the heat conduction equation  
- Apply explicit, implicit, and Crank-Nicolson finite difference methods  
- Extend solutions to two spatial dimensions  

### Lecture Flow
1. **Introduction to Parabolic Equations (10 min)**  
   - Formulation of the 1D heat equation: \( \frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2} \)  
   - Applications: transient heat conduction, diffusion problems  

2. **Explicit Methods (25 min)**  
   - Forward-time central-space (FTCS) scheme  
   - Stability criteria (Courant condition)  
   - Example: transient temperature distribution  

3. **Simple Implicit Method (20 min)**  
   - Backward-time central-space (BTCS) scheme  
   - Unconditional stability  
   - Example: same problem solved implicitly  

4. **Crank-Nicolson Method (25 min)**  
   - Combination of explicit and implicit methods  
   - Second-order accuracy in time  
   - Example: compare FTCS, BTCS, and Crank-Nicolson  

5. **Parabolic Equations in Two Spatial Dimensions (20 min)**  
   - Extension to 2D heat conduction  
   - ADI (Alternating Direction Implicit) method overview  
   - Practical considerations for boundary conditions  

6. **Summary & Discussion (10 min)**  
   - Comparison of explicit vs implicit vs Crank-Nicolson methods  
   - Guidelines for method selection and stability  

---

### 🎓 Suggested Homework
- Solve 1D transient heat conduction using FTCS, BTCS, and Crank-Nicolson  
- Extend Crank-Nicolson to a simple 2D heat conduction problem  
- Analyze effect of time step and grid spacing on stability and accuracy  

---

## 🧭 Instructor Notes
- Emphasize stability criteria for explicit schemes  
- Use visualization tools to show temperature evolution over time  
- Highlight advantages of implicit and Crank-Nicolson schemes for stiff problems  
- Encourage hands-on coding in Python, MATLAB, or similar software  
