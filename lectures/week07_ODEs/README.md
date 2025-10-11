# Week 7: Numerical Solutions of Ordinary Differential Equations (ODEs)

**Course Duration:** 2 Lectures × 2 Hours  
**Objective:** Introduce numerical methods for solving ODEs, including Euler, Runge-Kutta, and multistep methods.  
Students will learn step-by-step algorithms, stability considerations, and how to handle systems of ODEs.

---

## 📘 Lecture 1 – Euler and Runge-Kutta Methods

### Learning Outcomes
- Understand Euler’s method and its limitations  
- Apply improved Euler (Heun’s) method  
- Implement classical Runge-Kutta methods for first-order ODEs  
- Solve systems of ODEs using Runge-Kutta  

### Lecture Flow
1. **Introduction to ODEs (10 min)**  
   - Motivation: modeling physical systems (mechanical, electrical, chemical)  
   - Types of ODEs: first-order, higher-order, systems  

2. **Euler’s Method (30 min)**  
   - Derivation: \( y_{n+1} = y_n + h f(x_n, y_n) \)  
   - Step-by-step example  
   - Discussion: accuracy, local and global errors  

3. **Improvements of Euler’s Method (20 min)**  
   - Heun’s method / modified Euler  
   - Example: step averaging to improve accuracy  
   - Comparison with classical Euler  

4. **Runge-Kutta Methods (40 min)**  
   - RK2, RK4: derivation and algorithm  
   - Example: Solve \( dy/dx = x + y \)  
   - Implementation tips: step size selection, error control  

5. **Systems of ODEs (20 min)**  
   - Extending RK4 to multiple coupled equations  
   - Example: Predator-prey model or circuit system  

---

### 🎓 Suggested Homework
- Implement Euler, Heun, and RK4 methods for simple ODEs  
- Compare numerical solutions with analytical solutions  
- Solve a system of two coupled first-order ODEs using RK4  

---

## 📘 Lecture 2 – Adaptive and Multistep Methods

### Learning Outcomes
- Understand stiffness in ODEs and its implications  
- Apply adaptive Runge-Kutta methods for error control  
- Learn multistep methods and their advantages for long-time integration  

### Lecture Flow
1. **Adaptive Runge-Kutta Methods (25 min)**  
   - Step size control based on local error estimation  
   - Example: adaptive RK4 for \( dy/dx = x^2 - y \)  
   - Algorithm outline: adjusting \( h \) for accuracy  

2. **Stiffness in ODEs (20 min)**  
   - Definition of stiff equations  
   - Implications for step size and numerical stability  
   - Example: chemical reaction rate equations  

3. **Multistep Methods (35 min)**  
   - Concept: Adams-Bashforth (explicit) and Adams-Moulton (implicit)  
   - Advantages over single-step methods for long-time integration  
   - Example: solving \( dy/dx = -1000y + 3000 - 2000e^{-t} \)  

4. **Comparison and Summary (20 min)**  
   - Single-step vs multistep methods  
   - When to use adaptive methods  
   - Error and stability considerations  

---

### 🎓 Suggested Homework
- Implement adaptive RK4 for a given ODE  
- Solve a stiff ODE using explicit and implicit methods  
- Compare single-step vs multistep method results for long-time simulations  

---

## 🧭 Instructor Notes
- Emphasize stability and error propagation in numerical ODE solutions  
- Use visual plots to show effect of step size and stiffness  
- Encourage coding exercises in Python, MATLAB, or Excel  

